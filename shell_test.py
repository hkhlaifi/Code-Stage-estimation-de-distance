#Objectif : écrire des commandes shell depuis le code python 
#et retourner l'output

import os
import subprocess
import sys

input = 'python /home/samaudensiel/Desktop/Aziz/test_divers/programme_filepath'
stream = os.popen('echo Return output')
output = stream.read()

subprocess.run(["python", "/home/samaudensiel/Desktop/Aziz/test_divers/programme_filepath/image_path.py", "/home/samaudensiel/Desktop/Aziz/test_divers/programme_filepath/train_image/000026.png"])

#result = subprocess.run([sys.executable, "-c", "print('ocean')"], capture_output=True, text=True)
#print("stdout", result.stdout)
#print("stdout", result.stderr)