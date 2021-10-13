#générer fichier txt avec le nom des fichiers

import os
import subprocess
import sys

subprocess.run(["echo filename > outfile.txt"], shell=True)
ma_cmd = ["find", "Data", "-name", "\*.png", "-printf", "%f\n", ">>", "outfile.txt"]
with open('outfile.txt','a') as f:
    subprocess.run(ma_cmd, stdout=f)

#os.system("find Data -name \*.png -printf '"%f\n"' >> outfile.txt")
#subprocess.call("sed -i 'i/filename' outfile.txt", shell=True) | une alternative

#>>outfile.txt
#sed -i 'i/filename' outfile.txt ou echo "filename" >>outfile.txt (génère fichier de sortie)
#find nom_du_path -name \*.png -printf "%f\n"

#cmd = 'find Data -name \*.png -printf "%f\n" >> outfile.txt'
