#!/usr/local/bin/python3
# 
# Copyright 2017 Ed Lawford <ed.lawford@db.com>
#
# Command-line control for pfSense firewall rules
# Uses FauxAPI: https://github.com/ndejong/pfsense_fauxapi
# 

import pprint, sys
from fauxapi_lib import FauxapiLib

# Configuration
api_hostname = "firewall.digitician.com.au"
api_key = "fwcontrol"
api_secret = "triumph-fascism-gutter"
rule_prefix = "KinderControl"

# check args exist
if(len(sys.argv) < 4):
    print('usage: ' + sys.argv[0] + ' <host> <apikey> <apisecret> <rule category> <enable|disable>')
    sys.exit(1)

# config
fauxapi_host=sys.argv[1]
fauxapi_apikey=sys.argv[2]
fauxapi_apisecret=sys.argv[3]
rule_category=sys.argv[4]
rule_action=sys.argv[5]

FauxapiLib = FauxapiLib(fauxapi_host, fauxapi_apikey, fauxapi_apisecret, debug=False)

# Get the current set of filters
filters = FauxapiLib.config_get('filter')

# Iterate through and find 'KinderControl' rules, find enable/disable
i = 0
for rule in filters['rule']:
    if (rule['descr'].startswith(rule_prefix)):
        if (rule_category in rule['descr']):
            if (rule_action == "enable"):
                del filters['rule'][i]['disabled']
                print ("Rule {} enabled.".format(rule['descr']))
            elif (rule_action == "disable"):
                filters['rule'][i]['disabled'] = ""
                print ("Rule {} disabled.".format(rule['descr']))
    i=i+1

# Push the config back to pfSense
filters = FauxapiLib.config_set(filters, 'filter')

# Reload the config
FauxapiLib.send_event("filter reload")