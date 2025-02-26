from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
      EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book").click()


    x_value = browser.find_element(By.ID, "input_value").text
    

    y = calc(x_value)

    input_answer = browser.find_element(By.ID, "answer").send_keys(y)

    button = browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(3)
    browser.quit()

