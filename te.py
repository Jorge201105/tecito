

class Te:
    duracion = 365 #atributo de clas"tiempoe 365 días

    sabores = {
        1 : {"Nombre":"Te Negro","Tiempo":3,"recomendacion": "Desayuno"},
        2 : {"Nombre":"Te verde","Tiempo":5,"recomendacion": "Almuerzo"},
        3 : {"Nombre":"agua de hierbas","Tiempo":6,"recomendacion": "Once"},
    }

    precios = {
        300 : 3000,
        500 : 5000
    }


    @staticmethod
    def receta(sabor:int):
        """
        Esta función retorna el tiempo de preparacion en minutos y una recomenacion segun el sabor ingresado 
        
        """
        pedido = Te.sabores[sabor]

        return pedido["Nombre"], pedido["Tiempo"],pedido["recomendacion"]
    


    @staticmethod
    def obtener_precio(formato:int):
        """Retorna precio para formato indicado"""

        return Te.precios[formato]
    





