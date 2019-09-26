import os
from os.path import join, dirname
from dotenv import load_dotenv
import urllib.request,json
from requests import get, post

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Getting the api key
api_key = os.getenv('PIVOTAL_TOKEN')

# Getting the base url
base_url = 'https://www.pivotaltracker.com/services/v5/{}'

# Getting the headers
headers =  { 'X-TrackerToken': api_key }

# Getting the slack webhook
webhook = os.getenv('WEBHOOK_URL')

def get_projects():
    url = base_url.format('projects')
    response = get(url, headers = headers)
    return response.json()

def get_unscheduled_bug_cards(project_ids):
    combined_list = []
    for project_id in project_ids:
        url = base_url.format('projects/'+str(project_id)+'/stories?with_story_type=bug')
        response = get(url, headers = headers)
        combined_list.extend(response.json())
        len(combined_list)
    return combined_list

def post_to_bug_tracker_channel(list_of_bugs, state_of_bugs):
    slack_acctachments = { "text": state_of_bugs, "attachments": list_of_bugs}
    payload = json.dumps(slack_acctachments, default=obj_dict)
    return post(webhook, data=payload)

def obj_dict(obj):
    '''
    Map object to a python dictionary
    '''
    return obj.__dict__