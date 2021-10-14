from os import system

class Lavado:
    def __init__(self,tipo,precio):
        self.tipo=tipo
        self.precio=precio
        self.contador=0

    def incrementarContador(self):
        self.contador+=1
    
    def total(self):
        return self.contador * self.precio

lavadoBasico=Lavado('basico',300)
lavadoFull=Lavado('full',500)

class Empleado:
    def __init__(self,id,nombre,apellido):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.ventas=0

    def venta(self,monto):
        self.ventas+=monto
    
    def total(self):
        return self.ventas

Em1=Empleado('Juan','Romero',1)
Em2=Empleado('Maria','Ortiz',2)
Em3=Empleado('Ricardo','Escobar',3)
Em4=Empleado('Matias','Cueto',4)

class Auto:
    def __init__(self,precio,tipo):
        self.precio=precio
        self.tipo=tipo
        self.contador=0
    
    def incrementarContador(self):
        self.contador+=1

AutoChico=Auto('chico',100)
AutoGrande=Auto('grande',300)

Op=0
lavado=''
auto=''
contador=0

while (Op!=9):
    
    lavadoPrecio=0
    print("-----------------------Menú Principal----------------------------------")
    print("1.- Nuevo Servicio")
    print("9.- Salir y ver Estadisticas finales")
    Op=int(input())
    
    if (Op==1):
        print('Ingresar Id de empleado')
        print('1-', Em1.nombre, Em1.apellido, '2-', Em2.nombre, Em2.apellido, '3-', Em3.nombre, Em3.apellido, '4-', Em4.nombre, Em4.apellido)
        Op=int(input())
        print('Ingrese tipo de servicio (basico/full):')
        lavado=input()
        print('Ingrese tipo de auto (chico/grande):')
        auto=input()
        contador+=1
        if (lavado==lavadoBasico.tipo):
            lavadoBasico.incrementarContador()
            lavadoPrecio+=lavadoBasico.precio
        elif (lavado==lavadoFull.tipo):
            lavadoFull.incrementarContador()
            lavadoPrecio+=lavadoFull.precio
        else:
            print('¡Ingresó un tipo de lavado incorrecto!')
        if (auto==AutoChico.tipo):
            AutoChico.incrementarContador()
            lavadoPrecio+=AutoChico.precio
        elif (auto==AutoGrande.tipo):
            AutoGrande.incrementarContador()
            lavadoPrecio+=AutoGrande.precio
        else:
            print('¡Ingresó un tipo de auto incorrecto!')
        if (Op==1):
            Em1.venta(lavadoPrecio)
        elif (Op==2):
            Em2.venta(lavadoPrecio)
        elif (Op==3):
            Em3.venta(lavadoPrecio)
        elif (Op==4):
            Em4.venta(lavadoPrecio)
        system("cls")
    
    elif (Op==9):
        print('Total por empleado:')
        print('Empleado 1:', Em1.total())
        print('Empleado 2:', Em2.total())
        print('Empleado 3:', Em3.total())
        print('Empleado 4:', Em4.total())
        print('Total por tipo de lavado:')
        print('Básico:', lavadoBasico.total())
        print('Full:', lavadoFull.total())
        print('Total general:', (Em1.total() + Em2.total() + Em3.total() + Em4.total()))
        print('Porcentaje por tipo de lavado:')
        print('Básico: %', lavadoBasico.contador/contador*100)
        print('Full: %', lavadoFull.contador/contador*100)
        print('Porcentaje por tipo de auto:')
        print('Chico: %', AutoChico.contador/contador*100)
        print('Grande: %', AutoGrande.contador/contador*100)