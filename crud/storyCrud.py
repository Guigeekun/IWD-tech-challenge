import requests
import json
import crud.epicCrud as epicCrud


def add_story(url: str, global_headers: dict, name: str, status_id: int, epic_id: int, blocked_by: str):
    payload = {
        "name": name,
        "workflow_state_id": status_id,
        "epic_id": epic_id
    }
    # Note that we need to json.dumps the payload
    r = requests.post(url + 'stories', data=json.dumps(payload), headers=global_headers)
    print(r.text)
    return r.json()

# this function adds the epic_id attribute to the story and create the epic if needed
def match_epic(url: str, global_headers: dict, story: dict):
    # Matching epic
    # I could cache the epics instead of rechecking them from the backend
    # Would be more optimized
    epics = epicCrud.get_epics(url, global_headers)
    epic_exists = False
    for epic in epics:
        if (epic['name'] == story['epic']):
            story['epic_id'] = epic['id']
            epic_exists = True
            break
    # The epic doesn't exist, let's create it
    if (not epic_exists):
        epic = epicCrud.create_epic(url, global_headers, story['epic'])
        story['epic_id'] = epic['id']
    return story