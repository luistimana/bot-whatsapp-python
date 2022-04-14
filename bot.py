from selenium import webdriver
import time
import os, time

driver = webdriver.Chrome(executable_path=r"C:\Users\luist\AppData\Local\Programs\Python\Python310\Lib\site-packages\webbot\drivers\chrome_windows.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(10)

celular = "51987654321"
mensaje = "Hola, estoy enviando un mensaje desde Python"

driver.get("https://wa.me/" + celular + "/?text=" + mensaje)
time.sleep(5)

btn = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
btn.click()
time.sleep(5)
btn = driver.find_elements_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
btn.click()
time.sleep(30)

#boton enviar                    
btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")[0]
btn.click()
time.sleep(10)
	
print("-- Fin de Bot--")

time.sleep(40)

driver.close()