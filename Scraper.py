from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
import json

# Do cool thing
wait = WebDriverWait(webdriver, 10)

driver = webdriver.Chrome("/Users/victorsunderland/dev/HunkyHusky/chromedriver-3")
driver.get("https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7")

time.sleep(3)

content = driver.find_elements_by_class_name("circleChart")

#https://www.northeastern.edu/campusrec/
#/html/body/section[2]/div/header/i/section[2]/div/header/embed

driver.close()

gymList = [
    'Marino Center - 2nd Floor',
    'Marino Center - Gymnasium',
    'Marino Center - 3rd Floor Weight Room',
    'Marino Center - 3rd Floor Select & Cardio',
    'Marino Center - Track',
    'SquashBusters - 4th Floor',]

percentList = [int(elem.text[0:-1]) for elem in content]
gymPercents = dict(zip(gymList, percentList))

with open("gympercents.json", "w") as outfile:
    json.dump(gymPercents, outfile)

print(gymPercents)



