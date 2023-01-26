import crud.storyCrud as storyCrud
import crud.epicCrud as epicCrud
import crud.workflowCrud as workflowCrud
import story_parser as parser
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('SHORTCUT_API_URL')
token = os.getenv('SHORTCUT_ACCESS_TOKEN')
workflow_name = os.getenv('SHORTCUT_WORKFLOW')

global_headers = {
    'content-type': 'application/json',
    'Shortcut-Token': token
}


def main():
    stories = parser.parse_csv(os.getenv('CSV_PATH'))
    for story in stories:
        storyCrud.match_epic(url, global_headers, story)

        match_state(url, global_headers, story, workflow_name)

        print(story)

        # Adding stories
        storyCrud.add_story(
            url, global_headers, story["description"], story["state_id"], story["epic_id"], story["blocked by"])






def match_state(url: str, global_headers: dict, story: dict, workflow_name: str):
    workflow = workflowCrud.get_workflow_by_name(url, global_headers, workflow_name)
    for state in workflow['states']:
        print(state['name'])
        print(story['status'])
        if(story['status']==state['name']):
            story["state_id"] = state['id']
            return story
        # Note that if the status doesn't exist it won't create the attribute and thus crash later
    


if __name__ == "__main__":
    main()
