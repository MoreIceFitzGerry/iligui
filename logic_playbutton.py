from PyQt6.QtCore import QProcess

def run_ilivalidator(settings_list, file):
    # Aufruf-Syntax = java -jar ilivalidator.jar [Options] [file]
    if file == "":
        return ""
    else:
        
        java_path = "java11\\bin\\java.exe"
        ilivalidator_path = "ilivalidator-1.13.2\\ilivalidator-1.13.2.jar" # .jar file path
        xtflog_path = "result.xtf"
        settings_list.append(f"--xtflog {xtflog_path}") # in any case we want the xtflog
        option_string = " ".join(str(option) for option in settings_list)
        print(f"Option_string: {option_string}")
    
        process = QProcess()
        process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        # java11\\bin\java.exe -jar ilivalidator-1.13.2/ilivalidator-1.13.2.jar --xtflog errorlog.xtf  interlistests/Testbeispiel_roads/RoadsSimpleWrong.xml
        command = f"{java_path} -jar {ilivalidator_path} {option_string} {file}"
        print(command)
        process.startCommand(command)
        print("Running process...")
        process.waitForFinished()
    
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
        return xtflog_path
