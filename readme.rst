Get NWS CAP alerts for your area
================================
Note: these values are updated every 2 minutes.
The NWS server uses cache-control headers and timeouts to optimize response times.

::

    MY_STATE = 'NC'
    cap = NWSCAPParser('http://alerts.weather.gov/cap/{}.php?x=1'.format(MY_STATE))

    for ID, entry in cap.entries.items():
        print('################################')
        print('ID=', ID)
        print('entry.id=', entry.id)
        print('entry=', entry)

        print('entry.severity=', entry.severity)
        print('entry.urgency=', entry.urgency)
        print('entry.certainty=', entry.certainty)

        print('entry.status=', entry.status)
        print('entry.msgType=', entry.msgType)
        print('entry.category=', entry.category)
        print('entry.areaDesc=', entry.areaDesc)

Output

::

    ################################
    ID= https://alerts.weather.gov/cap/wwacapget.php?x=NC125F5E87CC18.BeachHazardsStatement.125F5E94C080NC.MHXCFWMHX.517dbba3998ca8105cf4c357df8d60e2
    entry.id= https://alerts.weather.gov/cap/wwacapget.php?x=NC125F5E87CC18.BeachHazardsStatement.125F5E94C080NC.MHXCFWMHX.517dbba3998ca8105cf4c357df8d60e2
    entry= <CAPEntry: {'id': 'https://alerts.weather.gov/cap/wwacapget.php?x=NC125F5E87CC18.BeachHazardsStatement.125F5E94C080NC.MHXCFWMHX.517dbba3998ca8105cf4c357df8d60e2', 'updated': '2020-08-17T11:10:00-04:00', 'published': '2020-08-17T11:10:00-04:00', 'author': {'name': 'w-nws.webmaster@noaa.gov'}, 'title': 'Beach Hazards Statement issued August 17 at 11:10AM EDT until August 17 at 8:00PM EDT by NWS', 'link': '', 'summary': '...BEACH HAZARDS STATEMENT REMAINS IN EFFECT UNTIL 8 PM EDT THIS EVENING... * WHAT...Dangerous rip currents. * WHERE...The beaches north of Cape Hatteras. * WHEN...Until 8 PM EDT this evening. * IMPACTS...Rip currents can sweep even the best swimmers away'}>
    entry.severity= Moderate
    entry.urgency= Expected
    entry.certainty= Likely
    entry.status= Actual
    entry.msgType= Alert
    entry.category= Met
    entry.areaDesc= Hatteras Island; Northern Outer Banks
    ################################
    ID= https://alerts.weather.gov/cap/wwacapget.php?x=NC125F5E86E924.BeachHazardsStatement.125F5E94C080NC.AKQCFWAKQ.d59a4d6449e2c689d8dd9b1209db835a
    entry.id= https://alerts.weather.gov/cap/wwacapget.php?x=NC125F5E86E924.BeachHazardsStatement.125F5E94C080NC.AKQCFWAKQ.d59a4d6449e2c689d8dd9b1209db835a
    entry= <CAPEntry: {'id': 'https://alerts.weather.gov/cap/wwacapget.php?x=NC125F5E86E924.BeachHazardsStatement.125F5E94C080NC.AKQCFWAKQ.d59a4d6449e2c689d8dd9b1209db835a', 'updated': '2020-08-17T05:29:00-04:00', 'published': '2020-08-17T05:29:00-04:00', 'author': {'name': 'w-nws.webmaster@noaa.gov'}, 'title': 'Beach Hazards Statement issued August 17 at 5:29AM EDT until August 17 at 8:00PM EDT by NWS', 'link': '', 'summary': '...BEACH HAZARDS STATEMENT REMAINS IN EFFECT THROUGH THIS EVENING... * WHAT...A high risk of rip currents. * WHERE...In Virginia, Virginia Beach. In North Carolina, Eastern Currituck County. * WHEN...From 8 AM EDT this morning through this evening.'}>
    entry.severity= Moderate
    entry.urgency= Expected
    entry.certainty= Likely
    entry.status= Actual
    entry.msgType= Alert
    entry.category= Met
    entry.areaDesc= Eastern Currituck

