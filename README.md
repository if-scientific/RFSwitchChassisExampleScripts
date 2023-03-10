# RFSwitchChassisVisaDemo
This repository houses example python scripts to show how to connect to the RFSwitchChassis through Visa. 

You will need to install python, pyvisa-py, as well as the needed visa libraries for your operating system. 
<br>
The VISA instrument address will be "TCPIP::**DEVICE_IP_ADDRESS**::9000::SOCKET."
<br>
The GPIB instrument address will be "GPIB0::**DEVICE_GPIB_ADDRESS**::INSTR"
<br>
To change any of the above configurations go to **DEVICE_IP_ADDRESS**:3000\config.
<br>
**Please make sure to indicate that the read and write termination characters are set to '\n'**

Any changes done on the GPIB or VISA connection will be shown on the web page hosted at **DEVICE_IP_ADDRESS**:3000

**We found some issues using the GPIB commands, so even though it works, we advice for the usage of the VISA connection flow.**
# Commands
There are 10 main commands that can be sent to the device. 

Those commands can either be a query or an order. A query will end with a "?". A query tells the device to return a value to the user. The result of the Query will be returned with a prefix of "[RESULT]: " on the GPIB interface. 

## *IDN?
### Parameters
No parameters needed.

### Description
This command can only be a query type  

The *IDN? command will return a string with the following format "IF Scientific, RF switch chassis, $DEVICE_SERIAL_NUMBER, $DEVICE_VERSION."

Where the $DEVICE_SERIAL_NUMBER is the serial number of the device, and the $DEVICE_VERSION has the version number of the software on the device.


## RESet/RES/*RST
### Parameters
No parameters needed.

### Description
This command can be run as a query to get the status of the command. It will return True if it passes, and False if it fails.

This command can be used to reset any errors indicated by the error led on the front panel. It can also be used as a singular command to disconnect all the switches. (It does both)


## INST:RESETSWitch/INST:RESETSW
### Parameters
Can take either one or zero parameters.

The only parameter to pass is the bay number. If no bay number is specified, the device will reset all the bays/switches.

### Description
This command is used to reset the switches without deleting the configuration.

## INST:SWitchON/INST:SWON
### Parameters
This command takes multiple parameters. Each parameter specifies the bay number and the switch number. 

The format is the following: BAYNUMBER!SWITCHNUMBER

### Description
This command can be used to activate multiple switches on in a single command.


## INST:SWitchOFF/INST:SWOFF
### Parameters
This command takes multiple parameters. Each parameter specifies the bay number and the switch number. 

The format is the following: BAYNUMBER!SWITCHNUMBER

### Description
This command can be used to de-activate multiple switches on in a single command.

## INST:TYPEswitch/INST:TYPE
### Parameters
This command takes two parameters. The first is a string indicating the type of switch to create. There are three options possible.

The second parameter is the bay number which should be a number between 1 and 12 (inclusive).

#### Switch types
**SP6T** This is the parameter for creating a single pole / 6 throws switch. <br>
**SPST** This is the parameter for creating a quad single pole / single throws switch.<br>
**empty** This is the parameter for no switch.

### Description
This command can be run as a query to get the status of the command. It will return True if it passes, and False if it fails.

This command is needed before trying to switch anything on. As it informs the device of state of each bay that it has. 


## INST:TURNswitch/INST:TURN
### Parameters
This command takes three parameters. The first parameter is a number indicating the bay number. This number should be between 1 and 12.

The second parameter is the switch number. If the switch type is empty. This command won't work. If it is set to SPST, you can use [1,4]. And if it is set to SP6T, you can use [1,6].

The third paramter is a boolean integer indicating the connection value. 0 indicates a disconnect. 1 indicates a connection.

### Description
This command can be run as a query to get the status of the command. It will return True if it passes, and False if it fails.

This command simply switches the individual switches to a specfic value.

## INST:INSTRumentApplication/INST:INSTRA
### Parameters
This command can take 0 to 1 paramters.

The paramter here would be the value to set to the field **Instrument Application**.

If no parameter is passed, and this command is not a query. It won't do anything. 

### Description
This command can be run as a query to get the value of the **Instrument Application** field. If passed with a parameter for the field value, it will return the paramter. Otherwise, it will return the current value.


## INST:CONFigurationType/INST:CONFT
### Parameters
This command can take 0 to 1 paramters.

The paramter here would be the value to set the field **Configuration Type**.

If no parameter is passed, and this command is not a query. It won't do anything. 

### Description
This command can be run as a query to get the value of the **Configuration Type** field. If passed with a parameter for the field value, it will return the paramter. Otherwise, it will return the current value.

Please note that you can add new lines to this field by adding "[NL]" in the parameter where a new line is needed.

## INST:IP
### Parameters
This command can take 1 parameter. This parameter is th ip address to switch the device into.

### Description
This command is used to check or change the ip address exclusively. 

If ran as a query, the command will return the current IP address of the machine. 

If not, the device will set its ip address to the parameter given if possible. If the ip address change was successful, the machine will restart. 
