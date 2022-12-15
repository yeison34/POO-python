import Usuario

class Cuenta(Usuario.Usuario):
    def __init__(self,nombre,apellido,cedula,edad,dineroAhorrado):
        super().__init__(nombre,apellido,cedula,edad)
        self.dineroAhorrado=dineroAhorrado

    def getNombre(self):
        return "Su nombre es: " + self.nombre

    def setNombre(self,nombre):    
        self.nombre=nombre

    def getApellido(self):
        return "Su Apellido es: " + self.apellido

    def setApellido(self,apellido):    
        self.apellido=apellido

    def getEdad(self):
        return "Su Edad es: " + self.edad

    def setEdad(self,edad):    
        self.edad=edad

    def mostrar(self):
        return "Nombre: "+self.nombre + "\nApellido: " + self.apellido + "\nEdad: " + str(self.edad) + "\nDinero En Cuenta: "+  str(self.dineroAhorrado)            

    def consignar(self):
        consignacion=input("Valor a Consignar => ")
        
        while True:
            if float(consignacion)<0:
                print("Ingrese Valores Positivos ")
                consignacion=input("\nValor a Consignar => ")
            else:
                break     
        self.dineroAhorrado=self.dineroAhorrado+float(consignacion)

    def retirar(self):
        retirar=input("Valor a Retirar => ")
        
        while True:
            if float(retirar)<0:
                print("Ingrese Valores Positivos")
                retirar=input("\nValor a Retirar")
            else:
                break     
        self.dineroAhorrado=self.dineroAhorrado-float(retirar)

