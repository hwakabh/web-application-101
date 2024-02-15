import json

import requests
# Suppressing InsecureRequestWarning with urllib3
import urllib3
urllib3.disable_warnings()


def fetch_token() -> str:
    url = VCENTER_REST_BASE_URL + '/rest/com/vmware/cis/session'
    h = {
        "Content-Type": "application/json",
        "vmware-api-session-id": "null"
    }

    res = requests.post(
        url=url,
        auth=(USERNAME, PASSWORD),
        headers=h,
        verify=False
    )
    return json.loads(res.text).get('value')



def get_esxi_name_list(token: str) -> list:
    url = VCENTER_REST_BASE_URL + '/rest/vcenter/host'
    h = {
        "Content-Type": "application/json",
        "vmware-api-session-id": token
    }

    res = requests.get(
        url=url,
        headers=h,
        verify=False
    )

    esxi_names = []
    for h in json.loads(res.text).get('value'):
        esxi_names.append(h.get('name'))

    return esxi_names


def clean_up_session(token: str) -> int:
    url = VCENTER_REST_BASE_URL + '/rest/com/vmware/cis/session'
    h = {
        "Content-Type": "application/json",
        "vmware-api-session-id": token
    }

    res = requests.delete(
        url=url,
        headers=h,
        verify=False
    )
    return res.status_code


# Setup credentials
VCENTER_REST_BASE_URL = 'https://resvc.haas.local'
USERNAME = 'administrator@vsphere.local'
PASSWORD = 'VMware1!'

# Call APIs
print('>>> Fetching session token to call API')
TOKEN = fetch_token()

print('>>> Listing up ESXi hosts')
vmhosts = get_esxi_name_list(token=TOKEN)
for h in vmhosts:
    print(h)

print('>>> Terminating session')
rc = clean_up_session(token=TOKEN)
if rc == 200:
    print('Success')
else:
    print('Failed')
