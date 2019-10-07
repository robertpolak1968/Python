from email import Encoders
from email.Message import Message
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMENonMultipart import MIMENonMultipart
import mimetypes

class SmartMessage:

    """Uproszczony interfejs dla bibliotek Pythona, kt�ry potrafi tworzy�
    wiadomo�ci tekstowe i z za��cznikami MIME."""

    def __init__(self, fromAddr, toAddrs, subject, body, enc='iso-8859-2'):
        """Zacznij od za�o�enia, i� b�dzie to prosta wiadomo�� tekstowa
        zgodna z RFC 2822 i bez MIME."""    
        self.msg = Message()
        self.msg.set_payload(body)
        self['Subject'] = subject
        self.setFrom(fromAddr)
        self.setTo(toAddrs)
        self.hasAttachments = False
        self.enc = enc

    def setFrom(self, fromAddr):
        "Ustawia adres nadawcy wiadomo�ci."
        if not fromAddr or not type(fromAddr)==type(''):
            raise Exception, 'Wiadomo�� musi mie� jednego i tylko jednego nadawc�.'
        self['From'] = fromAddr

    def setTo(self, to):
        "Ustawia adresy os�b, kt�re maj� otrzyma� wiadomo��."
        if not to:
            raise Exception, 'Wiadomo�� musi mie� co najmniej jednego odbiorc�.'
        self._addresses(to, 'To')

        #Dodatkowo przechowuj adresy jako list�. By� mo�e
        #skorzysta z niej kod, kt�ry zajmie si� wysy�aniem wiadomo�ci.
        self.to = to

    def setCc(self, cc):
        """Ustawia adresy os�b, kt�re maj� otrzyma� kopi� wiadomo�c. cho�
        nie jest ona adresowana do nich w spos�b bezpo�redni."""
        self._addresses(cc, 'Cc')

    def addAttachment(self, attachment, filename, mimetype=None):
        "Do��cza do wiadomo�ci wskazany plik."

        #Odgadnij g��wny i dodatkowy typ MIME na podstawie nazwy pliku.
        if not mimetype:
            mimetype = mimetypes.guess_type(filename)[0]
        if not mimetype:
            raise Exception, "Nie uda�o si� okre�li� typu MIME dla", filename
        if '/' in mimetype:
            major, minor = mimetype.split('/')
        else:
            major = mimetype
            minor = None

        #Wiadomo�� by�a konstruowana z za�o�eniem, i� b�dzie zawiera�
        #tylko i wy��cznie tekst. Poniewa� wiem, �e b�dzie zawiera�
        #co najmniej jeden za��cznik, musimy zmieni� j� na wiadomo��
        #wielocz�ciow� i wklei� tekst jako pierwsz� cz��.        
        if not self.hasAttachments:
            body = self.msg.get_payload()
            newMsg = MIMEMultipart()
            newMsg.attach(MIMEText(body,'plain',self.enc))
            #Skopiuj stare nag��wki do nowego obiektu.
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

        #Powi�� fragment MIME z g��wn� wiadomo�ci�.
        self.msg.attach(subMessage)        

    def _addresses(self, addresses, key):
        """Ustawia zawarto�� nag��wka na podstawie listy przekazanych adres�w."""
        if hasattr(addresses, '__iter__'):
            addresses = ', '.join(addresses)
        self[key] = addresses

    #Kilka metod dodatkowych umo�liwiaj�cych traktowanie klasy w podobny
    #spos�b, jak klasy Message lub MultipartMessage, stosuj�c odpowiedni�
    #delegacj� polece� do tych klas.
    def __getitem__(self, key):
        "Zwr�� nag��wek o podanym kluczu."
        return self.msg[key]

    def __setitem__(self, key, value):
        "Ustaw nag��wek o wskazanej nazwie."
        self.msg[key] = value

    def __getattr__(self, key):
        return getattr(self.msg, key)

    def __str__(self):
        "Zwr�� tekstow� reprezentacj� wiadomo�ci."
        return self.msg.as_string()

from smtplib import SMTP
class MailServer(SMTP):

    "Bardziej przyjazny dla u�ytkownika interfejs klasy SMTP."

    def __init__(self, server, serverUser=None, serverPassword=None, port=25):
        "Po��cz si� z serwerem SMTP."
        SMTP.__init__(self, server, port)
        self.user = serverUser
        self.password = serverPassword
        #Usu� znak komentarza z poni�szego wiersza, by zobaczy� ca�� wymian� komunikat�w.
        #self.set_debuglevel(True)

    def sendMessage(self, message):
        "Wy�lij wiadomo�� za pomoc� serwera SMTP."
        #Niekt�re serwery wymagaj� uwierzytelnienia.
        if self.user:
            self.login(self.user, self.password)

        #Wiadomo�� zawiera list� adres�w docelowych, kt�re mog� zawiera�
        #dodatkowe nazwy, na przyk�ad "Jan Kowalski <jan@przyklad.pl>".
        #Niekt�re serwery pocztowe obs�uguj� jedynie czyste adresy,
        #wi�c musimy utworzy� wersj�, kt�ra nie zawiera nazw.
        destinations = message.to
        if hasattr(destinations, '__iter__'):
            destinations = map(self._cleanAddress, destinations)
        else:
            destinations = self._cleanAddress(destinations)
        self.sendmail(message['From'], destinations, str(message))

    def _cleanAddress(self, address):
        "Przekszta�ca 'Nazwa <email@domena>' na 'email@domena'."
        parts = address.split('<', 1)
        if len(parts) > 1:
            #Ten adres zawiera tak naprawd� nazw� i adres:
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
