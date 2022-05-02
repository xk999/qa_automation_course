"""
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3. Нажать на кнопку "Book"
4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = driver.find_element_by_id("book")
button.click()


x_value = driver.find_element_by_id("input_value")
x = x_value.text
solution = str(log(abs(12*sin(int(x)))))

answer_field = driver.find_element_by_id("answer")
answer_field.send_keys(solution)

button2 = driver.find_element_by_id("solve")
button2.click()

time.sleep(5)

driver.quit()
