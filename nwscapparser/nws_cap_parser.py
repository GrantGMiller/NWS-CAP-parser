import requests
from lxml import objectify
from lxml.etree import ElementBase
import ast
import json


class NWSCAPParser:
    def __init__(self, raw_cap_xml=None, cap_url=None):
        self.xml = raw_cap_xml
        self.url = cap_url

        if self.xml is None and self.url is None:
            raise Exception('You must pass one parameter "raw_cap_xml" or "cap_url"')

        # placeholders
        self.alert = None
        self.FIPS6 = None
        self.UGC = None
        self.INFO_PARAMS = None

        # init the obj
        self.load()

    def load(self):
        if self.xml is None:
            if self.url:
                self.xml = requests.get(self.url).text
        # print('xml=', self.xml)
        self.alert = objectify.fromstring(self.xml.encode())
        self.FIPS6 = [g.value for g in self.alert.info.area.geocode if str(g.valueName).upper() == 'FIPS6']
        self.FIPS6 = []
        self.UGC = [g.value for g in self.alert.info.area.geocode if str(g.valueName).upper() == 'UGC']
        self.INFO_PARAMS = {}
        [self.INFO_PARAMS.update({p.valueName: p.value}) for p in self.alert.info.parameter]

    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        return getattr(self.alert, name)

    def as_dict(self):
        # return ast.literal_eval(repr(self.alert))
        # return objectify.dump(self.alert)
        # return vars(self.alert)
        ret = DumpNode(self.alert)
        return ret

    def as_json(self):
        return json.dumps(self.as_dict(), indent=2)

    def __repr__(self):
        return '<NWSCAPParser.NWSCAPParser instance (identifier:%s)>' % self.identifier


def DumpNode(node):
    d = {}
    for key, value in vars(node).items():
        if isinstance(value, ElementBase):
            value = DumpNode(value)
        d[key] = value
    if len(d) is 0:
        return str(node)
    return d
