#!/usr/bin/env python

import subprocess
import json

data=subprocess.check_output(["docker", "logs", "jet-nginx-HttpTest", "--tail", "1"])
j = json.loads(data)
log_keys = j.keys()

expected_fields = ['geoip_country_code', 'geoip_city', 'geoip_country_name', 'geoip_timezone']
for f in expected_fields:
    assert f in log_keys
