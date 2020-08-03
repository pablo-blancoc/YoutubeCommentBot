from time import sleep
from selenium import webdriver
import pyautogui as pag
import random

# Fields to fill
ACCOUNT_EMAIL = "youtube account mail"
ACCOUNT_PASSWORD = "youtube account password"
WORD_TO_SEARCH = "type here the word that's going to be searched in YouTube search bar"
VIDEOS_TO_COMMENT = 30  # Number of times the bot is going to try to comment a video
COMMENT = "type in here the comment that the bot is going to write on every comment it makes"


# FUNCTIONS
def delay(n: int):
    """
    Chooses a random number between 3 and n so the bot waits a little and seems more human
    :param n: integer representing maximum number of seconds to wait
    :return: None, just waits
    """
    if n < 4:
        n = 5
    s = random.randint(3, n)
    sleep(s)


def delay_less(n: int):
    """
    Chooses a random number of seconds to wait from 1 to n, to make seem the bot more human.
    :param n: integer representing maximum number of seconds to wait
    :return: None, just waits
    """
    s = random.randint(1, n)
    sleep(s)


def filter_by_time():
    """
    The function is used so that the videos that are displayed on YouTube are filtered by upload time and
        not the 'relevance' (default).
    :return: None
    """
    # Press a random point on the screen where there is supposed to be nothing so that we can now press the screen
    pag.moveTo(347, 241)
    pag.click()
    sleep(0.2)
    # Press the 'filter' button on the top-left part of the screen
    pag.moveTo(459, 233)
    pag.click()
    sleep(1)
    # Press filter by upload time button on the right of the screen
    pag.moveTo(1343, 368)
    pag.click()
    sleep(2)


def enter_video():
    """
    This function sole purpose is to click, it is used specifically to click on a video
    :return: None
    """
    pag.click()
    sleep(1)


def comment():
    """
    Scroll down on the video screen so you can see the comment button
    :return: None
    """
    pag.scroll(-10)
    sleep(0.5)


def go_back():
    """
    Press back arrow button on Chrome's top-left corner to go back to the screen where videos are listed
    :return: None
    """
    pag.moveTo(21, 81)
    pag.click()
    sleep(1)


def video_location():
    """
    Just a function that makes the mouse move to a position where a video should be located
    :return: None
    """
    pag.moveTo(669, 348)


"""
Set up chrome driver options so that the screen you open is in incognito mode, with extensions disabled, and some
    other chrome options. This helps the bot work.
"""
print("LOG:  Setting up Chrome options...")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--incognito")

"""

Open Chrome driver and maximize the window on the screen so that you can see all that's happening and PyAutoGui is 
    easier to use and configure.
    
"""
print("LOG:  Opening Chrome webdriver...")
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_position(0, 0)
driver.maximize_window()

# Login to Google via StackOverFlow
print("LOG:  Logging-In to StackOverFlow")
driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")
sleep(0.5)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
sleep(0.5)
driver.find_element_by_xpath('//input[@type="email"]').send_keys(ACCOUNT_EMAIL)
sleep(1)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
"""

In this part you need to write your Google's account password as I didn't find a way to automatically 
    write it on the screen. Yoy have exactly 10sec to do that (next line of code).

"""
sleep(10)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
delay(5)

# Go to Youtube
print("Going back to YouTube")
driver.get('https://youtube.com')
delay(5)

# Search a for the specified word in Youtube's search bar
print(f"LOG:  Searching for {WORD_TO_SEARCH}")
driver.find_element_by_xpath('//input[@id="search"]').send_keys(WORD_TO_SEARCH)
sleep(1)
driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
delay(6)

# Filter listed videos by upload time and not 'relevance'
print("LOG:  Filtering result by time...")
filter_by_time()

# Comment on the videos. This is the most important part of the code.
print("LOG:  Commenting videos...")
flag_counter = 0
for video_number in range(VIDEOS_TO_COMMENT):
    # It will try the number of times you specified on top
    delay_less(5)
    video_location()
    if flag_counter == 0:
        # If the flag counter is 0 it means it could comment on last video without a problem
        pag.scroll(-6)
    sleep(1)
    enter_video()
    comment()
    flag_counter += 1
    try:
        """
        
        This is the whole part where the bot is going to make the comment in the video it just clicked
        
        """
        driver.find_element_by_id('placeholder-area').click()
        # Send the comment to the input field and press enter to comment
        driver.find_element_by_id('contenteditable-root').send_keys(COMMENT)
        delay_less(5)
        pag.hotkey('command', 'ENTER')
        print(f"LOG:  Success on trial: {video_number}")
        delay_less(5)
        go_back()
        delay_less(5)
        flag_counter = 0
    except:
        """
        
        If there was some error while trying to comment the video the bot will fall here and try to scroll again 
            to see if it finds the comment box or otherwise go back and try next video. This is usual for
            LIVE videos as they don't have a comment section. 
        
        """
        print(f"ERROR: error in trial number: {video_number}")
        comment()
        if flag_counter == 3:
            go_back()
            flag_counter = 0
        sleep(0.5)

# After the bot has finished all trials, it will print it has finished and close chrome driver.
print("""

------------------------
FINISHED!


""")
driver.quit()
