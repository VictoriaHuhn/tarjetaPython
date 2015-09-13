from tarjeta import *

def test_Saldo():
	#Probamos la función Saldo().
	tarj = TarjetaComun(1)
	tarjM = TarjetaMedioBoleto(2)
	assert tarj.Saldo() == tarj.saldo
	assert tarjM.Saldo() == tarjM.saldo
	assert tarj.saldo == 0
	assert tarjM.saldo == 0


def test_RecargaTarjeta1():
	#Probamos el return de la función RecargaTarjeta().
	tarj = TarjetaComun(1)
	tarjM = TarjetaMedioBoleto(2)
	assert tarj.RecargaTarjeta(70) == 70
	assert tarj.RecargaTarjeta (196) == 230
	assert tarj.RecargaTarjeta (368) == 460
	
def test_RecargaTarjeta2():
	#Probamos la función Saldo() luego de implementar la RecargaTarjeta().
	tarj = TarjetaComun(1)
	tarjM = TarjetaMedioBoleto(2)
	tarj.RecargaTarjeta(70)
	tarjM.RecargaTarjeta(35)
	assert tarj.saldo == 70
	assert tarjM.saldo == 35


def test_PagarBoletoSinSaldo():
	#Probamos la función  PagarBoleto() con tarjetas sin saldo.
	K1 = Colectivo (1,"Semtur","K")
	v122= Colectivo(2,"Semtur","122v")
	tarj = TarjetaComun(1)
	tarjM = TarjetaMedioBoleto(2)
	assert tarjM.PagarBoleto(v122,"06/07/2008 04:20") == False
	assert tarj.PagarBoleto(v122,"06/07/2008 04:20") == False
	
def test_PagarBoleto():
	#Probamos la función PagarBoleto() para tarjetas cargadas.
	K1 = Colectivo (1,"Semtur","K")
	v122= Colectivo(2,"Semtur","122v")
	tarj = TarjetaComun(1)
	tarjM = TarjetaMedioBoleto(2)
	tarj.RecargaTarjeta(5.75)
	tarjM.RecargaTarjeta(2.90)
	assert tarjM.PagarBoleto(v122,"06/07/2008 04:20") == False #El medio boleto no funciona de 0 a 6 hs.
	assert tarj.PagarBoleto(v122,"06/07/2008 04:20") == True
	assert tarjM.PagarBoleto(K1,"06/07/2008 06:20") == True
	assert tarjM.Saldo() == 0
	assert tarj.Saldo() == 0

def test_Tranbordo():
	#Probamos la implementación de los transbordos.
	K1 = Colectivo (1,"Semtur","K")
	v122= Colectivo(2,"Semtur","122v")
	tarj = TarjetaComun(1)
	tarjM = TarjetaMedioBoleto(2)
	#Cargamos la tarjeta normal con lo justo para un boleto normal y dos transbordos.
	tarj.RecargaTarjeta(5.75+1.90+1.90)
	#Cargamos la tarjeta de medio boleto con lo justo para un medio boleto y un medio transbordo.
	tarjM.RecargaTarjeta(2.90+0.96)
	#Pagamos 3 viajes con la tarjeta normal, con 20 mins de diferencia entre c/u, en distintos colectivos.
	assert tarj.PagarBoleto(v122,"06/07/2008 06:20") == True
	assert tarj.PagarBoleto(K1,"06/07/2008 06:40") == True
	assert tarj.PagarBoleto(v122,"06/07/2008 07:00") == False
	#Pagamos 2 viajes con la tarjeta de medio boleto, en las mismas condiciones que antes.
	assert tarjM.PagarBoleto(K1,"06/07/2008 06:20") == True
	assert tarjM.PagarBoleto(v122,"06/07/2008 06:40") == True
	assert tarjM.Saldo() == 0
	assert round(tarj.Saldo()) == round(1.90)
	
def test_ViajesRealizados():
	#Probamos si la función pagar boleto guarda correctamente los viajes realizados. 
	K1 = Colectivo (1,"Semtur","K")
	v122= Colectivo(2,"Semtur","122v")
	tarj = TarjetaComun(1)
	tarjM = TarjetaMedioBoleto(2)
	#Cargamos las 2 tarjetas con lo justo para 4 viajes
	tarj.RecargaTarjeta(5.75*2+1.90*2)
	tarjM.RecargaTarjeta(2.90*2+0.96*2)
	tarj.PagarBoleto(v122,"06/07/2008 06:20")
	tarj.PagarBoleto(K1,"06/07/2008 06:40")
	tarj.PagarBoleto(v122,"06/07/2008 07:00")
	tarj.PagarBoleto(K1,"06/07/2008 7:20")
	tarjM.PagarBoleto(v122,"06/07/2008 06:20")
	tarjM.PagarBoleto(K1,"06/07/2008 06:40")
	tarjM.PagarBoleto(v122,"06/07/2008 07:00")
	tarjM.PagarBoleto(K1,"06/07/2008 7:20")
	assert round(tarj.Saldo()) == 0
	assert round(tarjM.Saldo()) == 0
	#Creamos listas independientes que tengan los mismos viajes.
	Lista=[x for x in range(0,6)]
	Lista[0]=Viaje(K1,"06/07/2008 7:20", 5.75)
	Lista[1]=Viaje(v122,"06/07/2008 7:00", 1.90)
	Lista[2]=Viaje(K1,"06/07/2008 6:40", 5.75)
	Lista[3]=Viaje(v122,"06/07/2008 6:20", 1.90)
	Lista[4]=Viaje()
	Lista[5]=Viaje()
	ListaM=[x for x in range(0,6)]
	ListaM[0]=Viaje(K1,"06/07/2008 7:20", 2.90)
	ListaM[1]=Viaje(v122,"06/07/2008 7:00", 0.96)
	ListaM[2]=Viaje(K1,"06/07/2008 6:40", 2.90)
	ListaM[3]=Viaje(v122,"06/07/2008 6:20", 0.96)
	ListaM[4]=Viaje()
	ListaM[5]=Viaje()
	#Comparamos con el retorno de las funciones
	assert tarj.ViajesRealizados() == Lista


	
