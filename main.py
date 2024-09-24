from lib import cuadrado
from lib import triangulo
print("Proyecto Figuras")
lado = 4
print(f"El área de un  cuadrado de lado {lado} es : {cuadrado.get_area(lado)}")

lado1=5
lado2 =3
lado3=4
h=2
print(f"El área de un  triángulo de lado {lado1,h} es : {triangulo.get_area(lado1,h)}")