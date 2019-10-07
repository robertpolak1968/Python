# Fig. 4.4: fig04_04.py
# Creating and using a programmer-defined function.

# function definition
def square( x,y ):
 return x * y

for x in range( 1, 11 ):
 if x<10 and (x*x)<10 : print x,'', x*x ,'',square( x,x*x )   
 if x<10 and (x*x)>10 : print x,'', x*x ,square( x,x*x )   
 else : print x,x*x ,square( x,x*x ) 
print