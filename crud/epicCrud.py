
import requests
import json


def get_epics(url: str, global_headers: dict):
    r = requests.get(url + 'epics', headers=global_headers)
    return r.json()


def create_epic(url: str, global_headers: dict, name: str):
    payload = {"name": name}
    # Note that we need to json.dumps the payload
    r = requests.post(url + 'epics', data=json.dumps(payload), headers=global_headers)
    return r.json()
