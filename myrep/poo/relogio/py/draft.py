class Watch:
    def __init__(self, hora: int = 0, mini: int = 0, seg: int = 0):
        self.hora: int = 0
        self.mini: int = 0
        self.seg: int = 0
        self.set_hora(hora)
        self.set_min(mini)
        self.set_segundo(seg)

    def __str__(self) -> str:
        return f"{self.hora:02d}:{self.mini:02d}:{self.seg:02d}"

    def set_hora(self, hora: int):
        if 0 <= hora <= 23:
            self.hora = hora
        else:
            print("fail: hora invalida")

    def set_min(self, mini: int):
        if 0 <= mini <= 59:
            self.mini = mini
        else:
            print("fail: minuto invalido")

    def set_segundo(self, segundo: int):
        if 0 <= segundo <= 59:
            self.seg = segundo
        else:
            print("fail: segundo invalido")

    def nextSecond(self):
        self.seg += 1
        if self.seg == 60: 
            self.seg = 0
            self.mini += 1
        if self.mini == 60:
            self.mini = 0
            self.hora += 1
        if self.hora == 24:
            self.hora = 0

def main():
    # Teste 1
    watch = Watch()
    print("$show")
    print(watch)
    print("$end")

    # Teste 2
    watch = Watch()
    print("$show")
    print(watch)
    print("$set 10 02 30")
    watch.set_hora(10)
    watch.set_min(2)
    watch.set_segundo(30)
    print("$show")
    print(watch)
    print("$end")

    # Teste 3
    watch = Watch()
    print("$set 10 02 30")
    watch.set_hora(10)
    watch.set_min(2)
    watch.set_segundo(30)
    print("$show")
    print(watch)
    print("$set 15 50 59")
    watch.set_hora(15)
    watch.set_min(50)
    watch.set_segundo(59)
    print("$show")
    print(watch)
    print("$end")

    # Teste 4
    print("$show")
    print(watch)
    print("$set 25 10 30")
    watch.set_hora(25)
    print("$show")
    print(watch)
    print("$end")

    # Teste 5
    print("$show")
    print(watch)
    print("$set 1 70 50")
    watch.set_hora(1)
    watch.set_min(70)
    print("$show")
    print(watch)
    print("$end")

    # Teste 6
    print("$show")
    print(watch)
    print("$set 23 59 70")
    watch.set_hora(23)
    watch.set_min(59)
    watch.set_segundo(70)
    print("$show")
    print(watch)
    print("$end")

    # Teste 7
    print("$show")
    print(watch)
    print("$set 15 59 59")
    watch.set_hora(15)
    watch.set_min(59)
    watch.set_segundo(59)
    print("$show")
    print(watch)
    print("$end")

    # Teste 8
    print("$set 15 59 59")
    watch.set_hora(15)
    watch.set_min(59)
    watch.set_segundo(59)
    print("$show")
    print(watch)
    print("$next")
    watch.nextSecond()
    print("$show")
    print(watch)
    print("$end")

    # Teste 9
    print("$set 23 59 59")
    watch.set_hora(23)
    watch.set_min(59)
    watch.set_segundo(59)
    print("$show")
    print(watch)
    print("$end")

    # Teste 10
    print("$set 23 59 59")
    watch.set_hora(23)
    watch.set_min(59)
    watch.set_segundo(59)
    print("$show")
    print(watch)
    print("$next")
    watch.nextSecond()
    print("$show")
    print(watch)
    print("$end")

    # Teste 11
    print("$init 10 20 30")
    watch = Watch(10, 20, 30)
    print("$show")
    print(watch)
    print("$end")

    # Teste 12
    print("$show")
    print(watch)
    print("$init 90 20 30")
    watch = Watch(90, 20, 30)
    print("$show")
    print(watch)
    print("$end")

    # Teste 13
    print("$init 90 100 60")
    watch = Watch(90, 100, 60)
    print("$show")
    print(watch)
    print("$end")

if __name__ == "__main__":
    main()