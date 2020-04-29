#############################################
## funcion para comparar CCL vs cedears    ##
##                                         ##
##									       ##
##                                         ##
#############################################
import scrapper
from scrapper import scrap

#CEDEAR, CEDEAR_percent, CEDEAR_data 

scrap('https://www.rava.com/empresas/perfil.php?e=CEDEARGOLD')

print(CEDEAR+"-"+CEDEAR_percent+"-"+CEDEAR_data)

#CEDEAR=url_to_text()
CCL =102.22
#CEDEAR_percent =6.00
CCL_percent =-6.00



com_CEDEAR=0.50
com_CCL=0.50
variacion=3
stop_loss=5

#############################
def comparar (CEDEAR,CCL,CEDEAR_percent,CCL_percent,com_CEDEAR,com_CCL,variacion,stop_loss):
	#-------------------------#
	#if(notfloat(CEDEAR)):
	#	print("error")
	#	return
	#if(notfloat(CCL)):
	#	print("error")
	#	return
	#if(notfloat(CEDEAR_percent)):
	#	print("error")
	#	return
	#if(notfloat(CCL_percent)):
	#	print("error")
	#	return
	#if(notfloat(com_CEDEAR)):
	#	print("error")
	#	return
	#if(notfloat(com_CCL)):
	#	print("error")
	#	return
	#if(notfloat(variacion)):
	#	print("error")
	#	return
	#if(notfloat(stop_loss)):
	#	print("error")
	#	return
	#-------------------------#

		comisiones=com_CCL+com_CEDEAR
		
		if(CEDEAR_percent<-5):
			print("Hay que vender el CEDEAR")
			return
		if(CCL_percent<-5):
			print("Hay que vender el CCL/MEP")
			print("¿Es logico vender los usd si bajan en este contexto?")
			return

		variacion=abs(abs(CEDEAR_percent-CCL_percent)-comisiones)

		print(variacion)
		if (variacion>3)&(CEDEAR_percent>CCL_percent):
			print("Hay que vender CEDEAR Y COMPRAR MEP")
			return

		if (variacion>3)&(CCL_percent>CEDEAR_percent):
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
#comparar(CEDEAR,CCL,CEDEAR_percent,CCL_percent,com_CEDEAR,com_CCL,variacion,stop_loss)
#############################
