import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import pickle

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time
from datetime import datetime

url = 'https://www.ice.gov/webform/ice-tip-form'
chrome_service = ChromeService(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options = chrome_options, service=chrome_service)
driver.get(url)

time.sleep(2)
driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
leo_no = driver.find_element(By.XPATH, "//label[@for='edit-are-you-a-leo-no']")
time.sleep(1)
leo_no.click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
firstname = driver.find_element(By.ID,"edit-first-name")
lastname = driver.find_element(By.ID,"edit-last-name")
email = driver.find_element(By.ID,"edit-email")
phonenumber = driver.find_element(By.ID,"edit-phone-number")

firstname.send_keys('Ted')
lastname.send_keys('Turduckinson')
phonenumber.send_keys('666-420-6969')
email.send_keys('fuckthepigs@acab.org')

inside_us = driver.find_element(By.XPATH, "//label[normalize-space()='Inside the U.S.']")
time.sleep(1)
inside_us.click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, window.scrollY + 700)")
time.sleep(1)

line1 = driver.find_element(By.ID,"edit-line-1")
line1.send_keys('1599 Pennsylvania Avenue')
line2 = driver.find_element(By.ID,"edit-line-2")
line2.send_keys('Community watchtower')
city = driver.find_element(By.ID,"edit-city")
city.send_keys('Washington')
state = Select(driver.find_element(By.ID,"edit-state"))
state.select_by_visible_text('District of Columbia')
zipcode = driver.find_element(By.ID,"edit-zip-code")
zipcode.send_keys('20500')

driver.execute_script("window.scrollTo(0, window.scrollY + 800)")
time.sleep(1)

human_trafficking = driver.find_element(By.XPATH, "//label[normalize-space()='Human Trafficking (Forced Labor/Slavery)']")
human_trafficking.click()

driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")

time.sleep(1)
line1 = driver.find_element(By.ID,"edit-line-1-location")
line1.send_keys('1600 Pennsylvania Avenue')
line2 = driver.find_element(By.ID,"edit-line-2-location")
line2.send_keys('Pedophile Suite')
city = driver.find_element(By.ID,"edit-city-location")
city.send_keys('Washington')
state = Select(driver.find_element(By.ID,"edit-state-location"))
state.select_by_visible_text('District of Columbia')
zipcode = driver.find_element(By.ID,"edit-zip-code-location")
zipcode.send_keys('20500')

individual = driver.find_element(By.XPATH, "//label[normalize-space()='Individual']")
individual.click()

driver.execute_script("window.scrollTo(0, window.scrollY + 900)")
time.sleep(1)

firstname = driver.find_element(By.ID,"edit-first-name-individual")
lastname = driver.find_element(By.ID,"edit-last-name-individual")
firstname.send_keys('Donald')
lastname.send_keys('Trump')
approximate_age = driver.find_element(By.XPATH, "//label[normalize-space()='Approximate Age']")
approximate_age.click()
time.sleep(1)
approximate_age = driver.find_element(By.ID,"edit-approximate-age")
approximate_age.send_keys('100')
driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
time.sleep(1)

line1 = driver.find_element(By.ID,"edit-line-1-individual")
line1.send_keys('1600 Pennsylvania Avenue')
line2 = driver.find_element(By.ID,"edit-line-2-individual")
line2.send_keys('Pedophile Suite')
city = driver.find_element(By.ID,"edit-city-individual")
city.send_keys('Washington')
state = Select(driver.find_element(By.ID,"edit-state-individual"))
state.select_by_visible_text('District of Columbia')
zipcode = driver.find_element(By.ID,"edit-zip-code-individual")
zipcode.send_keys('20500')

previously = driver.find_element(By.XPATH, "//label[@for='edit-have-you-previously-submitted-this-information-to-any-law-radios-false']")
previously.click()

driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
time.sleep(1)

additional = driver.find_element(By.XPATH, "//label[@for='edit-did-you-have-additional-businesses-individuals-to-report-on-no']")
additional.click()

summary = driver.find_element(By.ID,"edit-please-provide-a-summary-of-the-criminal-activity-limit-2500-cha")
summary.send_keys("Grotesque orange humanoid slimeball orchestrating the abduction of normal people and ruining the lives of family members and the murder of their community members.")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

math_question = driver.find_element(By.CSS_SELECTOR,"label[for='edit-captcha-response']")
math_answer = eval(math_question.text[math_question.text.find("(")+1:math_question.text.find("=")-1])

math_box = driver.find_element(By.ID,"edit-captcha-response")
math_box.send_keys(str(math_answer))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
submit = driver.find_element(By.ID,"edit-submit")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
submit.click()
driver.close()
