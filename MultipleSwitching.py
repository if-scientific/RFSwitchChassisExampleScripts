import pyvisa
import time

# Get the resource and connect to it
rm =pyvisa.ResourceManager()
a = rm.open_resource("TCPIP::192.168.1.228::9000::SOCKET",write_termination= "\n", read_termination="\n")

# Print the ID of the device
print("This is the device's identification string: ",a.query("*IDN?"))

# Reset all the connections
a.write("*RST")

# Specify the switches currently existing
a.query("INST:TYPEswitch? SPDT, 1")
a.query("INST:TYPEswitch? SPDT, 2")
a.query("INST:TYPEswitch? SPDT, 3")
time.sleep(1)

# Switch on (bay,switch) : (1,1), (2,2), (3,3) 
a.query("INST:SWON? 1!1 , 2!2 ,3!3")
time.sleep(1)

# Resets all the switches while maintaining the configuration
a.query("INST:RESETSW?") 
time.sleep(1)

# Switch on (bay,switch) : (1,1), (1,2), (1,3) 
a.query("INST:SWON? 1!1,1!2,1!3")
time.sleep(1)

# Switch off (bay,switch) : (1,1), (1,2), (1,3) 
a.query("INST:SWOFF? 1!1,1!2,1!3")
time.sleep(1)

# Resets specified switch while maintaining the configuraiton 
a.query("INST:RESETSW? 1")
time.sleep(1)

# Reset all the connections
a.write("*RST")