import requests
from lxml import objectify
from lxml.etree import ElementBase


def DumpNode(node):
    d = {}
    for key, value in vars(node).items():
        if isinstance(value, ElementBase):
            value = DumpNode(value)
        d[key] = value
    if len(d) == 0:
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

        for entryTag in xmlObj.entry:
            entryObj = CAPEntry(xmlObj, entryTag)
            if entryObj.id not in self.entries:
                self.entries[entryObj.id] = entryObj


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

    def __iter__(self):
        for key, value in DumpNode(self).items():
            yield key, value

    def dict(self):
        ret = {}
        for key, value in DumpNode(self).items():
            ret[key] = value
        return ret

    def __str__(self):
        return f'<CAPEntry: {DumpNode(self.entry)}>'


if __name__ == '__main__':
    MY_STATE = 'NC'
    cap = NWSCAPParser('http://alerts.weather.gov/cap/{}.php?x=1'.format(MY_STATE))
    import json

    for ID, entry in cap.entries.items():
        print('################################')
        print('ID=', ID)
        print('entry.id=', entry.id)
        print('entry=', entry)
        print('entry.title=', entry.title)

        print('entry.severity=', entry.severity)
        print('entry.urgency=', entry.urgency)
        print('entry.certainty=', entry.certainty)

        print('entry.status=', entry.status)
        print('entry.msgType=', entry.msgType)
        print('entry.category=', entry.category)
        print('entry.areaDesc=', entry.areaDesc)

        print('dict()=', json.dumps(entry.dict()))
