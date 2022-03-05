from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Game

BOT_NAME = "EsanBOT"
PATH = 'C:\Program Files\ChromeDriver\chromedriver.exe'
url = "https://jklm.fun/"

def main():
    driver = webdriver.Chrome(executable_path=PATH)
    Game.ConnectRoom(driver)

    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(by=By.XPATH, value="/html/body/div[2]/div[4]/div[1]/iframe"))

    playing = False
    while (True):
        # try:
            if (not Game.isGameRunning(driver) or not playing):
                Game.JoinGame(driver)
                playing = True
            else:
                Game.PlayGame(driver)
                playing = False
        # except:
        #     print("Something Went Wrong, Restart.")
        #     continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

