import os
import jdk

# Vor Neuinstallation, Kontrolle ob Java11 im lokalen Ordner installiert.
if os.path.isdir("java11") is True:
    pass
else:
    cwd = os.getcwd()
    jdk.install(version='11', jre=True, path=cwd)
    os.rename("jdk-11.0.18+10-jre", "java11")

#OPEN VALIDATOR
#os.system('cmd /k "java -jar ilivalidator-1.13.2/ilivalidator-1.13.2.jar"')

from tkinter import filedialog, Tk
root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(title='Please select a file to validate')
print("Filename: " + filename)

path = "java11\\bin\java.exe"
# SELECT ITF FILE TO VALIDATE IN VALIDATOR
os.system(f'cmd /k "{path} -jar ilivalidator-1.13.2/ilivalidator-1.13.2.jar {filename}"')
#os.system(f'cmd /k "java -jar ilivalidator-1.13.2/ilivalidator-1.13.2.jar {filename}"')

"""
import subprocess
subprocess.Popen(["jre/jdk-11.0.18+10-jre/bin/java.exe", 'ilivalidator-1.13.2/ilivalidator-1.13.2.jar'])
"""