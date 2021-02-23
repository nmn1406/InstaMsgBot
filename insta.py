from selenium import webdriver
from time import sleep
from secrets import pw



class InstaBot:
    def __init__(self, username, pw):
        i= int(input("Enter number of times you want to Send Messages:"))
        
        self.driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
     
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(6)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/direct/inbox/')]")\
        .click()
        sleep(3)
        self.driver.find_element_by_xpath("//div[contains(text(), 'namanagarwal_')]").click()
        sleep(2)
        text="Test Messages"
        for x in range(1,i):
        	print (x,text)
        	self.driver.find_element_by_xpath("//textarea").send_keys(text)
        	self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]").click()

my_bot = InstaBot('testmark123', pw)
sleep(2)
quit()

