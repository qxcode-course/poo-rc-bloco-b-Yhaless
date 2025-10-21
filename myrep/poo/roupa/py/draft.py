class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def getTamanho(self) -> str:
        return self.__tamanho
        
    def setTamanho(self, valor: str):
        if valor in ["PP", "P", "M", "G" , "GG", "XG"]:
            self.__tamanho = valor
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")


#TESTES, DEPOIS DE FAZER TUDO "ERRADO"

#1 show
def main():
    roupa = Roupa()

    print("$show")
    tamanho_atual = roupa.getTamanho()
    if tamanho_atual == "":
        print("size: ()")
    else:
        print(f"size: ({tamanho_atual})")

#2 F

    print("$size F")
    roupa.setTamanho("F")

#3 Show

    print("$show")
    tamanho_atual = roupa.getTamanho()
    if tamanho_atual == "":
        print("size: ()")
    else:
        print(f"size: ({tamanho_atual})")

#4 PP

    print("$size PP")
    roupa.setTamanho("PP")

#5 show

    print("$show")
    tamanho_atual = roupa.getTamanho()
    if tamanho_atual == "":
        print("size: ()")
    else:
        print(f"size: ({tamanho_atual})")

#6 end
    print("$end")

main()

#ENTENDI ERRADO
'''
def main():
    roupa = Roupa()

    while True:
        comando = input().strip()

        if comando == "show":
            tamanho_atual = roupa.getTamanho()
            if tamanho_atual == "":
                print("size: ()")
            else:
                print(f"size: ({tamanho_atual})")

        elif comando.startswith("size "):
            partes = comando.split(" ", 1)
            if len(partes) == 2:
                valor = partes[1]
                roupa.setTamanho(valor)

        elif comando == "end":
            break

main()
'''