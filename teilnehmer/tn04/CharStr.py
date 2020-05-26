#!/usr/bin/python3

log = [

"03/22 08:51:06 WARNING:.....mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available." ,
"03/22 08:51:06 INFO   :....mailbox_register: mailbox allocated for rsvp-udp" ,
"03/22 08:51:06 TRACE  :..entity_initialize: interface 9.37.65.139, entity for rsvp allocated and" ,
]

for zeile in log:
    aktion = zeile[15:21]
    if aktion == "WARNING":
        print("Warining")
    if aktion == "INFO":
        print("Info")
    if aktion == "TRACE":
        print("Trace")


a = "Hallo,"
b = "Wie geht es dir?"

print(len(b))


c = b[4:8]
d = a[3:5]

print(c +" " + d)

