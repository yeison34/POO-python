import Cuenta

class Beneficio (Cuenta.Cuenta):
    interes=0.05
    def __init(self,nombre,apellido,cedula,edad,dineroAhorrado):
        super().__init__(self,nombre,apellido,cedula,edad,dineroAhorrado)

    def mayorEdad(self):
        if self.edad>=18 and self.edad<28:
            return True
        else:
            return False  

    def mostrar(self):
        if self.mayorEdad:
            total=self.dineroAhorrado+self.dineroAhorrado*self.interes
            return super().mostrar()+"\nPor ser Mayor de edad tendras una bonificacion del 5%\nSaldo total: "+str(total)
        else:
            return super().mostrar
