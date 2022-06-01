#Function Basic 

def PLUS(a , b):
  c = a+b
  print("plus is "+str(c))

def Minus(a, b):
  c = a-b
  print("minus is "+str(c))
  
def Multiply(a, b):
  c = a*b
  print("product is "+str(c))

def Divide(a, b):
  c = a/b
  print("quotient is "+str(c))

def POW (a,b):
  c = pow(a, b)
  print("square is "+str(c))

condition = True

while(condition == True):
  print("---------------------------[Calculator]-------------------------")
  print("Calculator + - * / ^")
  number1=int(input(" number 1:"))
  number2=int(input(" number 2:"))
  operator=input(" operator? (+ - * / ^):")
  
  if (operator=="+") :
    PLUS (number1,number2)
  elif(operator=="-") :
    Minus (number1,number2)
  elif(operator=="*") :
    Multiply (number1, number2)
  elif(operator=="/") :
    if(number2==0) :
      print("anwser is infinity")
    else: 
      Divide (number1, number2)
  elif(operator=="^") :
    POW (number1, number2)
  else:
    print("[ERROR] Not an operator. Try again!!")

  print("----------------------------------------------------------------")
  user_answer = input("Press [N] to quit, Any key to continue.")
  if ( user_answer=="N" or  user_answer=="n"):
    condition=False
  else:
    condition=True


#Make Calculator with Function