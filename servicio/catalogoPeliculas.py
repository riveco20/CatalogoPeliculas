import os

class CatalogoPeliculas:

    rutaArchivo ='peliculas.txt'

    # accede directamente a los atributos de la clase

    @classmethod
    def agregarPelicula(cls,pelicula):
        with open(cls.rutaArchivo,'a',encoding='utf8') as archivo:#a permite escribir
          archivo.write(f'{pelicula.nombre}\n')#write permite abrir y cerrar el archivo

    #Listar pelicula

    @classmethod
    def listarPelicula(cls):
        with open(cls.rutaArchivo,'r',encoding='utf8') as archivo:
            print(f'Catalogo De peliculas'.center(50,'_'))
            print(archivo.read())

    @classmethod
    def eliminarPelicula(cls):
        os.remove(cls.rutaArchivo)
        print(f'Archivo Eliminado: {cls.rutaArchivo}')


