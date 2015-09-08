from tarjeta.py import *

tarj = TarjetaComun(1)
tarjM = TarjetaMedioBoleto(2)

def test_Saldo1():
	assert tarj.Saldo() == tarj.saldo
	assert tarjM.Saldo() == tarjM.saldo

#tarj.RecargaTarjeta(70)
#tarjM.RecargaTarjeta(35)

def test_RecargaTarjeta1():
	assert tarj.RecargaTarjeta(70) == 70
	assert tarj.RecargaTarjeta (196) == 230
	assert tarj.RecargaTarjeta (368) == 460

K1 = Colectivo (1,"Semtur","K")
v122= Colectivo(2,"Semtur","122v")

def test_PagarBoleto1():
	assert tarjM.PagarBoleto(v122,"06/07/2008 04:20") == False
	assert tarj.PagarBoleto(v122,"06/07/2008 04:20") == False
	
