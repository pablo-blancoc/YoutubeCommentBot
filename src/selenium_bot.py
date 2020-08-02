from time import sleep
from selenium import webdriver
import pyautogui as pag
import random

ACCOUNT_EMAIL = "goobadoops@gmail.com"
ACCOUNT_PASSWORD = "ScoobyDoPapa1"
WORD_TO_SEARCH = "gameplay"
VIDEOS_TO_COMMENT = 10
COMMENT = "this is where you put the comment to make"


# FUNCTIONS
def delay(n):
    if n < 4:
        n = 5
    s = random.randint(3, n)
    sleep(s)


def delay_less(n):
    s = random.randint(1, n)
    sleep(s)


def filter_by_time():
    # Press filter button
    pag.moveTo(342, 235)
    pag.click()
    sleep(1)
    # Press filter by upload time button
    pag.moveTo(1201, 361)
    pag.click()
    sleep(2)


# If the color of the screen isn't the same for RGB means that there is a video you can click
def clickable():
    x, y, z = pag.pixel(203, 181)
    if x == y == z:
        return False
    return True


# Click on the video
def enter_video():
    pag.click()
    sleep(1)


# Scroll down on the video screen so you can see the comment button
def comment():
    for _ in range(3):
        pag.scroll(-10)
        sleep(0.5)
    sleep(1)


def go_back():
    # Press back arrow button on Google
    pag.moveTo(21, 80)
    pag.click()
    sleep(1)


# Start location where videos can be found
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

# Open Chrome driver and maximize the window on the screen
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_position(0, 0)
driver.maximize_window()

# Login to Google via StackOverFlow
driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")
sleep(0.5)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
sleep(0.5)
driver.find_element_by_xpath('//input[@type="email"]').send_keys(ACCOUNT_EMAIL)
sleep(1)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
pag.write(ACCOUNT_PASSWORD, 3)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
delay(5)

# Go to Youtube
driver.get('https://youtube.com')
delay(5)

# Search a word
driver.find_element_by_xpath('//input[@id="search"]').send_keys(WORD_TO_SEARCH)
sleep(1)
driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
delay(6)

# Make the results page be filtered by upload time
filter_by_time()

for video_number in range(VIDEOS_TO_COMMENT):
    delay_less(5)
    video_location()
    pag.scroll(-6)
    sleep(1)
    if clickable():
        enter_video()
        comment()
        # Click on comment box
        try:
            driver.find_element_by_id('placeholder-area').click()
            # Send the comment to the input field
            driver.find_element_by_id('contenteditable-root').send_keys(COMMENT)
            delay_less(3)
            # Press enter to comment
            pag.hotkey('command', 'ENTER')
            delay_less(2)
            go_back()
            delay_less(2)
        except:
            print(f"ERROR: couldn't comment correctly on video: {video_number}")
    else:
        continue








