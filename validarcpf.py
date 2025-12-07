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

# Acessar a página
driver.get("https://analista-teste.seatecnologia.com.br")
print("Site iniciado!")

# Abrir modal
botao = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Adicionar Funcionário')]"))
)
botao.click()
print("Botão clicado!")

print("==== CT05 – Validando CPF inválido ====")

# Preencher nome válido
nome = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='root']/main/div[2]/div[2]/form/div[3]/div/div[1]/input")
    )
)
nome.clear()
nome.send_keys("João Silva")

# Preencher CPF inválido
cpf = driver.find_element(By.NAME, 'cpf')
cpf.clear()
cpf.send_keys("12345678900")  # CPF inválido

# Preencher outros campos
driver.find_element(By.NAME, 'birthDay').send_keys("01011990")
driver.find_element(By.NAME, 'rg').send_keys("1234567")

# Marcar checkbox
checkbox = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//label[contains(@class, 'ant-checkbox-wrapper')]//span[text()='O trabalhador não usa EPI.']/preceding-sibling::span"
    ))
)
checkbox.click()

# Clicar em salvar
salvar = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="root"]/main/div[2]/div[2]/form/button'
    ))
)
salvar.click()

# Validar erro de CPF
try:
    erro = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(), 'CPF') or contains(text(), 'inválido')]")
        )
    )
    print("✔ CT05 aprovado – Sistema bloqueou CPF inválido.")
except:
    print("✘ CT05 reprovado – Sistema ACEITOU CPF inválido.")

driver.quit()
