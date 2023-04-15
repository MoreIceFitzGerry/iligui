import jpype

# Start the JVM with the desired JRE
jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.home=java11")

# Load the Jar file
jar_path = "ilivalidator-1.13.2\ilivalidator-1.13.2.jar"
jpype.JClass("java.net.URLClassLoader").getSystemClassLoader().addURL(jpype.java.net.URL("file:" + jar_path))

# Find the main class of the Jar file
manifest = jpype.JClass("java.util.jar.JarFile")(jar_path).getManifest()
main_class = manifest.getMainAttributes().getValue("Main-Class")

# Run the main class with input arguments
#args = ["input1", "input2", "input3"]
args = ["tests\RoadsSimple.xml"]
jpype.JClass(str(main_class)).main(args)

# Shut down the JVM
jpype.shutdownJVM()
