###Clases en python

import random

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

  ##Método de clases
  #Este método usa la propia clase para crear un objeto
  @classmethod
  def random_rect(cls):
    base = random.randrange(1, 10)
    height = random.randrange(1, 10)
    return cls(base, height)
 
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

#print(rect2, "\n")
#print(rect3, "\n")
#print(Rectangle.equal_size(rect2, rect3))

rect4 = Rectangle().random_rect()
#print(rect4)


#PRÁCTICA: Crear una clase llamando a los atributos con método @property

class Person(object): #al ser una clase base que otras va a usar de herencia añadimos 'object' para dejarlo claro, pero no es necesario en la práctica
  def __init__(self, n, s, a):
    self.name = n
    self.surname = s
    self.age = a

  @property
  def completeName(self):
    return self.name +" "+self.surname
  
  #Parámetro .setter() para poder modificar una propiedad
  @completeName.setter
  def completeName(self, name_surname):
    n, s = name_surname.split(" ")
    self.name = n
    self.surname = s

  @property
  def createEmail(self):
    minusc = self.name
    return minusc.lower()+"@gamil.com"


miNombre = Person("Jonathan", "López", 42)

#print(miNombre.completeName +"\n"+ miNombre.createEmail)

##Herencias de clase
#Crear una clase a partir de otra
#Ej.: crear una clase Children y otra Adult a partir de la clase Person para determinar si la persona es mayor de edad o no 

class Children(Person):
  is_adult = False

class Adult(Person):
    is_adult = True

child1 = Children("Pablo", "López", 9)
print#(child1.completeName)
#print(child1.age)

##Crear una clase a partir de sobreescribir un método de otra

class secondName(Person):
  @property
  def completeName(self):
    return self.name +" "+self.surname

  @completeName.setter
  def completeName(self, name_surname):
    names = name_surname.split(" ") #esto separa los atributos convirtiéndolos en una lista
    self.surname = names[-1] # toma el último valor de la lista como el atributo apellido
    if len(names) > 2:
      self.name = " ".join(names[:len(names)-1]) #al haber sacado el último valor para apellido, la longitud de names quedaría como el nombre si tiene más de 2
    elif len(names) == 2:
      self.name = names[0]

  
brother = secondName("Luís", "López", 50)

brother.completeName = "Luis Miguel López"
<<<<<<< HEAD
#print(brother.__dict__)

sister = secondName("Mariola", "López", 51)
#print(sister.__dict__)


class Developer(Person):

  def __str__(self):
    return "EL desarrollador que creó este código se llama {}".format(super().completeName)

class ProgLang(object):

  @staticmethod
  def progVersion(language, version):
    print("El lenguaje de programación que usa es {} {}".format(language, version))

dev1 = Developer("Jonathan", "López", 42)
#print(dev1)

#lang1 = ProgLang.progVersion("Python", "3.14")
#print(lang1)

class DevProfile (Developer, ProgLang):
  pass

developer = DevProfile("Pepe", "Pérez", 23)
print(developer)
DevProfile.progVersion("Java", "12.0")

=======
print(brother.__dict__)

sister = secondName("Mariola", "López", 51)
print(sister.__dict__)


>>>>>>> 6f87f8a5a2d573b714fd654748accb922269c6bc
