
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

# Configurações do Chrome no MacIntel
options = Options()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Baixa o driver correto (NÃO usa .exe no Mac)
chromedriver_path = ChromeDriverManager().install()

# Cria o serviço apontando para o driver correto
service = ChromeService(chromedriver_path)

# Inicia o site
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://analista-teste.seatecnologia.com.br")

print("Site iniciado com sucesso!")

wait = WebDriverWait(driver, 10)

botao = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Adicionar Funcionário')]"))
)

time.sleep(1)  # só pra você ver ele apertar
botao.click()

print("Botao de adicionar funcionario clicado com sucesso!")


#preenchendo formulario de cadastro 

username = 'Guilherme Teste'
cpf = '12345678900'
birthDay = '07062005'
rg = '3566543'
driver.find_element(By.NAME, 'name').send_keys(username)
driver.find_element(By.NAME, 'cpf').send_keys(cpf)
driver.find_element(By.NAME, 'birthDay').send_keys(birthDay)
driver.find_element(By.NAME, 'rg').send_keys(rg)

print("Dados preenchidos com sucesso!")

checkbox = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//label[contains(@class, 'ant-checkbox-wrapper')]//span[text()='O trabalhador não usa EPI.']/preceding-sibling::span"
    ))
)

checkbox.click()
print("Checkbox marcada!")

salvar = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="root"]/main/div[2]/div[2]/form/button'
    ))
)

salvar.click()
print("Funcionario criado com sucesso!")



time.sleep(15)
