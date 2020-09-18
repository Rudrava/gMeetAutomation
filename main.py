from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import creds

mail_address, password = creds.getCreds()
print(mail_address, password)


ENTER_MAIL = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
ENTER_PASSWD = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
NEXT = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
LOGIN = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]'

MUTE = '/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div/div/div'
BLIND = '/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div[2]/div/div/div[1]/div/div[4]/div[2]/div/div'


JOIN_NOW = '//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span'
SHARE_PROMPT = '/html/body/div[1]/div[3]/div/div[2]/div[2]/div[3]/div'
NAME = "/html/body/div[1]/div[3]/div/div[2]/span/div/text()"
MEETING_ID = ""
   

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--disable-notifications")

CHROME_DRIVER = "./chromedriver.exe"
driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=chrome_options)

url = 'https://www.google.com/accounts/Login?hl=en&continue=https://meet.google.com/new'
driver.get(url)

sleep(5)

WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
    (By.XPATH, ENTER_MAIL))).send_keys(mail_address)

WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, NEXT))).click()


WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
    (By.XPATH, ENTER_PASSWD))).send_keys(password)

WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, LOGIN))).click()


sleep(5)
# driver.get("https://meet.google.com/new")


WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.XPATH, MUTE))).click()
print('Deafned the bitch ! ! !')

WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, BLIND))).click()
print("Made Google BLIND ! ! !")

MEETING_ID = driver.current_url

joinNow = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, JOIN_NOW))).click()
print(joinNow)
print(f"DID U JOIN to {MEETING_ID}???")

sharePrompt = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, SHARE_PROMPT))).click()
print(sharePrompt)
print("Removed irritation")

ADMIT = '/html/body/div[1]/div[3]/div/div[2]/div[3]/div[3]/span/span'


while True:
    # print('checking')
    sleep(1)
    x = 100
    try:
        connectingParticipant = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span').text
        print(connectingParticipant.strip("'"), " has joined the meeting")
        WebDriverWait(driver, x).until(
            EC.element_to_be_clickable((By.XPATH, ADMIT))).click()
    except:
        print('Listening . . .')

    finally:
        pass

