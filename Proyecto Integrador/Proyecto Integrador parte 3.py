import os
import msvcrt
def limpiarTerminal():
    os.system('cls' if os.name=='nt' else 'clear')

def main ():
    numero = 0
    while numero <= 50:
     while not msvcrt.kbhit() or msvcrt.getch() != b'n':
      pass
     
     limpiarTerminal()
     print(f'Nuevo número: {numero}')
     numero += 1

if __name__ == "__main__":
    main()