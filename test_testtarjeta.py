from datetime import datetime
#from tarjeta import *

class Colectivo:

	def __init__ (self, interno, empresa, linea):
		self.interno = interno
		self.empresa = empresa
		self.linea = linea

class Viaje:

	def __init__ (self, colectivo="NULL", horario="01/01/0001 0:00", monto=0):
		self.colectivo = colectivo
		self.horario = datetime.strptime(horario , "%d/%m/%Y %H:%M")
		self.monto = monto

class Tarjeta:

	def __init__(self, serie):
		self.serie = serie
		self.saldo = 0
		self.trasbordo = 0
		self.Viaje = [ x for x in range(0,6) ]
		for p in range(0,6):
		    self.Viaje[p]= Viaje();

	def Saldo (self):
		print ("Su saldo es: " + str(self.saldo))
		return self.saldo

	def RecargaTarjeta (self, monto):
		if (monto == 196):
			self.saldo = self.saldo + 230
			return 230
		else:
			if (monto ==  368):
				self.saldo = self.saldo + 460
				return 460
			else:
				self.saldo = self.saldo + monto
				return monto

	def ViajesRealizados (self):
		for i in range (0,5):
			if (self.Viaje[i].colectivo!="NULL" and self.Viaje[i].horario!="01/01/0001 0:00" and self.Viaje[i].monto!=0):
				print (" ")
				print ("Fecha: " + str(self.Viaje[i].horario))
				print ("Linea: " + str(self.Viaje[i].colectivo.linea) + " Interno: " + str(self.Viaje[i].colectivo.interno))
				print("Monto: " + str(self.Viaje[i].monto))
			else:
				print(" ")
				print("NULL")

class TarjetaComun (Tarjeta):


	def PagarBoleto (self, bondi, horario1):
		horario = datetime.strptime(horario1,"%d/%m/%Y %H:%M")
		delta=(horario - self.Viaje[0].horario)
		if (delta.seconds <= 3600 and self.Viaje[0].colectivo.interno != bondi.interno  and self.trasbordo == 0):
			if (self.saldo > 1.90):
				for i in range (0,5):
					self.Viaje[5-i].colectivo = self.Viaje[4-i].colectivo
					self.Viaje[5-i].horario = self.Viaje[4-i].horario
					self.Viaje[5-i].monto = self.Viaje[4-i].monto
				self.saldo = self.saldo - 1.90
				self.Viaje[0].colectivo = bondi
				self.Viaje[0].horario = horario
				self.Viaje[0].monto = 1.90
				print ("Abona Trasbordo")
				self.trasbordo = 1
				return True
			else:
			    print ("Saldo Insuficiente")
			    return False

		else:
			if (self.saldo > 5.75):
				for i in range(0,5):
					self.Viaje[5-i].colectivo = self.Viaje[4-i].colectivo
					self.Viaje[5-i].horario = self.Viaje[4-i].horario
					self.Viaje[5-i].monto = self.Viaje[4-i].monto
				self.saldo = self.saldo - 5.75
				self.Viaje[0].colectivo = bondi
				self.Viaje[0].horario = horario
				self.Viaje[0].monto = 5.75
				print ("Abona Boleto Normal")
				self.trasbordo = 0
				return True
			else:
			    print ("Saldo Insuficiente")
			    return False


class TarjetaMedioBoleto (Tarjeta):


	def PagarBoleto (self, bondi, horario1):
		horario=datetime.strptime(horario1,"%d/%m/%Y %H:%M")
		delta=horario - self.Viaje[0].horario
		if (horario.hour > 5):
			if ( delta.seconds <= 3600 and self.Viaje[0].colectivo.interno != bondi.interno and self.trasbordo == 0):
				if (self.saldo > 0.96):
					for i in range (0,5):
						self.Viaje[5-i].colectivo = self.Viaje[4-i].colectivo
						self.Viaje[5-i].horario = self.Viaje[4-i].horario
						self.Viaje[5-i].monto = self.Viaje[4-i].monto
					self.saldo = self.saldo - 0.96
					self.Viaje[0].colectivo = bondi
					self.Viaje[0].horario = horario
					self.Viaje[0].monto = 0.96
					print ("Abona Medio Trasbordo")
					self.trasbordo = 1
					return True
				else:
				    print ("Saldo Insuficiente")
				    return False

			else:
				if (self.saldo > 2.90):
					for i in range (0,5):
						self.Viaje[5-i].colectivo = self.Viaje[4-i].colectivo
						self.Viaje[5-i].horario = self.Viaje[4-i].horario
						self.Viaje[5-i].monto = self.Viaje[4-i].monto
					self.saldo = self.saldo - 2.90
					self.Viaje[0].colectivo = bondi
					self.Viaje[0].horario = horario
					self.Viaje[0].monto = 2.90
					print ("Abona Medio Boleto")
					self.trasbordo = 0
					return True
				else:
				    print ("Saldo Insuficiente")
				    return False
		else:
			if (delta.seconds <= 3600 and self.Viaje[0].colectivo.interno != bondi.interno  and self.trasbordo == 0):
				if (self.saldo > 1.90):
					for i in range (0,5):
						self.Viaje[5-i].colectivo = self.Viaje[4-i].colectivo
						self.Viaje[5-i].horario = self.Viaje[4-i].horario
						self.Viaje[5-i].monto = self.Viaje[4-i].monto
					self.saldo = self.saldo - 1.90
					self.Viaje[0].colectivo = bondi
					self.Viaje[0].horario = horario
					self.Viaje[0].monto = 1.90
					print ("Abona Trasbordo")
					self.trasbordo = 1
					return True
				else:
				    print ("Saldo Insuficiente")
				    return False

			else:
				if (self.saldo > 5.75):
					for i in range (0,5):
						self.Viaje[5-i].colectivo = self.Viaje[4-i].colectivo
						self.Viaje[5-i].horario = self.Viaje[4-i].horario
						self.Viaje[5-i].monto = self.Viaje[4-i].monto
					self.saldo = self.saldo - 5.75
					self.Viaje[0].colectivo = bondi
					self.Viaje[0].horario = horario
					self.Viaje[0].monto = 5.75
					print ("Abona Boleto Normal")
					self.trasbordo = 0
					return True
				else:
				    print ("Saldo Insuficiente")
				    return False

tarj = TarjetaComun(1)
tarjM = TarjetaMedioBoleto(2)

def test_Saldo1():
	assert tarj.Saldo() == 0
    assert tarjM.Saldo() == 0

tarj.RecargaTarjeta(70)
tarjM.RecargaTarjeta(35)
def test_RecargaTarjeta1():
	assert tarj.Saldo() == 70
	assert tarjM.Saldo() == 35
	assert RecargaTarjeta(70) == 70
	assert RecargaTarjeta (196) == 230
	assert RecargaTarjeta (368) == 460


lak = Colectivo (1,"semtur", "K")
un122 = Colectivo (2, "semtur", "122v")

tarj.PagarBoleto (un122, "15/10/2014 21:00") #Normal
tarj.Saldo()
tarj.PagarBoleto (lak, "15/10/2014 22:00") #Trasbordo
tarj.Saldo()
tarj.PagarBoleto (un122, "15/10/2014 22:15") #Normal
tarj.Saldo()
tarj.PagarBoleto (lak, "15/10/2014 22:55") #Trasbordo
tarj.Saldo()
tarj.PagarBoleto (lak, "15/10/2014 22:56") #Normal
tarj.Saldo()

tarj.ViajesRealizados()
