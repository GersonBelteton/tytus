from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Columna(Instruccion):
    def __init__(self, nombre, tipo, constraint, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)
        self.nombre = nombre
        self.tipo = tipo
        self.constraint=constraint
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)