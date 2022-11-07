###Clases en python

##Variable estática

class Book():
  """
  Clase para trabajar con libros
  """

  is_electronic = False

book1 = Book()

type(book1)

#print(book1)

#print(Book.is_electronic)

##docstrings
print(Book.__doc__)