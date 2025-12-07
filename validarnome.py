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

# Acessar a página
driver.get("https://analista-teste.seatecnologia.com.br")

print("Site iniciado com sucesso!")

wait = WebDriverWait(driver, 10)

# Abrir modal de novo funcionário
botao = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Adicionar Funcionário')]"))
)
time.sleep(1)
botao.click()
print("Botão de adicionar funcionário clicado com sucesso!")

print("==== CT04 – Validando NOME inválido ====")

# Campo nome
nome = wait.until(
    EC.visibility_of_element_located((
        By.XPATH,
        "//*[@id='root']/main/div[2]/div[2]/form/div[3]/div/div[1]/input"
    ))
)

# Limpa se necessário
nome.clear()
time.sleep(0.5)

# Digita nome inválido
nome.send_keys("João@123")

# Preencher restante do formulário
driver.find_element(By.NAME, 'cpf').send_keys("12345678900")
driver.find_element(By.NAME, 'birthDay').send_keys("01011990")
driver.find_element(By.NAME, 'rg').send_keys("3566543")
print("Dados preenchidos com sucesso!")

# Checkbox
checkbox = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//label[contains(@class, 'ant-checkbox-wrapper')]"
        "//span[text()='O trabalhador não usa EPI.']/preceding-sibling::span"
    ))
)
checkbox.click()
print("Checkbox marcada!")

# Botão salvar
salvar = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="root"]/main/div[2]/div[2]/form/button'
    ))
)
salvar.click()

# Esperar visualmente
time.sleep(2)

# Validar erro real do nome (normalmente aparece um texto embaixo do input)
try:
    erro = wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class,'ant-form-item-explain-error')]"
        ))
    )
    print("✔ CT04 aprovado – Mensagem de nome inválido exibida!")
except:
    print("✘ CT04 reprovado – O sistema ACEITOU nome inválido!")

time.sleep(2)
driver.quit()