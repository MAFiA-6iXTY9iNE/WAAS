import termcolor
import colorama
colorama.init()
from termcolor import colored

print("\n")
print(colored(r"""█░█░█ █░█ ▄▀█ ▀█▀ █▀ ▄▀█ █▀█ █▀█   ▄▀█ █░█ ▀█▀ █▀█   █▀ █▀▀ █▄░█ █▀▄ █▀▀ █▀█  
▀▄▀▄▀ █▀█ █▀█ ░█░ ▄█ █▀█ █▀▀ █▀▀   █▀█ █▄█ ░█░ █▄█   ▄█ ██▄ █░▀█ █▄▀ ██▄ █▀▄ """, 'green'))
print("\n")
print(colored("V3.0".center(75,"-"), 'yellow'))
print("\n")
print(colored("© PASINDU THARUSHA - All Rights Reserved. \nThis project is based on open source dependencies built by open source communities.\nThe software is licensed under GPL V3 Licence. \nE-mail : pasindutharushahewage@outlook.com".center(24,"-"), 'green'))
print("\n")

from rich.progress import track
from rich.console import Console
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import pandas

colorama_init()
excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')

count = 0

options = Options()
service = Service()
options.add_argument(r"--user-data-dir=C:\\Users\\5523\\AppData\\Local\\Google\\Chrome\\User Data\\")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://web.whatsapp.com")

input(colored("Press ENTER after login into Whatsapp Web and your chats are visiable.", 'yellow'))
for column in track(excel_data['Contact'].tolist(), description="Sending Messages..."):
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['Contact'][count]) + '&text=' + excel_data['Message'][count]
        sent = False
        # It tries 3 times to send a message in case if there any error occurred
        driver.get(url)
        try:
            click_btn = WebDriverWait(driver, 35).until(
                EC.element_to_be_clickable((By.CLASS_NAME, '_3XKXx')))
        except Exception as e:
            print(f"{Fore.RED}NOPE: {Style.RESET_ALL}" + str(excel_data['Contact'][count]))
            log_file = open('log.txt', 'a')
            log_file.write("NOPE: " + str(excel_data['Contact'][count]) + '\n')
        else:
            sleep(2)
            click_btn.click()
            sent = True
            sleep(5)
            print(f"{Fore.GREEN}SENT: {Style.RESET_ALL}" + str(excel_data['Contact'][count]))
            log_file = open('log.txt', 'a')
            log_file.write('SENT: ' + str(excel_data['Contact'][count]) + '\n')
        count = count + 1
    except Exception as e:
        print(f"{Fore.RED}NOPE: {Style.RESET_ALL}" + str(excel_data['Contact'][count]) + str(e))
        log_file = open('log.txt', 'a')
        log_file.write("NOPE: " + str(excel_data['Contact'][count]) + '\n')
driver.quit()
print("The script executed successfully.")
