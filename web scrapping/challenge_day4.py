
result = 0
notExit = True

while notExit :
  num1 = int(input("Choose a number : "))
  num2 = int(input("Choose another one : "))
  
  op = input("Choose an operation : \n Options are : +,-,* or /.\n Write 'exit' to finish.\n")
    
  if op == '+':
    result = num1 + num2
  elif op == '-':
    result = num1 - num2
  elif op == '*':
    result = num1 * num2
  elif op == '/':
    result = num1 / num2
  elif op == "exit":
    notExit = False;
    
  if op != "exit":
    print("Result : ", result)
    