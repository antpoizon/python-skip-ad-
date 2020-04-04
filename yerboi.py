import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620')
# enters email
email_box = driver.find_element_by_name('identifier')
email_box.send_keys('antpoizon@gmail.com')
email_box.send_keys(Keys.ENTER)
# enters password
time.sleep(5)
pass_box = driver.find_element_by_name('password')
pass_box.send_keys('ratslikejazz')
pass_box.send_keys(Keys.ENTER)
# looks for skip ad box
video_playing = driver.find_elements_by_class_name('ytp-ad-skip-button-container')
x = 10
while not video_playing and x <= 10:
    video_playing = driver.find_elements_by_class_name('ytp-ad-skip-button-container')
    print('no ad to skip!')
else:
    print('ad found!')
    time.sleep(6)
    ad_button = driver.find_element_by_class_name('ytp-ad-skip-button-container')
    ad_button.click()
    driver.find_elements_by_class_name('ytp-ad-skip-button-container')
    x = x-1
    if x == 0:
        break
    else:
        continue
