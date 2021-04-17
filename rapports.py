import pandas
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


url ='https://intranet.seidor.es/sap/bc/ui2/flp#ZRAPPORTS_ENTRADA-display&/'




def completeRapports(driver):
	informacion = r'C:\Files Lujan\Apps\rapports-bot\rapports.xlsx'
	df = pandas.read_excel(informacion, engine='openpyxl')

	add_btn = '#__button1'
	project_text = '#application-ZRAPPORTS_ENTRADA-display-component---Detail--proyecto-inner'
	description_text = '#application-ZRAPPORTS_ENTRADA-display-component---Detail--descr-inner'
	situation_cmb = '#application-ZRAPPORTS_ENTRADA-display-component---Detail--situacion'
	situacion_sel = '#__item3-application-ZRAPPORTS_ENTRADA-display-component---Detail--situacion-2'
	hours_text = '#application-ZRAPPORTS_ENTRADA-display-component---Detail--hora-inner'
	save_btn = '#application-ZRAPPORTS_ENTRADA-display-component---Detail--buttonSaveEntrada'

	for x in df.index:
		datee_sel = '#application-ZRAPPORTS_ENTRADA-display-component---Master--calendar--Month0-'+df['Date'][x].strftime("%Y%m%d")

		driver.find_element_by_css_selector(datee_sel).click()
		time.sleep(3)
		driver.find_element_by_css_selector(add_btn).click()
		time.sleep(2)
		driver.find_element_by_css_selector(project_text).send_keys(df['Project'][x])
		time.sleep(2)
		driver.find_element_by_css_selector(description_text).send_keys(df['Description'][x])
		time.sleep(1)
		driver.find_element_by_css_selector(situation_cmb).click()
		driver.find_element_by_css_selector(situacion_sel).click()
		time.sleep(2
		driver.find_element_by_css_selector(hours_text).send_keys(str(df['Hours'][x]))
		time.sleep(3)
		driver.find_element_by_css_selector(save_btn).click()

		time.sleep(5)



def inicio():
	user_text = '#USERNAME_FIELD-inner'
	pasw_text = '#PASSWORD_FIELD-inner'
	longin_btn = '#LOGIN_LINK'

	driver = webdriver.Chrome('./chromedriver.exe')
	driver.maximize_window()
	driver.get(url)


	#LOGIN
	driver.find_element_by_css_selector(user_text).send_keys('P_ALUJAN')
	driver.find_element_by_css_selector(pasw_text).send_keys('************')
	driver.find_element_by_css_selector(longin_btn).click()

	time.sleep(30)
	
	completeRapports(driver)




inicio()