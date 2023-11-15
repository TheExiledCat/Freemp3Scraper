from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import scraper as scraper 
import sys
import time
import json
import argparse
import os
import chromedriver_autoinstaller_fix
import undetected_chromedriver as uWebDriver
import random
chromedriver_autoinstaller_fix.install()  
parser = argparse.ArgumentParser()


user = os.path.expanduser("~")


parser.add_argument("-mode","--mode",help="Select download mode- options: album | track ",default="track")
parser.add_argument("-p","--path",help="Select download path- default = "+user+"/Music/FreeMp3Parser",default=user+"/Music/FreeMp3Parser")
parser.add_argument("-t","--title",help="Title: artist and album/track name")

args = parser.parse_args()
#print(f"{args.mode} {args.path}")
chrome_options = uWebDriver.ChromeOptions()
prefs = {"profile.default_content_settings.popups": 0,
             "download.default_directory": args.path,#IMPORTANT - ENDING SLASH V IMPORTANT
             "directory_upgrade": True}
chrome_options.add_experimental_option('prefs',prefs)
adblocker_path = "adblocker"
chrome_options.add_argument('load-extension=' + adblocker_path)
with open("agents.txt") as file:
    chrome_options.add_argument("user-agent="+random.choice(file.readlines()))
driver  = webdriver.Chrome(options=chrome_options)
title = args.title
with open("config.json") as file:
    options = json.load(file)

if __name__=="__main__":
    if len(sys.argv)>1:
        print("Welcome to freemp3scrape, use the -h flag to find out all the commands")
        print(driver.window_handles)
        print("loading...")
        while len(driver.window_handles)<2:
            continue
        for i in range(2):
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            pass
        
        driver.switch_to.window(driver.window_handles[0])
        scraper.run(driver,options["scraper_options"],title)
