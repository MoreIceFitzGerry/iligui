from PyQt6.QtCore import QProcess

def run_ilivalidator(Options, file):
    print("Command: " + Options + " " + file)
    ilivalidator_path = "ilivalidator-1.13.2/ilivalidator-1.13.2.jar" # .jar file path

    process = QProcess()
    process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
    if len(Options) == 0:
        process.start("java11\\bin\java.exe", ["-jar", ilivalidator_path, file])
    else:
        process.start("java11\\bin\java.exe", ["-jar", ilivalidator_path, Options, file])
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