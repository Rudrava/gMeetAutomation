from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


mail_address = ''
password = ''

ENTER_MAIL = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
ENTER_PASSWD = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
NEXT = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
LOGIN = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]'
BLIND = '/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div'
MUTE = '/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div'
JOIN_NOW = '/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]'
SHARE_PROMPT = '/html/body/div[1]/div[3]/div/div[2]/div[2]/div[3]/div'
MEETING_ID = ""


chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--disable-notifications")

CHROME_DRIVER = "./chromedriver.exe"
driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=chrome_options)

url = 'https://www.google.com/accounts/Login?hl=en&continue=http://www.google.co.in/'
driver.get(url)

sleep(5)

WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
    (By.XPATH, ENTER_MAIL))).send_keys(mail_address)

mail = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, NEXT))).click()
print(mail)

WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
    (By.XPATH, ENTER_PASSWD))).send_keys(password)

WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, LOGIN))).click()


sleep(5)
driver.get("https://meet.google.com/new")


mute = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.XPATH, MUTE))).click()
# driver.find_element_by_xpath(MUTE).click()
print(mute)
print('Deafned the bitch ! ! !')

blind = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, BLIND))).click()
# driver.find_element_by_xpath(BLIND).click()
print(blind)
print("Made Google BLIND ! ! !")

MEETING_ID = driver.current_url

joinNow = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, JOIN_NOW))).click()
# driver.find_element_by_xpath(JOIN_NOW).click()
print(joinNow)
print(f"DID U JOIN to {MEETING_ID}???")

sharePrompt = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, SHARE_PROMPT))).click()
# driver.find_element_by_xpath(SHARE_PROMT).click()
print(sharePrompt)
print("Removed irritation")
