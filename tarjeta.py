from datetime import datetime

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
		else:
			if (monto ==  368):
				self.saldo = self.saldo + 460
			else:
				self.saldo = self.saldo + monto

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
