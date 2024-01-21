import scrapy
class Library:

    def __init__(self, name, location, size):
        self.name = name
        self.location = location
        self.size = size
    
    @staticmethod
    def IsLibrary():
        return True

library_1 = Library("okul kütüphanesi", "Maltepe", "Large")

print(library_1.location)

print(Library.IsLibrary())
print(library_1.IsLibrary())