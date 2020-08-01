# Import libraries
import pyautogui as pag
import time
import sys
import webbrowser as wb

# GLOBAL VARIABLES
ACCOUNT_EMAIL = "goobadoops@gmail.com"
ACCOUNT_PASSWORD = "ScoobyDoPapa1"
ENTER_VIDEO_X = 472
ENTER_VIDEO_Y = 275


def open_youtube():
    pag.moveTo(251, 84)
    pag.click()
    pag.click()
    pag.write("youtube.com")
    pag.hotkey("ENTER")


def delay(n):
    time.sleep(n)


def sign_in():
    pag.moveTo(1390, 129)
    pag.click()
    pag.click()
    delay(3)
    pag.moveTo(728, 421)
    pag.click()
    pag.write(ACCOUNT_EMAIL)
    pag.moveTo(856, 626)
    pag.click()
    # NOT FINISHED


def search(text):
    pag.moveTo(637, 122)
    pag.click()
    pag.click()
    pag.write(text)
    pag.hotkey("ENTER")
    delay(1)


def filter_by_time():
    pag.moveTo(342, 193)
    pag.click()
    delay(1)
    pag.moveTo(1201, 321)
    pag.click()
    delay(2)


def video_location():
    pag.moveTo(472, 275)


def enter_first_video():
    video_location()
    pag.click()
    delay(1)


def enter_video():
    pag.click()
    delay(1)


def comment(text):
    for _ in range(2):
        pag.scroll(-10)
        delay(0.5)
    delay(1)
    pag.moveTo(66, 0)
    ###
    pag.moveTo(222, 489)
    pag.click()
    delay(0.5)
    pag.write(text)
    pag.moveTo(923, 527)
    delay(1)
    # pag.click()


def go_back():
    pag.moveTo(21, 80)
    pag.click()
    delay(1)


def comment_clickable():
    x, y, z = pag.pixel(203, 181)
    if x == y == z:
        return False
    return True


def clickable():
    x, y, z = pag.pixel(203, 181)
    if x == y == z:
        return False
    return True


# NOT WORKING
# open_youtube()
# delay(5)
# sign_in()

# print("\nIMPORTANT: do not use special characters or 'ñ' or that keys yet\n")
# search_word = input("Type the exact word you want to search for:  ")
# search(search_word)
# filter_by_time()
# enter_first_video()
# comment('hola')
# go_back()
# video_location()
# while True:
#     pag.scroll(-6)
#     delay(1)
#     if clickable():
#         enter_video()
#         comment('hola')
#     else:
#         continue


while True:
    posXY = pag.position()
    print(posXY, pag.pixel(posXY[0], posXY[1]))
    if posXY[0] == 0:
        break
