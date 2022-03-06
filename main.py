import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import Game


class Main:

    def __init__(self):
        self.BOT_NAME = ""
        self.ROOM_CODE = None
        self.PATH = ''
        self.url = "https://jklm.fun/"
        self.WORDS_TYPE = None
        self.LANG = None

    def main(self):
        sg.theme('Default1')
        layout = [
            [sg.Text('Desired Username:')],
            [sg.Text('', size=(0, 0)), sg.InputText()],
            [sg.Text('BombParty Room Code:')],
            [sg.Text('', size=(0, 0)), sg.InputText()],
            [sg.Text('ChromeDriver Location:')],
            [sg.Text('', size=(0, 0)), sg.InputText(), sg.FileBrowse()],
            [sg.Text('Select Language:')],
            [sg.Radio('English', "RADIO1", default=True), sg.Radio('French', "RADIO1", default=False)],
            [sg.Text('Select Word Type:')],
            [sg.Radio('All', "RADIO2", default=True), sg.Radio('Impressive', "RADIO2", default=False),
                sg.Radio('Simple', "RADIO2", default=False)],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window('BombParty Bot 1.0', layout, element_justification='c')
        event, values = window.read()
        window.close()

        self.BOT_NAME = values[0]

        self.ROOM_CODE = values[1].lower()

        self.PATH = values[2]

        if values[3]:
            self.LANG = 1
        else:
            self.LANG = 2

        if values[5]:
            self.WORDS_TYPE = 1
        elif values[6]:
            self.WORDS_TYPE = 2
        else:
            self.WORDS_TYPE = 3

        print(self.WORDS_TYPE, self.LANG)


        driver = webdriver.Chrome(executable_path=self.PATH)
        Game.ConnectRoom(driver, self.url, self.ROOM_CODE, self.BOT_NAME)
        iframe = 0
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(iframe))

        while (True):
            # try:
            if (not Game.isGameRunning(driver)):
                Game.JoinGame(driver, self.WORDS_TYPE, self.LANG)
            else:
                sleep(2)
        # except:
        #     print("Something Went Wrong, Restart.")
        #     continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Main().main()
