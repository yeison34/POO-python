##integrantes:
        # Pedro Danilo Toro Dominguez
        # Yasson Brayan Pernguez Paz 

import Beneficio

nombre=input("Ingrese Nombre del Usuario => ")
apellido=input("Ingrese Apellido del Usuario => ")
cedula=input("Ingrese Cedula del Usuario => ")
edad=int(input("Ingrese la Edad del Usuario => "))
cuenta=float(input("Ingrese El Valor de Cuenta Inicial del Usuario => "))

cliente=Beneficio.Beneficio(nombre,apellido,cedula,edad,cuenta)
while True:
    op=int(input("Operaciones Bancarias:\n1.Consignar\n2.Retirar\n3.Mostrar Datos\n4.Salir => "))
    
    if op==1:
        cliente.consignar()
    if op==2:
        cliente.retirar()
    if op==3:
        print(cliente.mostrar()) 
    if op==4:
        break            