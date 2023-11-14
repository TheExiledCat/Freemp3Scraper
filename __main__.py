from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
driver  = webdriver.Chrome()
driver.get("https://free-mp3-download.net")
print("Test")
if __name__=="__main__":
    if len(sys.argv)>1:
        print(sys.argv[1])
m= input("ABC")
time.sleep(10)