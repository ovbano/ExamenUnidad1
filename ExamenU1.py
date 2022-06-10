
'''
A continuación se va a presentar un programa que registre 
al personal acedémico de una institución educativa.
El personal solamente corresponde a la docencia de la institución.
Este programa se lo va realizar mediante clases las cuales se van
a detallar a continuación, y que contendran los seguiente atributos.

class personalAca:
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

Habrá una segunda clase que va a heredar a la super clase
esto implica que se va a poder accceder a la información,
atributos y variables de dicha super clase.

class docente(personalAca):
    def __init__(self, rol, departamento, salario):
        self.rol=rol
        self.departamento=departamento
        self.salario=salario

A continuación la codificación...
'''
#Creación de super clase
class personalAca:
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    

#creación de sub clase que hereda atributos de super clase
class docente(personalAca):
    def __init__(self, nombre, apellido, edad, rol, departamento, salario):
        super().__init__(nombre, apellido, edad)
        self.rol=rol
        self.departamento=departamento
        self.salario=salario
    
    def mostrarDatos(self):
        print("Sus datos ingresados son: ")
        for i in range(numPerosonal):
            print(listaPersonal[i])


    
print("-------------------Bienvenido querido usuario---------------")
print("Para su respectivo registro deberá llenar los siguientes campos")

listaPersonal=[]
docente1=docente("Valentin","Baño",23,"Físico","Ciencias exactas",423.15)

numPerosonal=int(input("Cuantas personas va a registrar "))
while (numPerosonal<=0):
    print("Ustede debe registra al menos a una persona, sin valores negativo")
    numPerosonal=int(input("Cuantas personas va a registrar "))
#Pedir datos al personal
for i in range(numPerosonal):
    #Ingresar un elemento con append(lo que quiera agregar)
    listaPersonal.append(input("Digite el nombre del personal {} que va a registrar: ".format(i+1) ))
    listaPersonal.append(input("Digite el apellido del personal {} que va a registrar: ".format(i+1) ))
    listaPersonal.append(int(input("Digite la edad del personal {} que va a registrar: ".format(i+1)) ))
    listaPersonal.append(input("Digite el rol que cumple la persona {} que va a registrar: ".format(i+1) ))
    listaPersonal.append(input("A que departamento pertenece la persona {} que va a registrar: ".format(i+1) ))
    listaPersonal.append(float(input("Cual es el salario de la persona {} que va a registrar: ".format(i+1)) ))

docente1.mostrarDatos()