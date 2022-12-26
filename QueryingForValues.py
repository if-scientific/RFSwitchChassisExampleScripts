import pyvisa


# Get the resource and connect to it
rm =pyvisa.ResourceManager()
a = rm.open_resource("TCPIP::192.168.1.228::9000::SOCKET",write_termination= "\n", read_termination="\n")

# Reset all the connections
a.write("*RST")

# Print the configuration type field
print("This is the confguration type field: ",a.query("INST:CONFT?"))

# Print the instrument application field
print("This is the instrument application field: ",a.query("INST:INSTRA?"))

# Print the static ip address
print("This is the device's static ip address: ",a.query("INST:IP?"))


# Print the ID of the device
print("This is the device's identification string: ",a.query("*IDN?"))