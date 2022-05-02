"""
Задание:
1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
2. Нажать на кнопку
3. Переключиться на новую вкладку
4. Пройти капчу для робота и получить число-ответ
"""

import time
from selenium import webdriver
from math import log, sin

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/redirect_accept.html")

button = driver.find_element_by_tag_name("button")
button.click()

win2 = driver.window_handles[1]

driver.switch_to.window(win2)

x_value = driver.find_element_by_id("input_value")
x = x_value.text
solution = str(log(abs(12*sin(int(x)))))

answer_field = driver.find_element_by_id("answer")
answer_field.send_keys(solution)

button2 = driver.find_element_by_tag_name("button")
button2.click()

time.sleep(5)

driver.quit()
