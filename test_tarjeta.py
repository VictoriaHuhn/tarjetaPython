from tarjeta.py import *

tarj = TarjetaComun(1)

def test_Saldo1():
	assert tarj.Saldo() == 0

def test_RecargaTarjeta1():
	assert tarj.Saldo() == 70

	assert RecargaTarjeta(70) == 70
	assert RecargaTarjeta (196) == 230
	assert RecargaTarjeta (2)

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


