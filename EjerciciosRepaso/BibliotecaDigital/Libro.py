class Libro:
    def __init__(self, titulo, autor, anio):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
    

    def get_titulo(self):
        return self._titulo
    
    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_autor(self):
        return self._autor
    
    def set_autor(self, autor):
        self._autor = autor
    
    def get_anio(self):
        return self._anio