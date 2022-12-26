# RFSwitchChassisVisaDemo
This repository houses example python scripts to show how to connect to the RFSwitchChassis through Visa. 
# Commands
There are 6 main commands that can be sent to the device. 

Those commands can either be a query or an order. A query will end with a "?". A query tells the device to return a value to the user. The result of the Query will be returned with a prefix of "[RESULT]" on the GPIB interface. 

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

The paramter here would be the value to set the field {Instrument Application}.

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
This command takes 0 paramters.

### Description
This command should only be run as a query. 

This command will return the current static ip address set to the machine.