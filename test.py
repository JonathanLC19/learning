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

#book1 = Book()

#type(book1)

#print(book1)

#print(Book.is_electronic)

#print(Book.__doc__)

book2 = Book("El Señor de los Anillos", "JRR Tolkien", False)

print(book2.title)
print(book2.author)
print(book2.is_electronic)
print(book2.__dict__)

book3 = Book("Harry Potter")

print(book3.is_electronic)
print(book3.__dict__)

##Ejercicio
##Vamos a crear la clase RationalNumber. Vamos a configurar el constructor de modo que haya un atributo numerator y otro denominator, este último con 1 como valor por defecto. Ambos atributos deben ser números enteros.

class RationalNumber():

  def __init__(self, n, d = 1):
    if type(n) is int and type(d) is int:
      self.numerator = n
      self.denominator = d
    else:
      print("numerador y denominador deben ser enteros")



rn1 = RationalNumber(3)

print(rn1.__dict__)

##Método Deconstructor

