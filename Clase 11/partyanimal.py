class PartyAnimal:
    x = 0 # atributo de clase

    def party(self) : # método de instancia
        self.x = self.x + 1
        print("Hasta ahora", self.x)
        #print(type(self))