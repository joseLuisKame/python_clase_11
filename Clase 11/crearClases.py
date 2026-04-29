class triangulo:
 base = 0
 altura = 0
 area = 0

 def __init__(self, base, altura):
    self.base = base
    self.altura = altura

 def area(self): 
    self.area = (self.base * self.altura) / 2
    print("El área del triángulo es:", self.area)
         
objtriangulo1 = triangulo(10, 5)

objtriangulo1.area()
print("Base:", objtriangulo1.base)  
print("Altura:", objtriangulo1.altura)
print("Área:", objtriangulo1.area)

