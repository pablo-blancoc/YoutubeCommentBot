# YoutubeCommentBot

A bot that will enter your youtube account and will try to comment on every video that is listed after searching for a particular word.

### The bot works in the next way:
  1. Enters your StackOverFlow account using Selenium, so it's important to note that you need to have a StackOverFlow account before starting.
##### NOTE: you need to introduce your passcode manually in this part
  2. Now that the bot has entered you Google Account somehow, it now goes to YouTube still logged in to your account.
  3. Inside Youtube it will now search for a specific word you provide and then start to comment on videos.
##### NOTE: There are some videos where the bot can't comment (lives for example) so it will just go back and try next video
##### NOTE: The bot uses PyAutoGui sometimes, which means that it needs accesibility permission on your computer
##### NOTE: Also because the bot uses PyAutoGui, it needs exact coordinates of your screen to click on some buttons, be sure to update them before using it
    
### Important considerations:

The bot uses Selenium's Chromedriver. The steps you need to follow to correctly install it in your **MacOS** system are as follows:
1. Install brew package manager from: https://brew.sh/
2. Install chromedriver from brew: ```brew cask install chromedriver```
3. Navigate to the chromedriver: ```cd /usr/local/Caskroom/chromedriver/<version of your driver>```
4. Add permissions to it: ```xattr -d com.apple.quarantine chromedriver```
5. Change some configurations in it: <br>
  ```vi chromedriver```<br>
  ```/cdc_```<br>
  Now you'll need to change cdc_ for dog_<br>
  Change all the letter in between the two ```_``` for the same number of 'e' letters (or any other character)<br>
  To save and exit press ESC and then type ```:wq``` + ENTER<br>
  Now run chromedriver to see you made all changes correcty: ```./chromedriver```. It should say: "ChromeDriver was started successfully." Stop it with CTRL+C.
6. Now you can run the code. Be sure to debug it first as it uses exact screen coordinates so it may not work for your screen as it is.
<br>
<br>
That's it. Now it should work perfectly.
