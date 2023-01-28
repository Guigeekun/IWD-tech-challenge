## Calling the API

For that we are using [Requests](https://pypi.org/project/requests/), a simple python lib that acts liek curl

```py
import requests

def get_stories(url: str, global_headers: dict):
    r = requests.get(url + 'stories', headers=global_headers)
    return r.json()
```

## Handling epic matching

The CSV file contains some `epic name` instead of an `epic id`, thus we need to match the name with an id

For that we:
- fetch the epics with `epicCrud.get_epics(url, global_headers)` 
- check if one got the same `epic name`
  - if yes we keep the `id` in the story object
  - if not we create the epic with `epicCrud.create_epic(url, global_headers, story['epic'])`

### What does it imply
If you have some epic with the names in you Shortcut app already, it won't recreate them and add the stories to these.

The script won't create epics with the same names.

If you wanna check that the script is correctly creating the epics, make sure to delete the already existing ones on your Shortcut app (or rename them)

*Kinda the same goes for matching state*