from dotenv import load_dotenv
import os
from ui.ui import init_ui

if __name__ == "__main__":
    load_dotenv()

    url = os.getenv('SHORTCUT_API_URL')
    workflow_name = os.getenv('SHORTCUT_WORKFLOW')
    default_path = os.getenv('DEFAULT_PATH')

    global_headers = {
        'content-type': 'application/json',
        'Shortcut-Token': os.getenv('SHORTCUT_ACCESS_TOKEN')
    }
    init_ui(url, global_headers, workflow_name, default_path)