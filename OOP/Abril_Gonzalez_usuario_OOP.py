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

