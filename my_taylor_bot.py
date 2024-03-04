import requests
import time
import telebot
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

API_KEY = '6559610608:AAEqQMnupll5hw2mBB414MonJAZElEq0roQ'
bot = telebot.TeleBot(API_KEY)

def check_page():
	chrome_options = Options()
	# chrome_options.add_argument("--disable-extensions")
	# chrome_options.add_argument("--disable-gpu")
	chrome_options.add_argument("--no-sandbox") # linux only
	chrome_options.add_argument("--headless=new") # for Chrome >= 109
	# chrome_options.add_argument("--headless")
	# chrome_options.headless = True # also works
	driver = webdriver.Chrome(options=chrome_options)

	url = "https://www.allaccess.com.ar/event/taylor-swift-the-eras-tour"

	driver.get(url)

	# Wait for potential JavaScript-based redirections
	driver.implicitly_wait(30)  # wait 10 seconds

	print("Final destination:")
	print(driver.current_url)
	new_url = driver.current_url
	print(driver.current_url == url)

	driver.quit()
	return new_url != url

def get_chat_ids():
    with open('chat_ids.txt', 'r') as f:
        chat_ids = [int(line.strip()) for line in f]
    return chat_ids


def send_notification():
    message = '¡La página ha cambiado y las entradas ya no están agotadas!'
    ids = get_chat_ids()
    print(ids)
    for id in ids:
    	bot.send_message(id, message)
    	


def main():
    #bot.polling()
    send_notification()
    while True:
        if check_page():
            send_notification()
            while check_page():
                time.sleep(600)
        time.sleep(60)  # Espera un minuto antes de volver a comprobar


if __name__ == '__main__':
    main()
