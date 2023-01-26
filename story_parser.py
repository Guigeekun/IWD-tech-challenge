import csv

# doc > doc/story_parser.md

# Parses the file at given path and return a tab containing each line


def parse_csv(path: str):
    with open(path) as file:
        reader = csv.reader(file)
        stories = []
        attributes = next(reader)
        # Iterating over rows
        for row in reader:
            story = {}
            # Iterating over attributes
            for i in range(len(attributes)):
                story[attributes[i]] = row[i]
            stories.append(story)
        # Note that we do not need to close file with "with" syntax
    return stories

# Output example
# [
#   {"attribute1": "smth", "attribute2": "smthelse"},
#   {"attribute1": "smth2", "attribute2": "smthelse2"},
#   {"attribute1": "smth3", "attribute2": "smthelse3"}
# ]
