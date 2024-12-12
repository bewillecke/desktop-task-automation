import pyautogui as pag
from time import sleep

# definição da função para clicar na imagem
def click_image(img):
    image = 'imgs/' + img + '.png'
    sleep(1)
    img_location = pag.locateOnScreen(image, confidence=0.9)
    return pag.click(img_location)