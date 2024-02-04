print ("The calculater you need\n")
print ("Enter + to do Addition\n")
print ("Enter - to do Substract\n")
print ("Enter * to do Multipication\n")
print ("Enter / to do Divison\n")
ui=input("Enter a choice: ")
if ui=="+":
  num1=float(input("Enter first number: \n"))
  num2=float(input("Enter sceond number: \n"))
  sol=num1+num2
  res=str(sol)
  print("your result: "+res,)

elif ui=="-":
  num1=float(input("Enter first number: \n"))
  num2=float(input("Enter sceond number: \n"))
  sol=num1-num2
  res=str(sol)
  print("your result: "+res,)

elif ui=="*":
  num1=float(input("Enter first number: \n"))
  num2=float(input("Enter sceond number: \n"))
  sol=num1*num2
  res=str(sol)
  print("your result: "+res,)

elif ui=="/":
  num1=float(input("Enter first number: \n"))
  num2=float(input("Enter sceond number: \n"))
  sol=num1/num2
  res=str(sol)
  print("your result: "+res,)
 
else :
  print("Plzz Enter Right choice: ")

  

