import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def start_ilivalidator(file_path):
    print("Filepath: " + file_path)
    ilivalidator_path = "ilivalidator-1.13.2/ilivalidator-1.13.2.jar" # .jar file path
    subprocess.Popen(["java11\\bin\java.exe", "-jar", ilivalidator_path, file_path], shell=True)

# Vor Neuinstallation, Kontrolle ob Java11 im lokalen Ordner installiert.
def checkinstall_cwdjava():
    if os.path.isdir("java11") is False:
        message = tk.Label(root, text="Java not installed in cwd. Please wait while we install it.")
        message.pack()
        try:
            import jdk
            cwd = os.getcwd()
            jdk.install(version='11', jre=True, path=cwd)
            os.rename("jdk-11.0.18+10-jre", "java11")
            checkinstall_cwdjava()
        except:
            message = tk.Label(root, text="Java could not be installed in cwd.")
            message.pack()
            return False
    else:
        message = tk.Label(root, text="Java has been installed in cwd.")
        message.pack()
        return True

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        start_ilivalidator(file_path)

def main():
    if checkinstall_cwdjava() is True:
        button = tk.Button(root, text="Select file", command=select_file)
        button.pack()
    else:
        root.destroy()

root = tk.Tk()
main()
root.mainloop() 