import datetime

import requests
from lxml import objectify
from lxml.etree import ElementBase
import pytz
import json
from dateutil.parser import parse


def DumpNode(node):
    d = {}
    for key, value in vars(node).items():
        if isinstance(value, ElementBase):
            value = DumpNode(value)
        d[key] = value
    if len(d) is 0:
        return str(node)
    return d


class NWSCAPParser:
    def __init__(self, url=None, rawXML=None):
        self.rawXML = rawXML
        self.url = url

        if self.rawXML is None and self.url is None:
            raise Exception('You must instantiate this object with either "url" or "rawXML"')

        self.entries = {
            # str(id): CAPEntryObj,
        }

        self.Update()

    def Update(self):
        xmlString = self.rawXML or requests.get(self.url).text
        # print('xmlString=', xmlString)
        xmlObj = objectify.fromstring(xmlString.encode())

        nowDT = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
        print('nowDT=', nowDT)

        for entry in xmlObj.entry:
            entry = CAPEntry(xmlObj, entry)
            if entry.id not in self.entries:
                self.entries[entry.id] = entry


class CAPEntry:
    def __init__(self, xmlObj, entry):
        self.xmlObj = xmlObj
        self.entry = entry

    def __getattr__(self, item):
        try:
            res = getattr(self.entry, item)
            return res
        except:
            pass

        res = self.entry.find(f'{item}')
        if res:
            return res
        else:
            return self.entry.find(f'{{{self.xmlObj.nsmap["cap"]}}}{item}')

    def __str__(self):
        return f'<CAPEntry: {DumpNode(self.entry)}>'


if __name__ == '__main__':

    cap = NWSCAPParser('http://alerts.weather.gov/cap/nc.php?x=1')

    for ID, entry in cap.entries.items():
        print('ID=', ID)
        print('entry.id=', entry.id)
        print('entry=', entry)
        print('entry.status=', entry.status)
        print('entry.msgType=', entry.msgType)
        print('entry.category=', entry.category)
        print('entry.areaDesc=', entry.areaDesc)
