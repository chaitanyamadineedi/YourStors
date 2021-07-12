from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class login():

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def storeOpenAndChangeCurrency(self):
        self.driver.get("https://demo.opencart.com/")
        self.driver.find_element_by_xpath("//i[@class='fa fa-caret-down']").click()
        self.driver.find_element_by_xpath("//button[text()='€ Euro']").click()

    def verifyChangeCurrency(self):
        self.driver.find_element_by_xpath("//p[@class='price']").is_displayed()
open=login()
open.__init__()
open.storeOpenAndChangeCurrency()
open.verifyChangeCurrency()
print("test")
open.driver.close()
open.driver.quit()
print("ccc")



