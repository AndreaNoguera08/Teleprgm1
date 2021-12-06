class Cuentas (ABC):
    TipoDeCuenta = ""
    __saldo = 0
    
    def __init__ (self,tipoDeCuenta):
        self.TipoDeCuenta = TipoDeCuenta
        #self.setsaldo(saldo)

        def getsaldo(self):
            resultado = self.__saldo
            return resultado

         def setsaldo(self, saldo):
            self.__saldo = self.__saldo + saldo
        def consultarS(self):
           print("Su saldo es: ",self.getSaldo)

        def depositar(self, monto):
        if monto > 0:
          self.setSaldo(monto) 

        def retirar(self,monto):
        if monto < 0:
          self.setSaldo(monto)

        
        def abonarIntereses(self):
         pass


class Ahorro (Cuentas):

class PlazoFijo (Cuentas):

    __SaldoPlazoF = 0
    Tiempo = 0
    tasa =0.1
    
  def _init_ (self, t):
    self.tiempo = t
  def getSaldoPlazo(self):
      return self.__SaldoPlazoF

  def setSaldoPlazo(self,saldo):
      self.__SaldoPlazpF =saldo

  def AbonarIntereses (self):
    interes = super().getSaldo* self.tasa * self.Tiempo
    self.setSaldoPlazoF(super().getSaldo + interes)


    MiCuenta = Cuentas()
    MiCuenta.setSaldo(4000)
    MiCuenta.getSaldo()
    print (MiCuenta.getSaldo)
   
   

        


    
    
    
        
    
       
       

