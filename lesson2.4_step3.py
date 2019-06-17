import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


checkPrice = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'),"10000 RUR")
    )
button = browser.find_element_by_xpath('//*[@id="book"]')
button.click()



input1 = browser.find_element_by_xpath("//*[@id='input_value']")
y = calc(input1.text)

input2 = browser.find_element_by_xpath("//*[@id='answer']")
input2.send_keys(y)

button = browser.find_element_by_xpath("/html/body/form/div/div/button")
button.click()