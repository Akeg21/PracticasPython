class  Cajero:
	def __init__ (self, saldo=1500):
		self.saldo = saldo

	def saldo(self):
		return self.saldo

	def consultar(self):
		print "Su saldo actual es: ", self.saldo

	def depositar(self):
		dep = input("Ingresa la cantidad que deseas depositar: ")
		self.saldo+=dep 
		print "Deposito Exitoso! \nSu saldo actual  es de: ",self.saldo
	def retirar(self):
		ret = input("Ingresa la cantidad que deseas retirar: ")
		if ret>self.saldo:
			print "Saldo Insuficiente"
		else:
			self.saldo-=ret
			print "Retiro Exitoso! \nSu saldo actual es de: ",self.saldo

obj= Cajero()
obj.consultar()
obj.depositar()
obj.retirar()
