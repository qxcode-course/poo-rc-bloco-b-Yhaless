class Camisa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        if valor in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__tamanho = valor
        else:
            print("Erro: O tamanho deve ser; PP, P, M, G, GG ou XG")

camisa = Camisa()

while camisa.getTamanho() == "":
    print("Digite seu tamanho de camisa")
    tamanho = input()
    camisa.setTamanho(tamanho)

print("Parabens, você comprou uma camisa tamanho", camisa.getTamanho())