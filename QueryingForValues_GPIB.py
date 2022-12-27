import pyvisa
import time

# Get the resource and connect to it
rm =pyvisa.ResourceManager()
print(rm.list_resources())

a = rm.open_resource("GPIB0::7::INSTR", read_termination="\n",write_termination= "\n",send_end =True,query_delay = 2)
a.chunk_size =120
# Print the ID of the device
print("This is the device's identification string: ",a.query("*IDN?"))
time.sleep(2)
# Reset all the connections
# Only switch on this bay if switch creation passes (Switch type:SPST -> only 4 switches possible)
if a.query("INST:TYPEswitch? SPST, 2")=="True":
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

