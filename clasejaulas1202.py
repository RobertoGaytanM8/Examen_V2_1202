# CLASE
class Jaulas1202:
    # DICCIONARIOS
    def Jaula1202(self):
        MiJaula={"ID":2222,
                    "Tipo": "Estandar",
                    "Capacidad": 20, 
                    "Tamaño": "Grande " ,
                    "Agua (Numero de contenedores)": 30, 
                    "Comida (Numero de contenedores)": 25,
                    "Candado": "Normal"}
        print(MiJaula)
        for info,cant in MiJaula.items():
            print(f"{info}: {cant}")
    
    def Perro1202(self):
        MiPerro={"ID":3032,
                    "Raza": "French Poodle",
                    "Edad": 3, 
                    "Comportamiento": "Amigable" ,
                    "Vacunas": 10, 
                    "Fech_ing": "19/JUL/21",
                    "Sexo": "Macho"}
        print(MiPerro)
        for infop,datap in MiPerro.items():
            print(f"{infop}: {datap}")
    

    def Refugios1202(self):
        MiRefugio={"ID":1185,
                    "Cant. Perros": 120,
                    "Empleados": 8, 
                    "Telefono": 6561234567 ,
                    "Cant Comida": "50kg", 
                    "Fundacion": "30/NOV/05",
                    "Encargado": "Nicolas"}
        print(MiRefugio)
        for info,data in MiRefugio.items():
            print(f"{info}: {data}")
    
    def Empleado1202(self):
        MiEmpleado={"ID":6488,
                    "Nombre": "Sebastian",
                    "Apellidos": "Rojas Mata", 
                    "DNI": 1234567 ,
                    "Salario": "$4000", 
                    "Fech Ingr": "14/JUL/07",
                    "Sexo": "Masculino"}
        print(MiEmpleado)
        for info,data in MiEmpleado.items():
            print(f"{info}: {data}")

    

# OBJETO
objeto1202=Jaulas1202()
print("")
print("INFROMACION DE JAULAS:")
objeto1202.Jaula1202()
print("")
print("INFROMACION DEL PERRO:")
objeto1202.Perro1202()
print("")
print("INFROMACION DEL REFUGIO:")
objeto1202.Refugios1202()
print("")
print("INFROMACION DEL EMPLEADO:")
objeto1202.Empleado1202()






