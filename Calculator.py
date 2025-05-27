#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def add(a,b):
      return float(a)+float(b)
def sub(a,b):
      return float(a)-float(b)
def mul(a,b):
      return float(a)*float(b)
def divv(a,b):
      return float(a)/float(b)
def pow(a,b):
      return float(a)^float(b)
def rem(a,b):
      return float(a)%float(b)

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
import math
def select_op(x):
   while(x!="-1"):
      
      if(x=="$"):
         break
      
      elif(x=="#"):
         print("Done. Terminating")
         exit()
      else:
         try:
            a=input("Enter first number: ")                                   
            print(int(a))
            
         except:
            print(str(a))
            if(a=="#"): 
               print("Done. Terminating")            
               exit()
            break

         try:   
            b=(input("Enter second number: "))         
            print(int(b))
            
                        
         except:
            print(str(b))
            if(b=="#"): 
               print("Done. Terminating")            
               exit()
            break      


         if x =="+":
            return print(float(a),"+",float(b),"=", add(a,b))
         elif x =="-":
            return print(float(a),"-",float(b),"=", sub(a,b))
         elif x =="*":
            return print(float(a),"*",float(b),"=", mul(a,b))

         elif x =="/":
            if float(a)==0:
               print("float division by zero")
               return print(float(a),"/",float(b),"=","None")           
            elif float(b)==0:
               print("float division by zero")
               return print(float(a),"/",float(b),"=","None")
            else:
               return print(float(a),"/",float(b),"=", divv(a,b))
      

         elif x =="^":
            return print(float(a),"^",float(b),"=", pow(a,b))
         elif x =="%":
            return print(float(a),"%",float(b),"=", rem(a,b))
         exit()
   

#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()
