from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pygetwindow as gw

# Chiedi all'utente il nome utente e la password
nome_utente = 'S9456017O'
password = 'zf36249s'

# Percorso al ChromeDriver su Windows
path_to_chromedriver = 'C:\\ChromeDriver\\chromedriver.exe'  # Assicurati che il percorso sia corret

# Configura il browser
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Esegui il browser in modalità headless (opzionale)
driver = webdriver.Chrome(executable_path=path_to_chromedriver, options=options)


# Apri la pagina di login
driver.get('https://web.spaggiari.eu/home/app/default/login.php')

# Trova il campo Codice Personale / Email e inserisci il nome utente
user_field = driver.find_element(By.ID, 'login')  # Usa l'ID corretto del campo
user_field.send_keys(nome_utente)

# Trova il campo Password e inserisci la password
password_field = driver.find_element(By.ID, 'password')  # Usa l'ID corretto del campo
password_field.send_keys(password)

# Premi il pulsante di login
login_button = driver.find_element(By.NAME, 'Submit')  # Usa il nome o il selettore corretto del pulsante
login_button.click()

# Attendi un po' di tempo per permettere alla pagina di caricarsi
time.sleep(5)

# Fai qualcosa dopo il login, ad esempio stampare il titolo della pagina
print(driver.title)

# Porta la finestra di Chrome in primo piano
chrome_window = gw.getWindowsWithTitle('Chrome')[0]  # Potrebbe essere necessario adattare il titolo della finestra
chrome_window.activate()


