from tarjeta.py import *

tarj = TarjetaComun(1)
tarj.RecargaTarjeta(70)

def test_saldo():
  assert tarj.Saldo() = 70
    
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


