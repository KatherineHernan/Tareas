from readchar import readkey, key


print("Presiona una tecla")
while True:
  
  tecla = readkey()
  print("Presionaste", tecla)
  if tecla == '\x00H':
    break
  
