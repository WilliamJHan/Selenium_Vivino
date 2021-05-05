from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import csv
import re
import time

# Set up chrome driver
driver = webdriver.Chrome('C:\\Users\\JeongwooHan\\Desktop\\ChromeDriver\\chromedriver.exe')

# Go to the page to scrape
driver.get("https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NFBLrrQNDVZLBhIuagVAyfQ027LEoszUksQctfwkW7V8W7XykuhYoEyxbUkFAIb-FFM%3D")
time.sleep(1)

# Set up action chains
actions = ActionChains(driver)

#Scroll to the bottom
# SCROLL_PAUSE_TIME = 1
# last_height = driver.execute_script("return document.body.scrollHeight")
# count = 0
# while count < 1:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     last_height = new_height
#     count = count + 1

#Scroll to the bottom
SCROLL_PAUSE_TIME = 3.5
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Set up CSV
csv_file = open('vivino_wine.csv', 'w', newline = '')
fieldnames = ['winery','wine_type','city','country','wine_name','year','overall_rating','overall_rating_count',\
              'price','light_bold','smooth_tannic','dry_sweet','soft_acidic']
writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
writer.writeheader()

# Get all urls
all_urls = driver.find_elements_by_xpath(".//div[@class='explorerPage__results--3wqLw']/div/div")
one_url = all_urls[0]
url = one_url.find_element_by_xpath("./div/div/a")
all_str_urls = [url.find_element_by_xpath("./div/div/a").get_attribute('href') for url in all_urls]

# Define function to find the metrics
def find_metrics(driver, wine_dict):

    metric_dict = {"Light": "light_bold",
                   "Smooth": "smooth_tannic",
                   "Dry": "dry_sweet",
                   "Soft": "soft_acidic"}
    
    all_metric_names = driver.find_elements_by_xpath('//tr[@class="tasteStructure__tasteCharacteristic--1rMFl"]/td/div[@class="tasteStructure__property--loYWN"]')
    selected_metric_names = [all_metric_names[i].text for i in range(len(all_metric_names)) if i%2 == 0]
    final_metric_names = [metric_dict[key] for key in selected_metric_names]
    missing_metric_names = list(set(metric_dict.values()) - set(final_metric_names))
    
    all_metrics_prep = driver.find_elements_by_xpath('//div[@class="indicatorBar__meter--2t_YL tasteStructure__progressBar--hjNb2"]/span[@class="indicatorBar__progress--3aXLX"]')
    all_metrics = [float(re.findall('\d*\.?\d+',all_metrics_prep[i].get_attribute('style'))[1]) for i in range(len(all_metrics_prep))]
    
    if len(missing_metric_names) > 0:
        for i in missing_metric_names:
            wine_dict[i] = -1

    for i,j in zip(final_metric_names, all_metrics):
        wine_dict[i] = j
    
    return wine_dict

index = 1
for url in all_str_urls:

    # Keep index documented
    print("Scraping Item Number: " + str(index))
    index = index + 1

    # Go into each link
    driver.get(url)
    
    # Clean dictionary to create the current row
    wine_dict = {}

    # Pull different elements using xpath
    try:
        winery = driver.find_element_by_xpath('//span[@class="headline"]/a[@class="winery"]').text
    except Exception as e:
        print(e)
        winery = 'NA'
        
    try:
        wine_type = driver.find_element_by_xpath('//span[@class="wineLocationHeader__wineType--14nrC"]').text
    except Exception as e:
        print(e)
        wine_type = 'NA'
        
    try:
        city = driver.find_element_by_xpath('//a[@class="anchor__anchor--3DOSm wineLocationHeader__region--1cbip"]').text
    except Exception as e:
        print(e)
        city = 'NA'
        
    try:
        country = driver.find_element_by_xpath('//a[@class="anchor__anchor--3DOSm wineLocationHeader__country--1RcW2"]').text
    except Exception as e:
        print(e)
        country = 'NA'
        
    try:
        wine_name = driver.find_element_by_xpath('//span[@class="vintage"]/a[@class="wine"]').text
    except Exception as e:
        print(e)
        wine_name = 'NA'
        
    try:
        year_prep = driver.find_element_by_xpath('//span[@class="vintage"]').text
        year = int(re.findall('\d+', year_prep)[-1])
    except Exception as e:
        print(e)
        year = -1
        
    try:
        overall_rating = float(driver.find_element_by_xpath('//div[@class="vivinoRating__averageValue--3Navj"]').text)
    except Exception as e:
        print(e)
        overall_rating = -1
        
    try:
        overall_rating_count_prep = driver.find_element_by_xpath('//div[@class="vivinoRating__caption--3tZeS"]').text
        overall_rating_count = int(re.findall('\d+', overall_rating_count_prep)[0])
    except Exception as e:
        print(e)
        overall_rating_count = -1
        
    try:
        time.sleep(0.5)
        price_prep = driver.find_element_by_xpath('//span[@class="purchaseAvailability__currentPrice--3mO4u"]').text
        price = float(re.findall('\d+', price_prep)[0])
    except:
        try:
            price_prep = driver.find_element_by_xpath('//span[@class="purchaseAvailabilityPPC__amount--2_4GT"]').text
            price = float(re.findall('\d+', price_prep)[0])
        except Exception as e:
            print(e)
            price = -1

    # Need some scrolling for the page to load
    try:
        driver.execute_script("window.scrollTo(0, 1080);")
        driver.execute_script("window.scrollTo(0, 1080);")
        driver.execute_script("window.scrollTo(0, 1080);")
        driver.execute_script("window.scrollTo(0, 1080);")
        driver.execute_script("window.scrollTo(0, 1080);")
        time.sleep(2)
        wine_dict = find_metrics(driver, wine_dict)
    except Exception as e:
        print(e)
        wine_dict['light_bold'] = -1
        wine_dict['smooth_tannic'] = -1
        wine_dict['dry_sweet'] = -1
        wine_dict['soft_acidic'] = -1

    # Define wine_dict and assign each element
    wine_dict['winery'] = winery
    wine_dict['wine_type'] = wine_type
    wine_dict['city'] = city
    wine_dict['country'] = country
    wine_dict['wine_name'] = wine_name
    wine_dict['year'] = year
    wine_dict['overall_rating'] = overall_rating
    wine_dict['overall_rating_count'] = overall_rating_count
    wine_dict['price'] = price

    writer.writerow(wine_dict)

csv_file.close()