from abc import ABC, abstractmethod

class metododepago(ABC):
    def __init__(self, envio, retiro, saldo):
        self.envio = envio
        self.retiro = retiro
        self.saldo = saldo
        
    @abstractmethod
    def mostrar_informacion(self):
        pass

class metododepagoNequi(metododepago):
    def __init__(self, envio, retiro, saldo, recargas):
        super().__init__(envio, retiro, saldo) 
        self.recargas = recargas

    def mostrar_informacion(self):
        return f"saldo: {self.saldo},envio: {self.envio}, retiro: {self.retiro},recargas en nequi: {self.recargas}"

class metododepagoDaviplata(metododepago):
    def mostrar_informacion(self):
        return f"saldo: {self.saldo},envio: {self.envio}, retiro: {self.retiro},"

class metododepagoPSE(metododepago):
    def mostrar_informacion(self):
        return f"saldo: {self.saldo},envio: {self.envio}, retiro: {self.retiro}, "

class metododepagoTarjetadecredito(metododepago):
    def mostrar_informacion(self):
        return f"saldo: {self.saldo} ,envio: {self.envio}, retiro: {self.retiro},"

class metododepagoTarjetadebito(metododepago):
    def mostrar_informacion(self):
        return f"saldo: {self.saldo},envio: {self.envio}, retiro: {self.retiro}, "

Nequi = metododepagoNequi("$300.000", "$ 50.000", "$150.000", "paquete de 3.000")
Daviplata = metododepagoDaviplata("$800.000", "$ 500.000", "$300.000")
PSE=metododepagoPSE("$1.000.000", "$ 700.000", "$500.000")
Tarjetadecredito=metododepagoTarjetadecredito("$2.000.000", "$ 1,400.000", "$100.000")
Tarjetadebito=metododepagoTarjetadebito("$3.000.000", "$ 2,400.000", "$200.000")
print(Nequi.mostrar_informacion())
print(Daviplata.mostrar_informacion())
print(PSE.mostrar_informacion())
print(Tarjetadecredito.mostrar_informacion())
print(Tarjetadebito.mostrar_informacion())
