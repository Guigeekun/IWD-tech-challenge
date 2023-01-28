import requests
import json
import crud.epicCrud as epicCrud
import crud.workflowCrud as workflowCrud
import story_parser as parser


def add_story(url: str, global_headers: dict, name: str, status_id: int, epic_id: int):
    payload = {
        "name": name,
        "workflow_state_id": status_id,
        "epic_id": epic_id
    }
    # Note that we need to json.dumps the payload
    r = requests.post(url + 'stories', data=json.dumps(payload),
                      headers=global_headers)
    print("Story Added !")
    return r.json()


def get_stories(url: str, global_headers: dict):
    r = requests.get(url + 'stories', headers=global_headers)
    return r.json()


def get_story_by_name(url: str, global_headers: dict, name: str):
    r = requests.get(
        url + "search/stories", params={'query': 'title:' + name}, headers=global_headers)
    return r.json()['data'][0]


def create_relation(url: str, global_headers: dict, story1_id: int, story2_id: int, relation: str):
    payload = {
        "object_id": story1_id,
        "subject_id": story2_id,
        "verb": relation
    }
    r = requests.post(url + 'story-links',
                      headers=global_headers, data=json.dumps(payload))
    print("Relation Created !")
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


def match_state(url: str, global_headers: dict, story: dict, workflow_name: str):
    workflow = workflowCrud.get_workflow_by_name(
            url, global_headers, workflow_name)
    for state in workflow['states']:
        if (story['status'] == state['name']):
            story["state_id"] = state['id']
            return story
        # Note that if the status doesn't exist it won't create the attribute and thus crash later

def handle_stories(url: str, global_headers: dict, workflow_name: str, path: str):
    stories = parser.parse_csv(path)
    handle_adding_stories(url, global_headers, workflow_name, stories)
    handle_adding_block_relation(url, global_headers, stories)


def handle_adding_stories(url: str, global_headers: dict, workflow_name: str, stories: list):
    for story in stories:
        # Getting epic id or creating it
        match_epic(url, global_headers, story)
        # Getting state id
        match_state(url, global_headers, story, workflow_name)
        # Adding stories
        # Storing the id, will be convenient for handling the blocking
        story["id"] = add_story(
            url, global_headers, story["description"], story["state_id"], story["epic_id"])["id"]


def handle_adding_block_relation(url: str, global_headers: dict, stories: list):
    # Handling blocked_by
    # we're relooping so the stories can be put in any order in the CSV file
    # if we wouldn't reloop, we couldn't refer to a story before creating it
    # i just don't think we should be dependant from the order of the stories in the CSV
    for story in stories:
        if(story['blocked by']):
            story2 = get_story_by_name(
                url, global_headers, story['blocked by'])
            create_relation(
                url, global_headers, story['id'], story2['id'], "blocks")