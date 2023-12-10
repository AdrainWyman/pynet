#!/usr/bin/env python
import ipdb
from getpass import getpass
from napalm import get_network_driver

device = {
    "hostname": "arista9-napalm.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

# Standard NAPALM
driver = get_network_driver("eos")
napalm_conn = driver(**device)
napalm_conn.open()

# Stage a full configuration
ipdb.set_trace()
napalm_conn.load_replace_candidate(filename="arista9.cfg")

# View differences
print(napalm_conn.compare_config())

# Commit with revert timer
napalm_conn.commit_config(revert_in=180)

# We should now have a pending commit
print(napalm_conn.has_pending_commit())

# Immediately cancel the pending commit
napalm_conn.rollback()

# Should be no pending commits at this point
print(napalm_conn.has_pending_commit())

napalm_conn.close()
