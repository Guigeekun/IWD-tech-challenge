import crud.storyCrud as crd
import story_parser as parser
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    stories = parser.parse_csv(os.getenv('CSV_PATH'))
    

if __name__ == "__main__":
    main()
