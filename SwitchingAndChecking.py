import pyvisa
import time

# Get the resource and connect to it
rm =pyvisa.ResourceManager()
a = rm.open_resource("TCPIP::192.168.1.228::9000::SOCKET",write_termination= "\n", read_termination="\n")

# Print the ID of the device
print("This is the device's identification string: ",a.query("*IDN?"))

# Reset all the connections
a.write("*RST")

# Only switch on this bay if switch creation passes (Switch type:SPDT -> only 4 switches possible)
if a.query("INST:TYPEswitch? SPDT, 2")=="True":
    # This switches switch 2 on bay 2.
    succeeded = a.query("INST:TURN? 2,2,1")
    print("Switching [bay:2,switch:2,1] succeeded: "+ succeeded)
    # sleep for a second
    time.sleep(1)

    # This switches switch 5 on bay 2. However, this will fail. Check switch type created above...
    succeeded = a.query("INST:TURN? 2,5,1")
    print("Switching [bay:2,switch:5,1] succeeded: "+ succeeded)
    # sleep for a second
    time.sleep(1)

# Reset the switch on bay 2 (This will also turn off all the switches on that bay)
a.write("INST:TYPEswitch? empty, 2")

