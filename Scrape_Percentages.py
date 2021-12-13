from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()
driver.get("https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7")

availability_perc = driver.find_elements(By.CLASS_NAME, "circleChart")

driver.close()

gym_list = [
    'Marino Center - 2nd Floor',
    'Marino Center - Gymnasium',
    'Marino Center - 3rd Floor Weight Room',
    'Marino Center - 3rd Floor Select & Cardio',
    'Marino Center - Track',
    'SquashBusters - 4th Floor']

percent_list = [int(percent.text[0:-1]) for percent in availability_perc]
gym_percents = dict(zip(gym_list, percent_list))

with open("gym_percents.json", "w") as outfile:
    json.dump(gym_percents, outfile)
