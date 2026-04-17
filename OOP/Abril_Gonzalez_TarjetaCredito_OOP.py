'''
class Usuario:
    empresa= 'empresa tecnologica'
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  
        self.saldo_pagar += monto
        return self
    
    def pagar_tarjeta(self, pago):
        self.pago = pago
        self.saldo_pagar -= pago
        return self
    
    def mostrar_saldo_usuario(self):
        return f'usuario: {self.nombre} {self.apellido} \nsaldo a pagar: ${self.saldo_pagar}'
    
    def transferir_deuda(self, otro_usuario, monto):
        if self.saldo_pagar >= monto:
            self.saldo_pagar -= monto
            otro_usuario.saldo_pagar += monto
        else:
            print(f'{self.nombre} {self.apellido}: no podes transferir mas de lo que debes')


Abril= Usuario('Abril', 'Gonzalez', 'abrilr.gonzalezyrc@gmail.com')
diego= Usuario('Diego', 'Yrcañaupa', 'd88192@gmail.com')
luciana= Usuario('luciana','caceres', 'lu.ch14@gmail.com')

print(f'mi nombre es {Abril.nombre}')
print(f'mail de diego: {diego.email}')

print('--------')
diego.hacer_compra(20000).hacer_compra(5000).pagar_tarjeta(20000)

print(diego.mostrar_saldo_usuario())

print('--------')

Abril.hacer_compra(30800).pagar_tarjeta(10000).pagar_tarjeta(8000)

print(Abril.mostrar_saldo_usuario())

print('--------')

luciana.hacer_compra(70000).hacer_compra(20000).hacer_compra(50000).pagar_tarjeta(10000).pagar_tarjeta(20000).pagar_tarjeta(20000).pagar_tarjeta(30000)

print(luciana.mostrar_saldo_usuario())

print('--------')
Abril.transferir_deuda(diego, 13000)
print(diego.mostrar_saldo_usuario())

'''

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
            
tarjeta_de_abril = TarjetaCredito(0, 100000, 0.02)
tarjeta_de_diego = TarjetaCredito(0, 80000, 0.04)
tarjeta_de_luciana = TarjetaCredito(0, 90000, 0.01)

tarjeta_de_abril.compra(50000).compra(20000).pago(60000).cobrar_interes()

print(tarjeta_de_abril.cobrar_interes())
print(tarjeta_de_abril.mostrar_info_tarjeta())

print('--------')

tarjeta_de_diego.compra(30500).compra(30000).compra(10000).pago(60000).cobrar_interes()

print(tarjeta_de_diego.cobrar_interes())
print(tarjeta_de_diego.mostrar_info_tarjeta())

print('--------')

tarjeta_de_luciana.compra(50000).compra(42000).compra(48000).pago(10000).cobrar_interes()

print(tarjeta_de_diego.cobrar_interes())
print(tarjeta_de_diego.mostrar_info_tarjeta())

print('--------')
TarjetaCredito.mostrar_tarjetas()

