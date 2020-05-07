# NWS CAP Parser (Python3)

A Python module to make parsing National Weather Service (NWS) alerts simple.

##  Common Alerting Protocol (CAP)

The NWS publishes weather alerts and advisories in the CAP format via Atom feeds. More information - and a 
full list of US feeds - can be found on the NWS CAP [home page](http://alerts.weather.gov/).

## Module Details

### NWSCAPParser

The nwscapparser module exports a single class, `NWSCAPParser`. Pass a string containing the
XML from a CAP alert as the only param to the initialization call:
```python
from nwscapparser3 import NWSCAPParser
filname = 'cap.IL124CA04A2F50.SevereThunderstormWarning.xml'
src = open(filname, mode='r').read()
cap = NWSCAPParser(src)
for ID, entry in cap.entries.items():
    print('ID=', ID, ', entry=', entry)
```

You can also pass a url to `NWSCAPParser()`
```python
from nwscapparser3 import NWSCAPParser
cap = NWSCAPParser('http://alerts.weather.gov/cap/nc.php?x=1')
for ID, entry in cap.entries.items():
    print('ID=', ID, ', entry=', entry)

    # you can access attributes of the event
    print('entry.status=', entry.status)
    print('entry.msgType=', entry.msgType)
```

### us_states

The module also exports a dictionary `us_states` with keys that are two-letter US state abbreviations and values 
that are full state names, to aid in iterating through the feeds offered by the NWS, which are published by state 
abbreviations. For example, the CAP feed for Arizona (AZ) can be accessed at the URL `http://alerts.weather.gov/cap/az.php?x=1`.
