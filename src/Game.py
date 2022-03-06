from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import src.dictionary as vocab

GAME_URL = "https://jklm.fun/"


class Game:

    def __init__(self, driver, name, room_code, word_type, lang):
        self.driver = driver
        self.name = name
        self.code = room_code
        self.url = GAME_URL
        self.type = word_type
        self.lang = lang

    def connectRoom(self):
        try:
            self.driver.get(self.url + self.code)
            sleep(1)
            # find name field
            loginAsGuest = self.driver.find_element(by=By.CLASS_NAME, value="styled")
            loginAsGuest.click()
            # LoginAsGuest.clear()
            loginAsGuest.send_keys(chr(8) * 10 + self.name + "\n")

            iframe = 0
            WebDriverWait(self.driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it(iframe))
        # General Except statement, kinda ass.
        except:
            # something went wrong badly
            print("Game not available, Restart App.")
            exit(1)

    def isGameRunning(self):
        try:
            # check top if the prompt says they are waiting
            # Top of the html says "Wait for x players to start"
            # or "Starting in xs" seconds. HTML hidden if the game isnt running
            isRunning = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div/header")
            visible = isRunning.is_displayed()
            # print(visible)
            if " 0s" in isRunning.text or not visible:
                return True
            else:
                return False
        except:
            #
            print("Game not available, Restart App.")
            # always assume game is running to make program not crash
            return True

    def joinGame(self):
        # wait for game to be available
        running = self.isGameRunning()
        # Join game button
        joinButton = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[1]/div[1]/button")
        joinButton.click()
        sleep(0.5)
        while (not running):
            sleep(0.2)
            running = self.isGameRunning()
        self.playGame()

    def isPlayerTurn(self):
        try:
            isPlayer = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[2]/div[2]")
            isVisible = isPlayer.is_displayed()
            return isVisible
        except:
            print("PlayerTurn Fail")
            # always assume game is not your turn for safety
            return False

    def playGame(self):
        dict = vocab.Dict(self.lang)
        dict.makeLists()
        # Bottom text to enter in worDS
        textfield = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
        while self.isGameRunning():
            while self.isPlayerTurn():
                prompt = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[2]/div").text

                # DO NOT HAVE HANGING IF STATEMENTS
                if self.type == 1:
                    word = dict.findAnswer(prompt.lower())
                elif self.type == 2:
                    word = dict.findAnswerImp(prompt.lower())
                else:
                    word = dict.findAnswerSimple(prompt.lower())

                # if realistic
                sleep(0.3)
                for ch in word:
                    textfield.send_keys(ch)
                    sleep(0.02)
                textfield.send_keys('\n')

                # if CHEATER
                # textfield.send_keys(word + "\n")
                # need to find a way to wait until its not your turn anymore, sometimes 0.5s is too little or too much.
                sleep(0.5)
