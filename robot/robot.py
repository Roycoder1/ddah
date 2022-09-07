

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Instabot:
    def __init__(self,us,password1,first_name,last_name,age,date,email,phone,city) -> None:
        service = Service("/Users/benisti/Downloads/chromedriver 2")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://127.0.0.1:8000/")
        sleep(3)
        self.driver.find_element("xpath",'/html/body/div/div/form/p[3]/a').click()
        sleep(2)
        self.driver.find_element('xpath','//input [@name=\"username\"]').send_keys(us)
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"password1\"]').send_keys(password1)
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"password2\"]').send_keys(password1)
        sleep(1)
        self.driver.find_element('xpath','//button [@type="submit"]').click()
        sleep(2)
        self.driver.find_element('xpath','//textarea [@name=\"first_name\"]').send_keys(first_name)
        sleep(1)
        self.driver.find_element('xpath','//textarea [@name=\"last_name\"]').send_keys(last_name)
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"age\"]').send_keys(age)
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"born_date\"]').send_keys(date)
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"email\"]').send_keys(email)
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"phone_number\"]').send_keys(phone)
        sleep(1)
        self.driver.find_element('xpath','//select [@name=\"city\"]').click()
        sleep(1)
        self.driver.find_element('xpath','//option [@value=\"11\"]').click()
        sleep(1)

        self.driver.find_element('xpath','//input [@name=\"countries\"]').send_keys(phone)
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"rock\"]').click()
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"reggae\"]').click()
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"rap\"]').click()
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"classic\"]').click()
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"voice\"]').click()
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"guitar\"]').click()
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"piano\"]').click()
        sleep(1)
        self.driver.find_element('xpath','//button [@type="submit"]').click()
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"username\"]').send_keys(us)
        sleep(1)
        self.driver.find_element('xpath','//input [@name=\"password\"]').send_keys(password1)
        sleep(1)
        self.driver.find_element('xpath','//button [@type="submit"]').click()
        sleep(1)
        


        



Instabot("Gaton23","Qwerty123", 'Gaston','Kornfield',25,'04/07/1997','gaston23@gmail.com','0543234867', 'Tel-Aviv')