###Clases en python


class Book():
  ##docstrings
  """
  Clase para trabajar con libros
  """
  ##Variable estática
  #is_electronic = False

  ##Método Constructor
  def __init__(self, title, author = "", electronic = False):
    self.title = title
    self.author = author
    self.is_electronic = electronic

  ##Método Destructor

  #def __del__(self):
    #print("Llamada al método destructor de la clase. Objeto eliminado")

###MÉTODOS DE UNA CLASE
##Métodos de instancia (invocados por un objeto a través del parámetro ´self')

class Rectangle():
  def __init__(self, base = 1, height = 1, color = "blue"):
    self.base = base 
    self.height = height
    self.color = color

  def perimeter(self):
      return 2 * self.base + 2 * self.height

  def area(self):
      return self.base * self.height

  ##Añadir nuevos inputs a métodos de instancia
  def base_big(self, min = 5):
    if self.base > min:
      return True
    return False

  ##Método .__str__
  def __str__(self):
    return ("Base: {}\nAltura: {}".format(self.base, self.height))

  ##Método estático
  #Los métodos estáticos se definen usando el decorador `@staticmethod`, que se añade antes de definir el método estático respectivo.
  @staticmethod
  def equal_size(rect1,rect2):
    if rect1.base == rect2.base and rect1.height == rect2.height:
      return True
    return False
 
#-------------------------------------------------------------------------------- 
# book1 = Book()

#type(book1)

#print(book1)

#print(Book.is_electronic)

#print(Book.__doc__)

book2 = Book("El Señor de los Anillos", "JRR Tolkien", False)

#print(book2.title)
#print(book2.author)
#print(book2.is_electronic)
#print(book2.__dict__)

book3 = Book("Harry Potter")

##Eliminar un objeto con método destructor

#del book3

#print(book3.is_electronic)
#print(book3.__dict__)

##Ejercicio
##Vamos a crear la clase RationalNumber. Vamos a configurar el constructor de modo que haya un atributo numerator y otro denominator, este último con 1 como valor por defecto. Ambos atributos deben ser números enteros.

class RationalNumber():

  def __init__(self, n, d = 1):
    if type(n) is int and type(d) is int:
      self.numerator = n
      self.denominator = d
    else:
      print("numerador y denominador deben ser enteros")
  
  #Implementa el método de instancia .quotient() que devuelva el cociente
  def quotient(self):
    return self.numerator / self.denominator

  #Implementa el método de instancia .isInfinite() que devuelva si el denominador es 0 o no
  def isInfinite(self):
    if self.denominator == 0:
      return True
    return False

  #Implementa el método de instancia .simplify() que simplifique la fracción a la fracción irreducible


rn1 = RationalNumber(3,3)

#print(rn1.__dict__)

##Métodos de instancia

rect1 = Rectangle(4,2,"red")

#print("El perímetro es {}".format(rect1.perimeter()))
#print("El área es {}".format(rect1.area()))
#print(rect1.base_big())
rect1.base = 6

#print("El perímetro es {}".format(rect1.perimeter()))
#print("El área es {}".format(rect1.area()))

#print(rect1.base_big())

rect2 = Rectangle(12,10)

#print(rect2.base_big(14))

rect3 = Rectangle(12,10)

#print(int(rn1.quotient()))
#print(rn1.isInfinite())

print(rect2, "\n")
print(rect3, "\n")
print(Rectangle.equal_size(rect2, rect3))


