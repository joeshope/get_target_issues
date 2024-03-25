import requests
import argparse
import json

parser = argparse.ArgumentParser(description='org: input the name of your org, project: provide the name of your project, token: input your snyk token')
parser.add_argument('--org')
parser.add_argument('--project')
parser.add_argument('--token')

args = parser.parse_args()
org_name = args.org
org_slug = "-".join(org_name.split())
project_name = args.project
snyk_token = args.token

org_response = requests.get('https://api.snyk.io/rest/orgs?version=2024-03-12', headers={'Authorization': f'Token {snyk_token}'})
org_res = org_response.json()
od = org_res['data']

def orgid():
    for i in od:
        if org_slug.lower() in i['attributes']['slug']:
            return i['id']
        
proj_response = requests.get(f'https://api.snyk.io/rest/orgs/{orgid()}/projects?version=2024-03-12', headers={'Authorization': f'Token {snyk_token}'})
pr = proj_response.json()
pd = pr['data']

def projid():
    for i in pd:
        if project_name.lower() in i['attributes']['name']:
            return i['id']

issue_response = requests.get(f'https://api.snyk.io/rest/orgs/{orgid()}/issues?version=2024-03-12&scan_item.id={projid()}&scan_item.type=project', headers={'Authorization': f'Token {snyk_token}'})
ir = issue_response.json()

json_obj = json.dumps(ir, indent=4)
with open('results.json', "w") as f:
    f.write(json_obj)