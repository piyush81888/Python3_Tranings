"""
Get data from web_server.log

then

Extract
IP
DATE
URL

then

keep extracted data in dictionary

Expected Dictionary:
----------------
{
    0: ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    1: ('123.123.123.123','26/Apr/2000','http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF'),
    2: ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    3: ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    4: ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    5: ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/')
}
----------------
"""