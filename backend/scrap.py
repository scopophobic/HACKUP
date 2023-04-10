from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def unstophackathons():
    driver = webdriver.Chrome(
    '/Users/scopo0/Downloads/chromedriver_mac_arm64/chromedriver')
    # url = 'https://unstop.com/hackathons'
    driver.get('https://unstop.com/hackathons')

    # web_driver_
    wait = WebDriverWait(driver, 10)
    # Scrape the content
    html_source = driver.page_source
    # print(html)

    soup = BeautifulSoup(html_source, 'lxml')
    card = soup.findAll('app-competition-listing',
                    class_='ng-tns-c195-1 ng-star-inserted')
    
    f= open("DATA/unstophackathon.txt","w+")
    for i in card:
        name = i.h2.text
        place = i.p.text
        f.write(f"hackathon name : {name}\n")
        f.write(f"location/college :{place}\n")
        print(f'FILE CREATED')


    # Close the browser
    driver.quit()



if __name__ == '__main__':
    while True:
        unstophackathons()
        time_wait=10
        print(f"Waiting for {time_wait} minutes")
        time.sleep(time_wait*60)
