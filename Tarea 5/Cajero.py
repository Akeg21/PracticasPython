import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
class Cajero:
    saldo = 0
		
    def __init__(self):
        self.saldo = 1500
		
	def consultar(self): 
   		 print "Su saldo actual es de: $", self.saldo
		
	def depositar(self,deposito):
		 self.saldo = self.saldo + deposito
		 print "Deposito Exitoso! \nSu saldo actual es de: $", self.saldo
        
    def retirar(self,retiro):
         if retiro < self.saldo:
             self.saldo = self.saldo - retiro
             print "Retiro Exitoso! \nSu saldo actual es de: $", self.saldo
         else:
             print "Lo sentimos no se puede realizar la operacion, Saldo Insuficente. \nSu saldo actual es de: $", self.saldo
		
    def menu(self):
		 opc = input("Selecciona una opcion: \n1)Consultar \n2)Depositar \n3)Depositar \n")

		 if opc == 1:
			 self.consultar()
        	 else:
		 	if opc == 2:
		    	 dep = input("Ingrese la cantidad que desea depositar: ")
                 self.depositar(dep)
          #else:
           # if opc == 3:
            #    	  ret = input("Ingrese la cantidad que desea retirar: ")
             #    	  self.retirar(ret)
				#      else:
                #		 print "Opcion Invalida"
var = raw_input()
obj = Cajero()
obj.menu()
obj.consultar()
obj.depositar()
obj.retirar()
