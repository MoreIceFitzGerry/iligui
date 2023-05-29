from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QProcess
import os

basedir = os.path.normpath(os.path.dirname(__file__))

def run_ilivalidator(settings_list, file):
    # Aufruf-Syntax = java -jar ilivalidator.jar [Options] [file]
    if file == "":
        return ""
    else:
        java_path = os.path.join(basedir, "java11\\bin\\java.exe")
        ilivalidator_path = os.path.join(basedir, "ilivalidator-1.13.2\\ilivalidator-1.13.2.jar") # .jar file path
        xtflog_path = os.path.join(basedir, "data\\result.xtf")
        settings_list.append(f"--xtflog {xtflog_path}") # in any case we want the xtflog
        option_string = " ".join(str(option) for option in settings_list)
        print(f"Option_string: {option_string}")
        process = QProcess()
        process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        # java11\\bin\java.exe -jar ilivalidator-1.13.2/ilivalidator-1.13.2.jar --xtflog errorlog.xtf  interlistests/Testbeispiel_roads/RoadsSimpleWrong.xml
        command = f"{java_path} -jar {ilivalidator_path} {option_string} {file}"
        print(command)

        print("Running process...")
        process.startCommand(command)
        timeout_in_milliseconds = 15000
        if not process.waitForFinished(timeout_in_milliseconds):
        # Handle the timeout as an error
            QMessageBox.critical(None, "Error", "An error occurred. The Ilivalidator has timed out after 15sec. Issues with INTERLIS-1 Files, Paths with Spaces, or Data Size are Possible.")
            QApplication.quit()
        else:
            print("Finished process")
            return xtflog_path
        
        
        # exit_code = process.exitCode() -> ALWAYS GIVES 1 THAT IT FAILED
        
        # if exit_code == 0:
            # print("Process completed successfully")
        # else:
            # print(f"Process exited with code {exit_code}")
            # QMessageBox.critical(None, "Error", "An error occurred. Ilivalidator Timed out. Possible Issues with INTERLIS-1 Files or Paths with Spaces.")
            # QApplication.quit()

        

        # setProcessChannelMode(QProcess::MergedChannels) will merge the output channels.
        # Various programs write to different outputs.
        # Some use the error output for their normal logging, some use the "standard" output, some both. Better to merge them.
        ####output= process.readAllStandardOutput()
        #error = process.readAllStandardError()

        # The programs output is in byte and needs to be decoded with the standard utf8.
        # It's possible some characters may have been output by the program that don't conform,
        # so we ingore these errors and simply pass what can be.
        ####textoutput = bytes(output).decode("utf8", "ignore")
        #####print(textoutput)
        #####return textoutput

if __name__ == "__main__":
    settings_list = []
    file = "C:/Users/mauri/Desktop/Aufgabe 1/sz_av_feusisberg_DMCH_nok.itf"
    run_ilivalidator(settings_list, file)
