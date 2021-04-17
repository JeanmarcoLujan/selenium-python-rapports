import pandas
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


url ='https://intranet.seidor.es/sap/bc/ui2/flp#ZRAPPORTS_ENTRADA-display&/'




def completeRapports():
	informacion = r'C:\Files Lujan\Apps\rapports-bot\rapports.xlsx'
	df = pandas.read_excel(informacion, engine='openpyxl')

	for x in df.index:
		hola = datee_sel = '#application-ZRAPPORTS_ENTRADA-display-component---Master--calendar--Month0-'+df['Date'][x].strftime("%Y%m%d")
		print(hola)



def inicio():
	completeRapports()




inicio()