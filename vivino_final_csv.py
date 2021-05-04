from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time

# Set up chrome driver
driver = webdriver.Chrome('C:\\Users\\JeongwooHan\\Desktop\\ChromeDriver\\chromedriver.exe')

# Go to the page to scrape
driver.get("https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NTBQS660DQ1WSwYSLmoFQNn0NNuyxKLM1JLEHLX8JFu1fFu18pLoWKAMmDKCUMZQngmEhlLmasW2iVUARfgfyg%3D%3D")

actions = ActionChains(driver)

# Click each wine to go to specific wine page
wine_button = driver.find_element_by_xpath('//div[@class="vintageTitle__vintageTitle--2iCdc"]/a').get_attribute('href')
wine_button.click()


wine_button.switch_to.window(wine_button.window_handles[-1])
wine_button.close()

csv_file = open('vivino_wine.csv', 'w', encoding = 'utf-8', newline = '')
writer = csv.writer(csv_file)



SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(SCROLL_PAUSE_TIME)
	new height = driver.execute_script("return document.body.scrollHeight")
	if new_height == last_height:
		break
	last height = new_height


all_urls

for url in all_urls:





While True:
	
	SCROLL_PAUSE_TIME = 1

	last_height = driver.execute_script("return document.body.scrollHeight")

	while True:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(SCROLL_PAUSE_TIME)
		new height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last height = new_height

	try:

		# Elements that I want to scrape
		winery = driver.find_element_by_xpath('//span[@class="headline"]/a[@class="winery"]').text
		wine_type = driver.find_element_by_xpath('//span[@class="wineLocationHeader__wineType--14nrC"]').text
		city = driver.find_element_by_xpath('//a[@class="anchor__anchor--3DOSm wineLocationHeader__region--1cbip"]').text
		country = driver.find_element_by_xpath('//a[@class="anchor__anchor--3DOSm wineLocationHeader__country--1RcW2"]').text
		wine_name = driver.find_element_by_xpath('//span[@class="vintage"]/a[@class="wine"]').text
		year = int(driver.find_element_by_xpath('//span[@class="vintage"]').text[0])
		overall_rating = int(driver.find_element_by_xpath('//div[@class="vivinoRating__averageValue--3Navj"]').text)
		# I just need the number from here
		overall_rating_count = int(driver.find_element_by_xpath('//div[@class="vivinoRating__caption--3tZeS"]').text)
		# Seems like every page is different
		try:
			price = blah
		except:
			try:
				price = bleh
			except Exception as e:
				print(e)
		# How do I get an element? I need the 'left' element
		light_bold = int(driver.find_element_by_xpath('//div[@class="indicatorBar__meter--2t_YL tasteStructure__progressBar--hjNb2"]/span[@class="indicatorBar__progress--3aXLX"]/style'))
		smooth_tannic = 
		dry_sweet = 
		soft_acidic = 


		wine_dict = {}

		wine_dict['winery'] = winery
		wine_dict['wine_type'] = wine_type
		wine_dict['city'] = city
		wine_dict['country'] = country
		wine_dict['wine_name'] = wine_name
		wine_dict['year'] = year
		wine_dict['overall_rating'] = overall_rating
		wine_dict['overall_rating_count'] = overall_rating_count
		wine_dict['price'] = price
		wine_dict['light_bold'] = light_bold
		wine_dict['smooth_tannic'] = smooth_tannic
		wine_dict['dry_sweet'] = dry_sweet
		wine_dict['soft_acidic'] = soft_acidic

		writer.writerow(wine_dict.values())





except Exception as e:
		print(e)
		csv_file.close()
		driver.close()
		break