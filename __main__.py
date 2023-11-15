from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import scraper 
import sys
import time
import json
import argparse
import os
parser = argparse.ArgumentParser()

user = os.path.expanduser("~")
driver  = webdriver.Chrome()

parser.add_argument("-mode","--mode",help="Select download mode- options: album | track ")
parser.add_argument("-p","--path",help="Select download path- default = "+user+"/Music")
with open("config.json") as file:
    options = json.load(file)

print(options)
if __name__=="__main__":
    if len(sys.argv)>1:
        print(sys.argv[1])
        scraper.run(driver,options)
