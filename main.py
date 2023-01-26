import crud.storyCrud as storyCrud
import story_parser as parser
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv('SHORTCUT_API_URL')
workflow_name = os.getenv('SHORTCUT_WORKFLOW')

global_headers = {
    'content-type': 'application/json',
    'Shortcut-Token': os.getenv('SHORTCUT_ACCESS_TOKEN')
}


def main():
    stories = parser.parse_csv(os.getenv('CSV_PATH'))
    handle_adding_stories(stories)
    handle_adding_block_relation(stories)


def handle_adding_stories(stories: list):
    for story in stories:
        # Getting epic id or creating it
        storyCrud.match_epic(url, global_headers, story)
        # Getting state id
        storyCrud.match_state(url, global_headers, story, workflow_name)
        # Adding stories
        # Storing the id, will be convenient for handling the blocking
        story["id"] = storyCrud.add_story(
            url, global_headers, story["description"], story["state_id"], story["epic_id"])["id"]


def handle_adding_block_relation(stories: list):
    # Handling blocked_by
    # we're relooping so the stories can be put in any order in the CSV file
    # if we wouldn't reloop, we couldn't refer to a story before creating it
    # i just don't think we should be dependant from the order of the stories in the CSV
    for story in stories:
        if(story['blocked by']):
            story2 = storyCrud.get_story_by_name(
                url, global_headers, story['blocked by'])
            rel = storyCrud.create_relation(
                url, global_headers, story['id'], story2['id'], "blocks")


if __name__ == "__main__":
    main()
