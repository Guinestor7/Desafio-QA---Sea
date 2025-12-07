import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Iniciar driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://analista-teste.seatecnologia.com.br")
print("Site iniciado!")

# Abrir modal
botao = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Adicionar Funcionário')]"))
)
botao.click()

print("==== CT06 – Validando RG inválido ====")

# Preencher nome válido
nome = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[3]/div/div[1]/input")
    )
)
nome.clear()
nome.send_keys("João Silva")

# CPF válido
cpf = driver.find_element(By.NAME, 'cpf')
cpf.clear()
cpf.send_keys("12345678901")  # aceita qualquer CPF no layout atual

# RG inválido
rg = driver.find_element(By.NAME, 'rg')
rg.clear()
rg.send_keys("12")  # inválido

# Preencher nascimento
driver.find_element(By.NAME, 'birthDay').send_keys("01011990")

# Marcar checkbox
checkbox = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//label[contains(@class, 'ant-checkbox-wrapper')]//span[text()='O trabalhador não usa EPI.']/preceding-sibling::span"
    ))
)
checkbox.click()

# Botão salvar
salvar = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="root"]/main/div[2]/div[2]/form/button'
    ))
)
salvar.click()

# Validar erro
try:
    erro = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(), 'RG') or contains(text(), 'inválido')]")
        )
    )
    print("✔ CT06 aprovado – Sistema bloqueou RG inválido.")
except:
    print("✘ CT06 reprovado – Sistema ACEITOU RG inválido.")

driver.quit()
