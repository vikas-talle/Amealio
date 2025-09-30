from selenium import webdriver
from webdriver-manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.preprod-merchant.amealio.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("name", "number").send_keys("9989023333")
driver.find_element("id", "password").send_keys("amealio@1")
driver.find_element("xpath", "//*[@id="root"]/div[1]/div/div[2]/div/form/button/span[1]").click()
driver.quit()
