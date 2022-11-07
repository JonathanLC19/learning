###Clases en python


class Book():
  ##docstrings
  """
  Clase para trabajar con libros
  """
  ##Variable estática
  #is_electronic = False

  ##Método Constructor
  def __init__(self, title, author, electronic):
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
print(book2.electronic)
print(book2.__dict__)

