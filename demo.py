import sys
from pprint import pprint

from nwscapparser3 import NWSCAPParser


def test_basic_fields(alert):
    print('---- basic fields ----')
    print(alert.identifier)
    print(alert.info.effective)
    print(f'{len(alert.FIPS6)} FIPS6 codes:{alert.FIPS6}')
    print(f'{len(alert.UGC)} UGC codes:{alert.UGC}')
    print(f'{len(alert.INFO_PARAMS)} INFO_PARAMS:{alert.INFO_PARAMS}')


def test_dict_dump(alert):
    print('---- dict dump ----')
    pprint(alert.as_dict())


def test_json_dump(alert):
    print('---- json dump ----')
    print(alert.as_json())


if __name__ == '__main__':
    # first command line arg is assumed to be a full URL to a CAP
    import requests

    def TestLocalXML():
        print('--Testing parse of a local XML file---')

        filepath = r'cap.2020-05-07T14_12_00.xml'
        with open(filepath, 'rt') as file:
            src = file.read()

        cap = NWSCAPParser(rawXML=src)

        for ID, entry in cap.entries.items():
            print('ID=', ID, ', entry=', entry)

    def TestRemoteURL():
        print('--Testing parse of a remote file---')

        cap = NWSCAPParser(url='http://alerts.weather.gov/cap/nc.php?x=1')

        for ID, entry in cap.entries.items():
            print('ID=', ID, ', entry=', entry)

    TestLocalXML()
    TestRemoteURL()