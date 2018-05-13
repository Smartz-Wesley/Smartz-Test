class Person ():
    def lopen(self):
        print("rechtervoet, linkervoer, rechtervoet, wat was het ook alweer...")

    def praten(self):
        print("Het enige dat ik kan is praten")

    def werken(self):
        print("Ben ik aan het werk?")

class Wesley (Person):
    def usa(self):
        print("Oh say can you see....")

class Jeffrey (Person):
    def antiajax(self):
        print("Bah, bah Ajax: joden, joden")

class Tim (Person):
    def best(self):
        print("Zoals mijn grote voorbeeld altijd aangaf, ik ben de beste!")

class Dennis (Person):
    def fortnite(self):
        print("Van het weekend zal ik eens gaan spelen")

w = Wesley()
j = Jeffrey()
t = Tim()
d = Dennis()

w.lopen()
w.praten()
w.werken()
w.usa()