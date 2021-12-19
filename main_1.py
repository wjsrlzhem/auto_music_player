#auto music player

from selenium import webdriver
import time
import pyautogui
import datetime


URL = 'https://www.youtube.com/Something THAT YOU WANT TO WATCH URL'
stack = 0
driver = webdriver.Chrome(executable_path  = 'chromedriver')

driver.get(url = URL)
driver.set_window_position(0,0)
driver.set_window_size(1920,1080)
time.sleep(5)
driver.find_element_by_css_selector('#movie_player > div.ytp-cued-thumbnail-overlay > button').click()
time.sleep(3)
size = pyautogui.size()

print('screen size : {0}'.format(size))

while True:
    try :
        nowTime = datetime.datetime.now()
        location = pyautogui.locateCenterOnScreen('skip.png', confidence = 0.7)
        
        if location == None:
            print("광고 없음")
            time.sleep(3)
            
            continue


        print("광고 발견")
        pyautogui.moveTo(location[0],location[1],1)
        pyautogui.click(button = 'left')
        time.sleep(5)
        break
        
    except KeyboardInterrupt:
        print('thx')
        break
