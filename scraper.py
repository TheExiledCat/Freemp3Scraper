from selenium import webdriver
import undetected_chromedriver as uWebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
site = "https://free-mp3-download.net"


def run(browser,scraper_options, title):
    
    if scraper_options["mode"]=="album":
        scrape_album(browser,scraper_options,title)
    elif scraper_options["mode"]=="track":
        scrape_track(browser,scraper_options,title)
    else:
        print("error")
    
    input("Press enter once all files are downloaded")
    

def scrape_album(browser:uWebDriver.Chrome,scraper_options,title):
    
    
   
    browser.get(site)
    search_form = browser.find_element(By.ID,"search")
    input_box = search_form.find_element(By.XPATH,"//input")
    input_box.send_keys(title)
    time.sleep(0.5)
    search_button = search_form.find_element(By.XPATH,"//button")
    search_button.click()
    
    table =WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "results_t")))

    track_elements =table.find_elements(By.XPATH,"*")
    #open pages
    i = 1
    captcha = True
    for track in track_elements:
        
        download_button = track.find_element(By.CLASS_NAME,"btn")
        browser.execute_script("arguments[0].setAttribute('target',arguments[1])",download_button.find_element(By.XPATH,".."),"_blank")
        download_button.click()
        browser.switch_to.window(browser.window_handles[len(browser.window_handles)-1])
        #qualities
        quality_elements = browser.find_element(By.ID,"quality-row").find_elements(By.XPATH,"*")
        quality = scraper_options["quality"]
        selection = -1
        if quality == "mp3(128)":
            selection = 0
        elif quality =="mp3(320)":
            selection = 1
        elif quality =="FLAC":
            selection =2
        quality_elements[selection].find_element(By.CLASS_NAME,"quality-label").click()
        
        # captcha pls
        try:
            captcha = browser.find_element(By.CLASS_NAME, "g-recaptcha")
            captcha.click()
            input()
            time.sleep(2)
            try: 
                
                print(browser.find_element(By.ID,"rc-imageselect"))
                if not browser.find_element(By.ID,"rc-imageselect").is_displayed():
                    pass
                else:
                    print("cap")
                    input()
                
            except Exception as e:
                print(e.args)
                print("at 74")
                
        except Exception as e:
            print(e.args)
            print("at 78")
         
        
        #download 
        download_button = browser.find_element(By.CLASS_NAME,"card-action").find_element(By.XPATH,"//button")
        time.sleep(1)
        print(browser.find_element(By.ID,"song-title").text)
        download_button.click()
        time.sleep(1)
        browser.switch_to.window(browser.window_handles[0])
    input()
        
    
    
def scrape_track(browser,scraper_options,title):
    browser.get(site)
    pass
