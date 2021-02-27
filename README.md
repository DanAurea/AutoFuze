# AutoFuze

AutoFuze is a small toolkit created to provide a way to communicate with ECU embedded in car. 
It's allow to do some pentest through several standard used in AutoSar framework. 
Everything is written in Python to provide an easy way to automate and do testing of ECU.

## Protocols

Following protocols are implemented and should provide a way to fuzz ECU. Especially UDS and XCP that could be
useful for flashing software, update NVM and other embedded parameters.

* UDS
    - Ethernet (DoIP)
    - CAN
* XCP
    - USB
    - Ethernet
    - SxI
    - CAN
* SOME/IP
* OBD
* USB
* CAN

## Disclaimer

This toolkit hasn't been done to provide a high performance library but a readable one with focus
on maintainability.

If any feature is requested for fuzzing purpose or for testing purpose of ECU based on AutoSar framework then 
don't hesitate to make a ticket.