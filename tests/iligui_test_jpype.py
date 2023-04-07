import jpype

# Start the JVM
jpype.startJVM()

# Create a Java object from the script
script_class = jpype.JClass("ilivalidator-1.13.2/ilivalidator-1.13.2.jar)   
script = script_class()

# Call a method on the Java object
result = script.run()

# Print the result
print(result)

# Shutdown the JVM
jpype.shutdownJVM()