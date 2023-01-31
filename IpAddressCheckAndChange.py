import pyvisa
import time

# Get the resource and connect to it
rm =pyvisa.ResourceManager()
a = rm.open_resource("TCPIP::192.168.1.228::9000::SOCKET",write_termination= "\n", read_termination="\n")

print("This is the Device's current static Ip address: " + a.query("INST:IP?"))

ipAddress = input("IP address to set: ")

print("Setting the device's ip address to "+ ipAddress+ " device will restart if the ip address is valid")
a.write("INST:IP "+ ipAddress)