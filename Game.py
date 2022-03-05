from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import dictionary as Vocab
import main

def ConnectRoom(driver):
    code = input("Enter game room code.")
    # code = "qvec"

    try:
        driver.get(main.url + code)
        sleep(1)
        # find name field
        LoginAsGuest = driver.find_element(by=By.CLASS_NAME, value="styled")
        LoginAsGuest.click()
        # LoginAsGuest.clear()
        LoginAsGuest.send_keys(chr(8) * 10 + main.BOT_NAME + "\n")
        sleep(5)

    except:
        print("Game not available, Restart App.")
        exit(1)

def isGameRunning(driver):
    try:
        isRunning = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div/header")
        return isRunning.isDisplayed()
    except:
        print("Game Running Fail")
        # always assume game is running for safety
        return True

def JoinGame(driver):
    #wait for game to be available
    Running = isGameRunning(driver)
    while (not Running):
        sleep(0.5)
        Running = isGameRunning(driver)
    #Join game button
    joinButton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[1]/div[1]/button")
    joinButton.click()
    PlayGame(driver)

def PlayGame(driver):
    sleep(10)
    Dict = Vocab()
    while(isGameRunning(driver)):
        prompt = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[2]/div").text
        print(prompt)

