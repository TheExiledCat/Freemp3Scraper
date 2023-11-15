from selenium import webdriver
import undetected_chromedriver as uWebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from urllib.request import urlretrieve
site = "https://free-mp3-download.net"


def run(browser,scraper_options, title):
    
    if scraper_options["mode"]=="album":
        scrape_album(browser,scraper_options,title)
    elif scraper_options["mode"]=="track":
        scrape_track(browser,scraper_options,title)
    else:
        print("error")
    
    input()
    

def scrape_album(browser:webdriver.Chrome,scraper_options,title):
    
   
    browser.get(site)
    search_form = browser.find_element(By.ID,"search")
    input_box = search_form.find_element(By.XPATH,"//input")
    input_box.send_keys(title)
    search_button = search_form.find_element(By.XPATH,"//button")
    search_button.click()
    
    table =WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "results_t")))

    track_elements =table.find_elements(By.XPATH,"*")
    #open pages

    for track in track_elements:
        print(track)
        
        
        download_button = track.find_element(By.CLASS_NAME,"btn")
        browser.execute_script("arguments[0].setAttribute('target',arguments[1])",download_button.find_element(By.XPATH,".."),"_blank")
        download_button.click()
        browser.switch_to.window(browser.window_handles[1])
        
        
        
        
        
        #browser.close()
        browser.switch_to.window(browser.window_handles[0])
    input()
        
    
    
def scrape_track(browser,scraper_options,title):
    browser.get(site)
    pass
