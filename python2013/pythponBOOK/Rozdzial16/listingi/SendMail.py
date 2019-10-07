from email import Encoders
from email.Message import Message
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMENonMultipart import MIMENonMultipart
import mimetypes

class SmartMessage:

    """Uproszczony interfejs dla bibliotek Pythona, który potrafi tworzyæ
    wiadomoœci tekstowe i z za³¹cznikami MIME."""

    def __init__(self, fromAddr, toAddrs, subject, body, enc='iso-8859-2'):
        """Zacznij od za³o¿enia, i¿ bêdzie to prosta wiadomoœæ tekstowa
        zgodna z RFC 2822 i bez MIME."""    
        self.msg = Message()
        self.msg.set_payload(body)
        self['Subject'] = subject
        self.setFrom(fromAddr)
        self.setTo(toAddrs)
        self.hasAttachments = False
        self.enc = enc

    def setFrom(self, fromAddr):
        "Ustawia adres nadawcy wiadomoœci."
        if not fromAddr or not type(fromAddr)==type(''):
            raise Exception, 'Wiadomoœæ musi mieæ jednego i tylko jednego nadawcê.'
        self['From'] = fromAddr

    def setTo(self, to):
        "Ustawia adresy osób, które maj¹ otrzymaæ wiadomoœæ."
        if not to:
            raise Exception, 'Wiadomoœæ musi mieæ co najmniej jednego odbiorcê.'
        self._addresses(to, 'To')

        #Dodatkowo przechowuj adresy jako listê. Byæ mo¿e
        #skorzysta z niej kod, który zajmie siê wysy³aniem wiadomoœci.
        self.to = to

    def setCc(self, cc):
        """Ustawia adresy osób, które maj¹ otrzymaæ kopiê wiadomoœc. choæ
        nie jest ona adresowana do nich w sposób bezpoœredni."""
        self._addresses(cc, 'Cc')

    def addAttachment(self, attachment, filename, mimetype=None):
        "Do³¹cza do wiadomoœci wskazany plik."

        #Odgadnij g³ówny i dodatkowy typ MIME na podstawie nazwy pliku.
        if not mimetype:
            mimetype = mimetypes.guess_type(filename)[0]
        if not mimetype:
            raise Exception, "Nie uda³o siê okreœliæ typu MIME dla", filename
        if '/' in mimetype:
            major, minor = mimetype.split('/')
        else:
            major = mimetype
            minor = None

        #Wiadomoœæ by³a konstruowana z za³o¿eniem, i¿ bêdzie zawieraæ
        #tylko i wy³¹cznie tekst. Poniewa¿ wiem, ¿e bêdzie zawieraæ
        #co najmniej jeden za³¹cznik, musimy zmieniæ j¹ na wiadomoœæ
        #wieloczêœciow¹ i wkleiæ tekst jako pierwsz¹ czêœæ.        
        if not self.hasAttachments:
            body = self.msg.get_payload()
            newMsg = MIMEMultipart()
            newMsg.attach(MIMEText(body,'plain',self.enc))
            #Skopiuj stare nag³ówki do nowego obiektu.
            for header, value in self.msg.items():
                newMsg[header] = value
            self.msg = newMsg
            self.hasAttachments = True
        subMessage = MIMENonMultipart(major, minor, name=filename)
        subMessage.set_payload(attachment)

        #Zakoduj teksty jako quoted printable natomiast wszystkie 
        #inne typy jako base64.
        if major == 'text':            
            encoder = Encoders.encode_quopri
        else:
            encoder = Encoders.encode_base64
        encoder(subMessage)        

        #Powi¹¿ fragment MIME z g³ówn¹ wiadomoœci¹.
        self.msg.attach(subMessage)        

    def _addresses(self, addresses, key):
        """Ustawia zawartoœæ nag³ówka na podstawie listy przekazanych adresów."""
        if hasattr(addresses, '__iter__'):
            addresses = ', '.join(addresses)
        self[key] = addresses

    #Kilka metod dodatkowych umo¿liwiaj¹cych traktowanie klasy w podobny
    #sposób, jak klasy Message lub MultipartMessage, stosuj¹c odpowiedni¹
    #delegacjê poleceñ do tych klas.
    def __getitem__(self, key):
        "Zwróæ nag³ówek o podanym kluczu."
        return self.msg[key]

    def __setitem__(self, key, value):
        "Ustaw nag³ówek o wskazanej nazwie."
        self.msg[key] = value

    def __getattr__(self, key):
        return getattr(self.msg, key)

    def __str__(self):
        "Zwróæ tekstow¹ reprezentacjê wiadomoœci."
        return self.msg.as_string()

from smtplib import SMTP
class MailServer(SMTP):

    "Bardziej przyjazny dla u¿ytkownika interfejs klasy SMTP."

    def __init__(self, server, serverUser=None, serverPassword=None, port=25):
        "Po³¹cz siê z serwerem SMTP."
        SMTP.__init__(self, server, port)
        self.user = serverUser
        self.password = serverPassword
        #Usuñ znak komentarza z poni¿szego wiersza, by zobaczyæ ca³¹ wymianê komunikatów.
        #self.set_debuglevel(True)

    def sendMessage(self, message):
        "Wyœlij wiadomoœæ za pomoc¹ serwera SMTP."
        #Niektóre serwery wymagaj¹ uwierzytelnienia.
        if self.user:
            self.login(self.user, self.password)

        #Wiadomoœæ zawiera listê adresów docelowych, które mog¹ zawieraæ
        #dodatkowe nazwy, na przyk³ad "Jan Kowalski <jan@przyklad.pl>".
        #Niektóre serwery pocztowe obs³uguj¹ jedynie czyste adresy,
        #wiêc musimy utworzyæ wersjê, która nie zawiera nazw.
        destinations = message.to
        if hasattr(destinations, '__iter__'):
            destinations = map(self._cleanAddress, destinations)
        else:
            destinations = self._cleanAddress(destinations)
        self.sendmail(message['From'], destinations, str(message))

    def _cleanAddress(self, address):
        "Przekszta³ca 'Nazwa <email@domena>' na 'email@domena'."
        parts = address.split('<', 1)
        if len(parts) > 1:
            #Ten adres zawiera tak naprawdê nazwê i adres:
            newAddress = parts[1]
            endAddress = newAddress.find('>')
            if endAddress != -1:                    
                address = newAddress[:endAddress]
        return address

##msg = SmartMessage("Me <me@example.com",
##                   "You <you@example.com>",
##                   "Your picture",
##                   "Here's that picture I took of you.")
##msg.addAttachment(open("photo.jpg").read(), "photo.jpg")
##MailServer("localhost").sendMessage(msg)
