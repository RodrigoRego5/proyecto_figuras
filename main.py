from lib import cuadrado
from lib import rectangulo
from lib import triangulo
from lib import circunferencia
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado = 4
print(f"El área de un  {cuadrado.get_identificador} de lado {lado} es : {cuadrado.get_area(lado)} y el perímetro es : {cuadrado.get_perimetro(lado)}")

base = 4
altura=2
print(triangulo.get_identificador())
print(f"El área de un {triangulo.get_identificador()} de base {base} y altura {altura} es : {triangulo.get_area(base,altura)} y el perímetro es : {triangulo.get_perimetro(base)}")
print(f"El área de un  cuadrado de lado {lado} es : {cuadrado.get_area(lado)} y el perímetro es : {cuadrado.get_perimetro(lado)}")

base = 4
altura=2
print(rectangulo.get_identificador())
print(f"El área de un {rectangulo.get_identificador()} de base {base} y altura {altura} es : {rectangulo.get_area(base,altura)} y el perímetro es : {rectangulo.get_perimetro(base,altura)}")

radio = 3
print(circunferencia.get_identificador())
print(f"El área de una {circunferencia.get_identificador()} de radio {radio} es : {circunferencia.get_area(radio)}")