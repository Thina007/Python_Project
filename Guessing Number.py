import numpy as np
from numpy import random


while(1):

 a=random.randint(10)
 b=random.randint(10)
 c=random.randint(10)
 d=random.randint(10)
 e=random.randint(10)
 f=random.randint(10)
 g=random.randint(10)

 while(1):
      
   print("______________________________________________________________________________")


   print("\n\n",[a],[b],[c],[d],[e],[f],[g])

 
   print("\nIf You Want To Guess the Number Press(N)!! 'or' You Want a  Clue Press(C)")
  
   ch=input("\nEnter Your Chooice:")
   thina=[a,b,c,d,e,f,g]
   r=random.choice(thina)
   
   









   if( ch=="c" or ch=="C"):
      print("\n 1st Clue so You Loose 25 point's outof 100 Point's")
      if r==2 or  r==4 or r==6  or r==8:
           print("\n => The Number is Divided By Even Number")
           
      if r==0 or r==3 or r==1 or r==5 or r==7:
           print("\n => My One of the favorite Number")
           
      if r==0 or r==1 or r==2 or r==3 or r==4 or r==5:
           print("\n => Lower Number")

      if r==6 or r==7 or r==8 or r==9 or r==10:
           print("\n => Higer Number")
         
      nu=input("\n \n Press 'N' to Enter Guessing Number or Press 'S' for Second Clue:")
      if nu=="n" or nu=="N":
         n=int(input("\n Enter The Number You are Guessing Correctly:"))  
         if r==n:
          print("\n You are 'Winner'")
          print("\n You Score:75 Point's")
          print("\n My Guessing also Number is:",r)
          break
     
         else:
          print("\n You are Looser !! BeterLuck  Next Time!!!")
          print("\n You Score:0 Point's")
          print("\n My Guessing Number is:",r)
          break












      if(nu!="n"):
       if nu=="s" or nu=="S":
           print("\n \n  2nd Clue so You Loose Again 25 point's outof 75 Point's")
           if r==3 or  r==7 or r==8  or r==9 or r==5:
             print("\n => My favorite Cricketar's T-shirt Number !!")
           
           if r==4 or r==6 :
             print("\n =>Number Divided By 2")
           
           if r==0 or  r==1 or r==2 or r==3:
              print("\n =>Very Lower Number")

           if r==8 or r==9 or r==10:
               print("\n =>Very Higer Number")
    
      if(nu!="n" or nu!="N"):
       nuu=input("\n Press 'N' to Enter Guessing Number or Press 'G' for Giveup!!:")

       if nuu=="n" or nuu=="N":
         n=int(input("\n Enter The Number You are Guessing Correctly:"))  
         if r==n:
          print("\n You are 'Winner'")
          print("\n You Score:50 Point's")
          print("\n My Guessing also Number is:",r)
          break
     
         else:
          print("\n You are Looser BeterLuck  Next Time!!!")
          print("\n You Score:0 Point's")
          print("\n My Guessing Number is:",r)
          break


       if nuu=="g" or nuu=="G":
           print("\n Sorry Our are Out!! BeterLuck  Next Time!!!")
           print("\n My Guessing Number is:",r)
           break
    










   if(ch=="n" or ch=="N"):
    n=int(input("\nEnter The Number Your are Guessing:"))
   
    if r==n:
       print("\n You are 'Winner'")
       print("\n You Score: 100 Point's")
       print("\n My Guessing also Number is:",r)
       break
     
    else:
     print("\n You are Looser!! BeterLuck  Next Time!!!")
     print("\n You Score:0 Point's")
     print("\n My Guessing Number is:",r)
     break

 
