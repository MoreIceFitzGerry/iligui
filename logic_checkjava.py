import os

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
