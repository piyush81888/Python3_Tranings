"""
Get data from web_server.log

then

Extract
IP
DATE
URL

then

keep extracted data in list of tuples

Expected list:
----------------
[
    ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    ('123.123.123.123','26/Apr/2000','http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF'),
    ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/')
]
----------------
"""