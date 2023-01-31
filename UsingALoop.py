import pyvisa
import time


# Get the resource and connect to it
rm =pyvisa.ResourceManager()
a = rm.open_resource("TCPIP::192.168.1.228::9000::SOCKET",write_termination= "\n", read_termination="\n")

# Reset the device
a.write("*RST")

# For each bay in the device
for j in range(1,13):
    # Set it to a SP6T switch and return the result of the command
    print(a.query("INST:TYPEswitch? SP6T, "+str(j)))
    for i in range(1,7):
        # For each switch in each bay, turn it on
        a.write("INST:TURN "+str(j)+","+str(i)+",1")

# Sleep for 5 seconds
time.sleep(5)

# Reset all the switches to off
a.write("RES")
