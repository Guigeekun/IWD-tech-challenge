# Story parser

## Input

- path: path of the csv file, you can get it from the env var `CSV_PATH`

## Output

Returns a tab of objects each representing a story
```json
[
  {'description': 'Create Stories', 'status': 'to do', 'epic': 'Code', 'blocked by': 'Create Shortcut Token API'}, 
  {'description': 'Read Shortcut API documentation', 'status': 'in progress', 'epic': 'Spike', 'blocked by': 'Read & Understand tech challenge'}, 
  {'description': 'Tech challenge accepted!', 'status': 'done', 'epic': 'Spike', 'blocked by': ''}, 
  ...
]
```

## Notes

### Why are you not using a package ?
The parser can technically parse `anything`, not only stories, this is a generic code that I could have imported from a `package` instead of doing it myself. For such a short piece of code, I prefer doing it myself rather than importing **to limit the amount of packages**.

### Why are you not typing the output like the input
As the name of the file is `story_parser` I would have liked to type the output, in general I would have used [pydantic](https://docs.pydantic.dev/). In this case **this would be very overkill** and takes some time so let's not.