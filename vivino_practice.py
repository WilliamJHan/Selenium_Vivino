from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import csv
import time
import re

# Set up chrome driver
driver = webdriver.Chrome('C:\\Users\\JeongwooHan\\Desktop\\ChromeDriver\\chromedriver.exe')

# Go to the page to scrape
driver.get("https://www.vivino.com/cartuxa-pera-manca-tinto/w/2545450?year=1990")
actions = ActionChains(driver)

# Set up CSV
csv_file = open('vivino_wine.csv', 'w', newline = '')
fieldnames = ['winery','wine_type','city','country','wine_name','year','overall_rating','overall_rating_count',\
              'price','light_bold','smooth_tannic','dry_sweet','soft_acidic']
writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

#Pull different elements using xpath
try:
    winery = driver.find_element_by_xpath('//span[@class="headline"]/a[@class="winery"]').text
except Exception as e:
    print(e)
    
try:
    wine_type = driver.find_element_by_xpath('//span[@class="wineLocationHeader__wineType--14nrC"]').text
except Exception as e:
    print(e)
    
try:
    city = driver.find_element_by_xpath('//a[@class="anchor__anchor--3DOSm wineLocationHeader__region--1cbip"]').text
except Exception as e:
    print(e)
    
try:
    country = driver.find_element_by_xpath('//a[@class="anchor__anchor--3DOSm wineLocationHeader__country--1RcW2"]').text
except Exception as e:
    print(e)
    
try:
    wine_name = driver.find_element_by_xpath('//span[@class="vintage"]/a[@class="wine"]').text
except Exception as e:
    print(e)
    
try:
    year_prep = driver.find_element_by_xpath('//span[@class="vintage"]').text
    year = int(re.findall('\d+', year_prep)[0])
except Exception as e:
    print(e)
    
try:
    overall_rating = float(driver.find_element_by_xpath('//div[@class="vivinoRating__averageValue--3Navj"]').text)
except Exception as e:
    print(e)
    
try:
    overall_rating_count_prep = driver.find_element_by_xpath('//div[@class="vivinoRating__caption--3tZeS"]').text
    overall_rating_count = int(re.findall('\d+', overall_rating_count_prep)[0])
except Exception as e:
    print(e)
    
try:
    price_prep = driver.find_element_by_xpath('//span[@class="purchaseAvailability__currentPrice--3mO4u"]').text
    price = float(re.findall('\d+',price_prep)[0])
except Exception as e:
    print(e)
    
try:
    driver.execute_script("window.scrollTo(0, 1080);")
    driver.execute_script("window.scrollTo(0, 1080);")
    driver.execute_script("window.scrollTo(0, 1080);")
    driver.execute_script("window.scrollTo(0, 1080);")
    driver.execute_script("window.scrollTo(0, 1080);")
    time.sleep(2)
    light_bold_prep = driver.find_element_by_xpath('//div[@class="indicatorBar__meter--2t_YL tasteStructure__progressBar--hjNb2"]/span[@class="indicatorBar__progress--3aXLX"]').get_attribute('style')
    light_bold = float(re.findall('\d*\.?\d+',light_bold_prep)[1])
except Exception as e:
    print(e)
    
try:
    smooth_tannic_prep = driver.find_element_by_xpath('//div[@class="indicatorBar__meter--2t_YL tasteStructure__progressBar--hjNb2"]/span[@class="indicatorBar__progress--3aXLX"]').get_attribute('style')
    smooth_tannic = float(re.findall('\d*\.?\d+',smooth_tannic_prep)[1])
except Exception as e:
    print(e)
    
try:
    dry_sweet_prep = driver.find_element_by_xpath('//div[@class="indicatorBar__meter--2t_YL tasteStructure__progressBar--hjNb2"]/span[@class="indicatorBar__progress--3aXLX"]').get_attribute('style')
    dry_sweet = float(re.findall('\d*\.?\d+',dry_sweet_prep)[1])
except Exception as e:
    print(e)
    
try:
    soft_acidic_prep = driver.find_element_by_xpath('//div[@class="indicatorBar__meter--2t_YL tasteStructure__progressBar--hjNb2"]/span[@class="indicatorBar__progress--3aXLX"]').get_attribute('style')
    soft_acidic = float(re.findall('\d*\.?\d+',soft_acidic_prep)[1])
except Exception as e:
    print(e)

# Define wine_dict and assign each element
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

# Save the dictionary into the CSV
writer.writeheader()
writer.writerow(wine_dict)
csv_file.close()