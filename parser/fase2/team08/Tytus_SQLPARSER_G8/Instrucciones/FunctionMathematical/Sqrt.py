import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones.Aritmetica import Aritmetica
from Instrucciones.Expresiones.Primitivo import Primitivo

class Sqrt(Instruccion):
    def __init__(self, valor, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.NUMERIC),linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if self.valor.tipo.tipo != Tipo_Dato.SMALLINT and self.valor.tipo.tipo != Tipo_Dato.INTEGER and self.valor.tipo.tipo != Tipo_Dato.BIGINT and self.valor.tipo.tipo != Tipo_Dato.DECIMAL and self.valor.tipo.tipo != Tipo_Dato.NUMERIC and self.valor.tipo.tipo != Tipo_Dato.REAL and self.valor.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION:
            error = Excepcion('42883',"Semántico","No existe la función sqrt("+self.valor.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if resultado < 0:
            error = Excepcion('42883',"Semántico","No se puede calcular la raíz cuadrada un de número negativo",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if isinstance(resultado,int):
            return int(math.sqrt(resultado))
        else:
            return math.sqrt(resultado)
        
    def analizar(self, tabla, arbol):
        return super().analizar(tabla, arbol)

    def traducir(self, tabla, arbol):
        super().traducir(tabla, arbol)
        if isinstance(self.valor, Primitivo):
            return f"SQRT({self.valor.traducir(tabla,arbol).temporalAnterior})"
        elif isinstance(self.valor, Aritmetica):
            return f"SQRT({self.valor.concatenar(tabla,arbol)})"
        return f"SQRT({self.valor.traducir(tabla,arbol)})"