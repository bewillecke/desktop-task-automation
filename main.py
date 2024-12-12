# realização dos imports
import pyautogui as pag
import os
from time import sleep
from dotenv import load_dotenv
from search_image_function import click_image

load_dotenv()

# pegar os valores de email e senha para login no Google e no Notion
EMAIL_GOOGLE = os.getenv('EMAIL_GOOGLE')
SENHA_GOOGLE = os.getenv('SENHA_GOOGLE')
EMAIL_NOTION = os.getenv('EMAIL_NOTION')
SENHA_NOTION = os.getenv('SENHA_NOTION')

# abrir o google chrome
click_image('chrome_icon')
pag.hotkey('ctrl', 'shift', 'n')
pag.hotkey('ctrl', 'l')
pag.write('google', interval=0.05)
pag.press('space', 2)
pag.press('enter')
sleep(2)
click_image('google_icon')

# abrir o globo.com
pag.hotkey('ctrl', 't')
pag.hotkey('ctrl', 'l')
pag.write('globo.com', interval=0.05)
pag.press('space', 2)
pag.press('enter')
sleep(3)

# abrir o gmail.com e realizar o login
pag.hotkey('ctrl', 't')
pag.hotkey('ctrl', 'l')
pag.write('gmail.com')
pag.press('space', 2)
pag.press('enter')
sleep(4)
click_image('gmail_login_button')
sleep(4)
pag.write(EMAIL_GOOGLE, interval=0.05)
pag.press('enter')
sleep(4)
pag.write(SENHA_GOOGLE, interval=0.05)
pag.press('enter')
sleep(4)

# abrir o Google Calendar e realizar o login
pag.hotkey('ctrl', 't')
pag.hotkey('ctrl', 'l')
pag.write('google calendar', interval=0.05)
pag.press('space', 2)
pag.press('enter')
sleep(1)
click_image('calendar_icon')
sleep(3)
click_image('calendar_login_button')
sleep(3)

# abrir a agenda no notion
pag.hotkey('ctrl', 't')
pag.hotkey('ctrl', 'l')
pag.write('notion', interval=0.05)
pag.press('space', 2)
pag.press('enter')
sleep(2)
click_image('notion_icon')
sleep(3)
click_image('translate_button')
sleep(0.5)
click_image('notion_login_button')
sleep(4)
pag.write(EMAIL_NOTION, interval=0.05)
pag.press('enter')
sleep(2)
pag.write(SENHA_NOTION, interval=0.05)
pag.press('enter')
sleep(3)

# abrir spotify e selecionar playlist lofi
click_image('spotify_icon')
sleep(2)
click_image('search_field')
pag.write('lofi')
pag.press('enter')
sleep(2)
click_image('lofi_beats_icon')
sleep(2)
click_image('lofi_chill_icon')
sleep(2)
click_image('play_button')
sleep(0.5)
click_image('volume_button')
sleep(3)

# abrir o Visual Studio Code
pag.press('win')
sleep(1)
pag.write('vscode')
sleep(0.5)
click_image('vscode_icon')