from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import dictionary as vocab
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
        # check top if the prompt says they are waiting
        isRunning = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div/header")
        visible = isRunning.is_displayed()
        # print(visible)
        if " 0s" in isRunning.text or not visible:
            return True
        else:
            return False
    except:
        print("Game Running Fail")
        # always assume game is running for safety
        return True


def JoinGame(driver):
    print("Joining Game!")
    # wait for game to be available
    running = isGameRunning(driver)
    # Join game button
    joinButton = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[1]/div[1]/button")
    joinButton.click()
    sleep(0.5)
    while (not running):
        sleep(0.2)
        running = isGameRunning(driver)
    PlayGame(driver)


def isPlayerTurn(driver):
    try:
        isPlayer = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[2]/div[2]")
        isVisible = isPlayer.is_displayed()
        return isVisible
    except:
        print("PlayerTurn Fail")
        # always assume game is not your turn for safety
        return False

def PlayGame(driver):
    dict = vocab.Dict()
    # dict.makeLists()
    print("Lists Created")
    textfield = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
    while isGameRunning(driver):
        while isPlayerTurn(driver):
            print("PLAYING!")
            prompt = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[2]/div").text
            word = dict.findAnswer(prompt.lower())
            print(word)

            # if realistic
            sleep(0.6)
            for ch in word:
                textfield.send_keys(ch)
                sleep(0.05)
            textfield.send_keys('\n')

            # if CHEATER
            # textfield.send_keys(word + "\n")
            sleep(0.5)
