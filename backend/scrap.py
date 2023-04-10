from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up the webdriver
driver = webdriver.Chrome(
    '/Users/scopo0/Downloads/chromedriver_mac_arm64/chromedriver')

# Load the webpage
driver.get('https://unstop.com/hackathons')

# Wait for up to 10 seconds for elements to load
wait = WebDriverWait(driver, 10)

# Wait for the page to load by waiting for the presence of a specific element
# element_present = EC.presence_of_element_located(('h2', 'body'))
# wait.until(element_present)

# Scrape the content
html_source = driver.page_source
# print(html)

soup = BeautifulSoup(html_source, 'lxml')
card = soup.findAll('app-competition-listing',
                    class_='ng-tns-c195-1 ng-star-inserted')



for i in card:
    name=i.h2.text
    place=i.p.text
    print(name)
    print("\n")
    print(place)



# Close the browser
driver.quit()
