  
import random
while True:


     

 print(" 1 pedra")
 print(" 2 papel")
 print(" 3 tesoura")


 escolha = int(input("escolha uma opcao: "))

 computador = random.randint(1,3)
 print("Computador escolheu: ", computador)
 
 if escolha == computador:
        print("Empate!")

 elif escolha == 1 and computador == 3:
        print("Você venceu!")

 elif escolha == 2 and computador == 1:
        print("Você venceu!")

 elif escolha == 3 and computador == 2:
        print("Você venceu!")

 else:
        print("Computador venceu!")