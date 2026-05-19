class Moneda:
    # diccionario con simbolos de moneda según pais
    __dict_simbolo ={"CAD":"$","USD":"$","MXN":"$","BZD":"BZ$","GTQ":"Q","HNL":"L","NIO":"C$",
                    "PAB":"B/.","XCD":"EC$","BSD":"B$","BBD":"Bds$","CUP":"$","HTG":"G","JMD":"J$",
                    "DOP":"RD$","TTD":"TT$","GYD":"G$","PEN":"S/","CLP":"$","CRC":"₡","ARS":"$",
                    "BOB":"Bs","BRL":"R$","COP":"$","PYG":"₲","SRD":"$","UYU":"$U","VED":"Bs.D"}
    
    @staticmethod
    def __invertirFormatoDefault(temp):
        # Formatear para . miles , decimal
        return temp.replace(",", "X").replace(".", ",").replace("X", ".")

    @staticmethod
    def moneda(valor, simbolo):
        simbolo = simbolo.upper().strip()

        # Formatear moneda , mile . decimal
        temp = "{:,.2f}".format(valor)

        # Paises con formato . miles , decimal 
        otro_formato_pais = ["CLP", "CRC", "ARS", "BOB", "BRL", "COP", "PYG", "SRD", "UYU", "VED"]
        if simbolo in otro_formato_pais:
            temp = Moneda.__invertirFormatoDefault(temp)

        # Agregamos simbolo según país a traves de diccionarios dentro de lista
        monedaFormateada = Moneda.__dict_simbolo[simbolo]+temp

        # Devolvemos resultado
        return monedaFormateada
    
    @staticmethod
    def tipoMoneda():
        tipo = "CAD, USD, MXN, BZD, GTQ, HNL, NIO, PAB, XCD, BSD, BBD, CUP, HTG, JMD, DOP, TTD, GYD, PEN, CLP, CRC, ARS, BOB, BRL, COP, PYG, SRD, UYU, VED"
        lista_tipos = tipo.split(", ")
        
        # Listar los tipos de monedas a formatear
        return lista_tipos