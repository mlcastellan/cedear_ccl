#############################################
## funcion para comparar MEP vs cedears    ##
##                                         ##
##									       ##
##                                         ##
#############################################
from scrapper import *

#CEDEAR, CEDEAR_percent, CEDEAR_data 

scrap('https://www.rava.com/empresas/perfil.php?e=CEDEARGOLD')

print(CEDEAR+"-"+CEDEAR_percent+"-"+CEDEAR_data)

#CEDEAR=url_to_text()
MEP =102.22
#CEDEAR_percent =6.00
MEP_percent =-6.00



com_CEDEAR=0.50
com_MEP=0.50
variacion=3
stop_loss=5

#############################
def comparar (CEDEAR,MEP,CEDEAR_percent,MEP_percent,com_CEDEAR,com_MEP,variacion,stop_loss):
	#-------------------------#
		comisiones=com_MEP+com_CEDEAR
		
		if(CEDEAR_percent<-stop_loss):
			print("Hay que vender el CEDEAR")
			return
		if(MEP_percent<-stop_loss):
			print("Hay que vender el MEP/MEP")
			print("¿Es logico vender los usd si bajan en este contexto?")
			return

		variacion=abs(abs(CEDEAR_percent-MEP_percent)-comisiones)

		print(variacion)
		if (variacion>3)&(CEDEAR_percent>MEP_percent):
			print("Hay que vender CEDEAR Y COMPRAR MEP")
			return

		if (variacion>3)&(MEP_percent>CEDEAR_percent):
			print("Hay que vender MEP Y COMPRAR CEDEAR")
			return
#############################
def notfloat(n):
    try:
        float(n)
        return False
    except:
        return True
#############################

#############################
#comparar(CEDEAR,MEP,CEDEAR_percent,MEP_percent,com_CEDEAR,com_MEP,variacion,stop_loss)
#############################
