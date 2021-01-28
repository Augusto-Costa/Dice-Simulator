#Simulador de dados
#Simular o uso de um dado gerando um valor de 1 até 6
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Voce gostaria de gerar um novo valor para o dado?"
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if(resposta == "sim" or resposta == "s"):
                self.GerarValordoDado()
            elif(resposta == "não" or resposta == "n"):
                print("Ok, agradecemos sua participação ")

            else:
                print("Favor digitar sim ou não")
        except:
            print("Ocorreu um erro ao receber sua resposta! ")
    def GerarValordoDado(self):
        print(random.randint(self.valor_minimo , self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()


