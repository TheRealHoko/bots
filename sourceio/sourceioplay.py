#!/usr/bin/python3
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'http://s0urce.io/'

driver = webdriver.Firefox()
driver.get(url)
elem = driver.find_element_by_xpath('//*[@id="login-input"]')
elem.clear()
elem.send_keys("pørtal")
elem.send_keys(Keys.RETURN)
i = 0
src = ['']
first_src = []
while True:
	element = WebDriverWait(driver, 100).until(
			EC.element_to_be_clickable((By.XPATH , '//*[@id="tool-type-word"]'))
	)
	elem = driver.find_element_by_xpath('//*[@class="tool-type-img"]')
	val = elem.get_attribute('src')
	first_src.append(val)
	if i > 0:
		src.append(val)
	if 'ng' in first_src[i][-2:]:
		element = driver.find_element_by_xpath('//*[@id="targetmessage-button-send"]').click()
		#element = driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[5]/div[3]/span/img').switchTo()
		element = driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[5]/div[3]/span/img').click()
		element = WebDriverWait(driver, 1000).until(
				EC.element_to_be_clickable((By.XPATH , '//*[@id="tool-type-word"]'))
				)
		elem = driver.find_element_by_xpath('//*[@class="tool-type-img"]')
		first_src = elem.get_attribute('src')
	if url + 'client/img/word/e' in first_src[i]:
		n_dict = 'e.dict'
		with open(n_dict, 'r', newline=None) as f:
			contents = f.readlines()
	if url + 'client/img/word/m' in first_src[i]:
		n_dict = 'm.dict'
		with open(n_dict, 'r', newline=None) as f:
			contents = f.readlines()
	if url + 'client/img/word/h' in first_src[i]:
		n_dict = 'h.dict'
		with open(n_dict, 'r', newline=None) as f:
			contents = f.readlines()
	if '/' in first_src[i][-2:]:
		word = first_src[i][-1:]
	else:
		word = first_src[i][-2:]
	contents_word = contents[int(word)]
	print(first_src, i)
	print(src)
	print(word)
	print(contents_word)
	elem = driver.find_element_by_xpath('//*[@id="tool-type-word"]')
	elem.clear()
	elem.send_keys(contents_word)
	time.sleep(0.25)
	elem.send_keys(Keys.RETURN)
	if src[i] == first_src[i]:
		with open(n_dict, 'w', newline=None) as f:
			ch_input = input("What's the word?") + '\n'
			contents[int(word)] = ch_input
			f.writelines(contents)
	i += 1
