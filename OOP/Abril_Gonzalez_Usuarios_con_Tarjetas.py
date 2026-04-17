class TarjetaCredito:

    todas_las_tarjetas = []

    def __init__(self, saldo_pagar, limite_credito, intereses):
        self.saldo_pagar = saldo_pagar
        self.limite_credito= limite_credito
        self.intereses= intereses
        TarjetaCredito.todas_las_tarjetas.append(self)

    def compra(self, monto):
        if (self.saldo_pagar + monto) <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print('Tarjeta Rechazada, has alcanzado tu límite de crédito')
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        return (f'saldo a pagar: {self.saldo_pagar}')

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self.saldo_pagar
    
    @classmethod
    def mostrar_tarjetas(cls):
        for i in cls.todas_las_tarjetas:
            print(i.mostrar_info_tarjeta())
            

class Usuario:
    empresa= 'tecnolgia'
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta= TarjetaCredito(0, 100000, 0.2)
        self.tarjetas= []

    def agregar_tarjeta(self, saldo=0, limite_credito=100000, intereses=0.2):
        nueva_tarjeta= TarjetaCredito(saldo, limite_credito, intereses)
        self.tarjetas.append(nueva_tarjeta)
        return self

    def hacer_compra(self, monto, i):  
        self.tarjetas[i-1].compra(monto)
        return self
    
    def pagar_tarjeta(self, pago, i):
        self.tarjetas[i-1].pago(pago)
        return self
    
    def mostrar_saldo_usuario(self, i):
        return f'USUARIO: {self.nombre} {self.apellido} \nsaldo a pagar en tarjeta {i}: ${self.tarjetas[i-1].saldo_pagar}'
    
    def transferir_deuda(self, otro_usuario, monto, i_origen, i_destino):
        if self.tarjetas[i_origen-1].saldo_pagar >= monto:
            self.tarjetas[i_origen-1].pago(monto)
            otro_usuario.tarjetas[i_destino-1].compra(monto)
        else:
            print(f'ADVERTENCIA: {self.nombre} {self.apellido} no podes transferir mas de lo que debes')

Usuario1= Usuario('Abril', 'Gonzalez', 'abrilr.gonzalezyrc@gmail.com')
Usuario2= Usuario('Diego', 'Yrcañaupa', 'd88192@gmail.com')
Usuario3= Usuario('luciana','Caceres', 'lu.ch14@gmail.com')

#----------------------------------------------

Usuario1.agregar_tarjeta().agregar_tarjeta()

Usuario2.agregar_tarjeta().agregar_tarjeta()

Usuario3.agregar_tarjeta()

#----------------------------------------------

Usuario1.hacer_compra(70500, 1).hacer_compra(30000, 2).pagar_tarjeta(40000, 1)
print(Usuario1.mostrar_saldo_usuario(1))
print(Usuario1.mostrar_saldo_usuario(2))

print('----------------')

Usuario2.hacer_compra(50000, 2).pagar_tarjeta(10000, 2).transferir_deuda(Usuario1, 80000, 2, 1)
print(Usuario2.mostrar_saldo_usuario(1))
print(Usuario2.mostrar_saldo_usuario(2))

print('----------------')

Usuario3.hacer_compra(80000, 1).transferir_deuda(Usuario2, 60000, 1, 1)
print(Usuario3.mostrar_saldo_usuario(1))
print(Usuario2.mostrar_saldo_usuario(1))

