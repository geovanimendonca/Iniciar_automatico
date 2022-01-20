import pyautogui, time 

#pyautogui.alert('alerta', 'Titulo','ok')
pyautogui.FAILSAFE = True # Se mover o mouse o programa finaliza
#time.sleep (3)
#print(pyautogui.position())

pyautogui.PAUSE = 2
# Abrir chrome Point(x=466, y=744)
pyautogui.click(466, 744)
# Digitar site
pyautogui.write('gmail.com')
pyautogui.press('enter')

# Abrir nova aba Point(x=269, y=17)
pyautogui.click(269, 17)
pyautogui.write('youtube.com')
pyautogui.press('enter')

# Abrir nova aba Point(x=507, y=18)
pyautogui.click(507, 18)
pyautogui.write('web.whatsapp.com')
pyautogui.press('enter')

# Arrastar aba Point(x=595, y=15) -> Point(x=2053, y=349)
pyautogui.moveTo(595,15)
pyautogui.dragTo(2053, 349, 2, button = 'left')

# Abrir Spotify
pyautogui.click(173,746)
time.sleep(10)
# Musicas curtidas Point(x=125, y=255)
pyautogui.click(125,255)
time.sleep(3)
# Play Point(x=298, y=418)
pyautogui.click(298, 418)

# Abrir pasta Point(x=220, y=745)
#pyautogui.click(220,745)
# Clicar Point(x=326, y=154)
#pyautogui.click(821,154)
# digitar C:\Codes -> enter
#pyautogui.write('C:\Codes')
#pyautogui.press('enter')

# Abrir vscode Point(x=418, y=743)
pyautogui.click(418, 743)

#pyautogui.alert('', '', 'Finalizar')
