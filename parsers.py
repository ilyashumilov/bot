import urllib.request
import requests as r
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

from xpath import Xpath
class parsers():
    @classmethod
    def ig_parser(self, user):
        url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'

        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
        }

        resp = r.get(url, headers=headers, timeout=10)
        image_url = resp.json()['data']['user']['profile_pic_url']

        # Adding user_agent information
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        # Image URL and Filename
        filename = "pic.jpg"

        # Get resource
        urllib.request.urlretrieve(image_url, filename)

        print(os.listdir())

    @classmethod
    def vk_parser(self,username):
        desired_capabilities = {
            "browserName": "firefox",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=desired_capabilities
        )

        # Заходим на главную страницу
        driver.get('https://vk.com/')

        # Ожидаем появление формы ввода логина

        input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Xpath.number)))
        input_element = driver.find_element(By.XPATH, Xpath.number)
        input_element.clear()
        input_element.send_keys('77774476105')
        print('send number')

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Xpath.number_btn))).click()
        print('clicked the number button')

        input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Xpath.password)))
        input_element = driver.find_element(By.XPATH, Xpath.password)

        input_element.clear()
        input_element.send_keys('YRiKVARF')
        print('send password')

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Xpath.password_btn))).click()
        print('clicked the password button')
        driver.save_screenshot('ss.png')
        print('screenshot taken')
        time.sleep(10)
        driver.save_screenshot('3d.png')

        print('screenshot taken')

        driver.get(f'https://vk.com/{username}')
        print('profile uploaded')
        driver.save_screenshot('3d.png')


        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Xpath.photo)))
        print('photo uploaded')

        item = driver.find_element(By.XPATH, Xpath.photo)


        print(item.get_attribute("src"))

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        # Image URL and Filename
        filename = "pic.jpg"

        # Get resource
        urllib.request.urlretrieve(item.get_attribute("src"), filename)

        print(os.listdir())

    def tg_parser(self,username):
        desired_capabilities = {
            "browserName": "firefox",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=desired_capabilities
        )

        # Заходим на главную страницу
        driver.get('https://web.telegram.org/z/')

        time.sleep(20)
        driver.save_screenshot('tg1.png')
        time.sleep(20)
        driver.save_screenshot('tg2.png')
        time.sleep(20)

        input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Xpath.tg_input)))
        input_element = driver.find_element(By.XPATH, Xpath.tg_input)

        input_element.clear()
        input_element.send_keys(username)
        print('search profile')


        item = driver.find_element(By.XPATH, Xpath.tg_photo)


        print(item.get_attribute("src"))

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        # Image URL and Filename
        filename = "pic.jpg"

        # Get resource
        urllib.request.urlretrieve(item.get_attribute("src"), filename)

        print(os.listdir())