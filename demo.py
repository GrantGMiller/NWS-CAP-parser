import sys
from pprint import pprint

from nwscapparser import NWSCAPParser


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
    pprint(alert.as_json())


if __name__ == '__main__':
    # first command line arg is assumed to be a full URL to a CAP
    import requests

    if len(sys.argv) > 1:
        cap_url = sys.argv[1]
        response = requests.get(cap_url)
        src = response.text
    # testing
    else:
        filepath = r'cap.IL124CA04A2F50.SevereThunderstormWarning.xml'
        with open(filepath, 'rt') as file:
            src = file.read()

    alert = NWSCAPParser(src)
    print(alert)
    test_basic_fields(alert)
    test_dict_dump(alert)
    test_json_dump(alert)
