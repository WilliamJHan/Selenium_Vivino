from selenium import webdriver
import time
import re


# Set up chrome driver
driver = webdriver.Chrome()
# driver = webdriver.Chrome(r'C:\Users\JeongwooHan\Desktop\ChromeDriver\chromedriver.exe')

# Go to the page to scrape
driver.get("https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NTBQS660DQ1WSwYSLmoFQNn0NNuyxKLM1JLEHLX8JFu1fFu18pLoWKAMmDKCUMZQngmEhlLmasW2iVUARfgfyg%3D%3D")

# Click each wine to go to specific wine page
wine_button = driver.find_element_by_xpath('//div[@class="vintageTitle__vintageTitle--2iCdc"]/a')
wine_buttom.click()

# Elements that I want to scrape
winery = driver.find_element_by_xpath('//span[@class="headline"]/a[@class="winery"]').text
wine_type = driver.find_element_by_xpath('//span[@class="wineLocationHeader__wineType--14nrC"]').text
city = driver.find_element_by_xpath('//a[@class="anchor__anchor--3DOSm wineLocationHeader__region--1cbip"]').text
country = driver.find_element_by_xpath('//a[@class="anchor__anchor--3DOSm wineLocationHeader__country--1RcW2"]').text
wine_name = driver.find_element_by_xpath('//span[@class="vintage"]/a[@class="wine"]').text
year = driver.find_element_by_xpath('//span[@class="vintage"]').text
overall_rating = driver.find_element_by_xpath('//div[@class="vivinoRating__averageValue--3Navj"]').text
# I just need the number from here
overall_rating_count = driver.find_element_by_xpath('//div[@class="vivinoRating__caption--3tZeS"]').text
# Seems like every page is different
price = 
# How do I get an element? I need the 'left' element
light_bold = driver.find_element_by_xpath('//div[@class="indicatorBar__meter--2t_YL tasteStructure__progressBar--hjNb2"]/span[@class="indicatorBar__progress--3aXLX"]/style')
smooth_tannic = 
dry_sweet = 
soft_acidic = 

print('Title = ')