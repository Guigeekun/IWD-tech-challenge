import requests
import json
import crud.epicCrud as epicCrud


def get_workflows(url: str, global_headers: dict):
    r = requests.get(url + 'workflows', headers=global_headers)
    return r.json()


def get_workflow_by_name(url: str, global_headers: dict, workflow_name: str):
    workflows = get_workflows(url, global_headers)
    for workflow in workflows:
        if (workflow['name'] == workflow_name):
            return workflow
