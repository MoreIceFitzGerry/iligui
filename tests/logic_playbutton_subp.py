import os
import subprocess

def run_ilivalidator(file_path):
    print("Filepath: " + file_path)
    ilivalidator_path = "ilivalidator-1.13.2/ilivalidator-1.13.2.jar" # .jar file path
    #process = subprocess.Popen(["java11\\bin\java.exe", "-jar", ilivalidator_path, file_path], shell=True)
    process = subprocess.Popen(["java11\\bin\java.exe", "-jar", ilivalidator_path, file_path], stdout=subprocess.PIPE)

    # Wait for the JAR file to finish and get its output
    output, error = process.communicate()
    # Decode the output bytes to a string and append it to the QPlainTextEdit widget
    outputtext = output.decode('utf-8')
    return outputtext

# Vor Neuinstallation, Kontrolle ob Java11 im lokalen Ordner installiert.
def checkinstall_cwdjava():
    if os.path.isdir("java11") is False:
        try:
            import jdk
            cwd = os.getcwd()
            jdk.install(version='11', jre=True, path=cwd)
            os.rename("jdk-11.0.18+10-jre", "java11")
            checkinstall_cwdjava()
        except:
            return False
    else:
        return True
