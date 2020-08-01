from time import sleep
from selenium import webdriver
import pyautogui as pag

ACCOUNT_EMAIL = "goobadoops@gmail.com"
ACCOUNT_PASSWORD = "ScoobyDoPapa1"
word = "gameplay"


# FUNCTIONS
def filter_by_time():
    pag.moveTo(342, 235)
    pag.click()
    sleep(1)
    pag.moveTo(1201, 361)
    pag.click()
    sleep(2)


def clickable():
    x, y, z = pag.pixel(203, 181)
    if x == y == z:
        return False
    return True


def enter_video():
    pag.click()
    sleep(1)


def comment():
    for _ in range(2):
        pag.scroll(-10)
        sleep(0.5)
    sleep(1)


def go_back():
    pag.moveTo(21, 80)
    pag.click()
    sleep(1)


def video_location():
    pag.moveTo(472, 275)


# Set chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--incognito")

# Open Chrome driver
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_position(0, 0)
driver.maximize_window()

# Login to Google
driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys(ACCOUNT_EMAIL)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(10)
# Google signup doesn't accept passwords so you have to type them. TYPE YOUR GOOGLE PASSWORD
# driver.find_element_by_xpath('//input[@type="password"]').send_keys(ACCOUNT_PASSWORD)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(5)

# Go to Youtube
driver.get('https://youtube.com')
sleep(5)

# Search a word
driver.find_element_by_xpath('//input[@id="search"]').send_keys(word)
driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
sleep(5)

filter_by_time()

for _ in range(2):
    video_location()
    pag.scroll(-6)
    sleep(2)
    if clickable():
        enter_video()
        comment()
        # Click on comment box
        driver.find_element_by_id('placeholder-area').click()
        # Send the keys to the input field
        driver.find_element_by_id('contenteditable-root').send_keys('hola')
        pag.hotkey('command', 'ENTER')
        # driver.find_element_by_xpath('//input[@id="contenteditable-root"]').send_keys('hola')
        sleep(1)
        # Find 'Comment' button
        # driver.find_element_by_xpath('//button[text()="Comentar"]')
        # driver.find_element_by_css_selector('style-scope ytd-button-renderer style-primary size-default').click()
        sleep(1)
        go_back()
        sleep(1)
    else:
        continue








