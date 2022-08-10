## AUGMENTER SES CONNECTIONS LINKEDIN !
## L'INTERET DE CE PROGRAMME EST DE SE CONNECTER A UN MAXIMUM DE PERSONNE SUR LINKEDIN
## IL Y'A A PEU PRES UNE PERSONNE SUR 4 QUI ACCEPTE LA CONNECTIONS LINKEDIN
## VOUS POUVEZ LARGEMENT DEPASSER LES 500 CONNECTIONS EN UNE SEMAINE


import pyautogui
import keyboard

##TOUTES LES VALEURS X ET Y DEPENDENT DES PIXELS DE VOTRE ORDINATEURS ET VARIENT
##D'UN ORDINATEUR A L'AUTRE IL FAUDRAIT AINSI AJUSTER LES VALEURS EN FONCTION DE VOTRE PC

y=855

def Confirm():      ##### CONFIRMER L'ABONNEMENT
    pyautogui.sleep(0.3)
    pyautogui.click(930, 280)
    pyautogui.sleep(0.3)

def Next():         ###PASSER A LA PAGE SUIVANTE
    pyautogui.click(890,550)
    pyautogui.sleep(3)

def Click():
    if keyboard.is_pressed('1'):   ##EXECUTER LE CODE SI L'UTILISATEUR APPUIS SUR 1
        pyautogui.click(y,280)  ## CLIQUER SUR LA 1er CONNECTION
        Confirm()
        pyautogui.click(y, 390) ## CLIQUER SUR LA 2e CONNECTION
        Confirm()
        pyautogui.click(y, 500) ## 3e etc...
        Confirm()
        pyautogui.click(y, 610)
        Confirm()
        pyautogui.click(y, 720)
        Confirm()
        pyautogui.click(y, 830)
        Confirm()
        pyautogui.scroll(-30) ##DESCENDRE TOUT EN BAS DE LA PAGE
        pyautogui.click(y, 215)
        Confirm()
        pyautogui.click(y,325)
        Confirm()
        pyautogui.click(y,435)
        Confirm()
        Next()


while True:
    Click()

