from time import sleep
from selenium import webdriver
import pyautogui as pag
import random

######
# Fields to fill
ACCOUNT_EMAIL = "youtube account mail"
ACCOUNT_PASSWORD = "youtube account password"
WORD_TO_SEARCH = "type here the word that's going to be searched in YouTube search bar"
VIDEOS_TO_COMMENT = 30  # Number of times the bot is going to try to comment a video
COMMENT = "type in here the comment that the bot is going to write on every comment it makes"
######


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
    pag.moveTo(347, 241)
    pag.click()
    sleep(0.2)
    pag.moveTo(459, 233)
    pag.click()
    sleep(1)
    # Press filter by upload time button
    pag.moveTo(1343, 368)
    pag.click()
    sleep(2)


# If the color of the screen isn't the same for RGB means that there is a video you can click
def clickable():
    x, y, z = pag.pixel(669, 348)
    if x == y == z:
        return False
    return True


# Click on the video
def enter_video():
    pag.click()
    sleep(1)


# Scroll down on the video screen so you can see the comment button
def comment():
    pag.scroll(-10)
    sleep(0.5)


def go_back():
    # Press back arrow button on Google
    pag.moveTo(21, 81)
    pag.click()
    sleep(1)


# Start location where videos can be found
def video_location():
    pag.moveTo(669, 348)


# Set chrome options
print("Setting up Chrome options...")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--incognito")

# Open Chrome driver and maximize the window on the screen
print("Openning Chrome webdriver")
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_position(0, 0)
driver.maximize_window()

# Login to Google via StackOverFlow
print("Loging-In to StackOverFlow")
driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")
sleep(0.5)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
sleep(0.5)
driver.find_element_by_xpath('//input[@type="email"]').send_keys(ACCOUNT_EMAIL)
sleep(1)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
# Computer can't write the password so you need to type it, you have 10sec
sleep(10)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
delay(5)

# Go to Youtube
print("Going back to YouTube")
driver.get('https://youtube.com')
delay(5)

# Search a word
print(f"Searching for {WORD_TO_SEARCH}")
driver.find_element_by_xpath('//input[@id="search"]').send_keys(WORD_TO_SEARCH)
sleep(1)
driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
delay(6)

# Make the results page be filtered by upload time
print("Filtering result by time...")
filter_by_time()

print("Commenting videos...")
flag_counter = 0
for video_number in range(VIDEOS_TO_COMMENT):
    delay_less(5)
    video_location()
    if flag_counter == 0:
        pag.scroll(-6)
    sleep(1)
    enter_video()
    comment()
    flag_counter += 1
    # Click on comment box
    try:
        driver.find_element_by_id('placeholder-area').click()
        # Send the comment to the input field
        driver.find_element_by_id('contenteditable-root').send_keys(COMMENT)
        delay_less(5)
        # Press enter to comment
        pag.hotkey('command', 'ENTER')
        print(f"Success on trial: {video_number}")
        delay_less(5)
        go_back()
        delay_less(5)
        flag_counter = 0
    except:
        print(f"ERROR: error in trial number: {video_number}")
        comment()
        if flag_counter == 3:
            go_back()
            flag_counter = 0
        sleep(0.5)
print("""

------------------------
FINISHED!


""")
driver.quit()