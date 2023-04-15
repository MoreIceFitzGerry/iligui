import os
from PyQt5.QtCore import QProcess

def run_ilivalidator(file_path):
    print("Filepath: " + file_path)
    ilivalidator_path = "ilivalidator-1.13.2/ilivalidator-1.13.2.jar" # .jar file path

    process = QProcess()
    process.setProcessChannelMode(QProcess.MergedChannels)
    process.start("java11\\bin\java.exe", ["-jar", ilivalidator_path, file_path])
    process.waitForFinished()

    # setProcessChannelMode(QProcess::MergedChannels) will merge the output channels.
    # Various programs write to different outputs.
    # Some use the error output for their normal logging, some use the "standard" output, some both. Better to merge them.
    output= process.readAllStandardOutput()
    error = process.readAllStandardError()

    # The programs output is in byte and needs to be decoded with the standard utf8.
    # It's possible some characters may have been output by the program that don't conform,
    # so we ingore these errors and simply pass what can be.
    textoutput = bytes(output).decode("utf8", "ignore")
    return textoutput

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
