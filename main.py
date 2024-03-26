import requests
import argparse
import json

parser = argparse.ArgumentParser(description='org: input the name of your org, target: provide the name of your project, token: input your snyk token')
parser.add_argument('--org')
parser.add_argument('--target')
parser.add_argument('--token')

args = parser.parse_args()
org_name = args.org
org_slug = "-".join(org_name.split())
target_name = args.target
snyk_token = args.token

org_response = requests.get('https://api.snyk.io/rest/orgs?version=2024-03-12', headers={'Authorization': f'Token {snyk_token}'})
org_res = org_response.json()
od = org_res['data']

def orgid():
    for i in od:
        if org_slug.lower() in i['attributes']['slug']:
            return i['id']
        
target_response = requests.get(f'https://api.snyk.io/rest/orgs/{orgid()}/targets?version=2024-03-12', headers={'Authorization': f'Token {snyk_token}'})
tr = target_response.json()
td = tr['data']

def targetid():
    for i in td:
        if target_name in i['attributes']['display_name']:
            return i['id']
        
project_response = requests.get(f'https://api.snyk.io/rest/orgs/{orgid()}/projects?target_id={targetid()}&version=2024-03-12', headers={'Authorization': f'Token {snyk_token}'})
pr = project_response.json()
pd = pr['data']

def projid():
    projList = []
    for i in pd:
        projList.append(i['id'])
    return projList

def issuedata():
    all_content = []
    oid = orgid()
    for i in projid():
        issue_count = requests.post('https://api.snyk.io/v1/reporting/counts/issues/latest?groupBy=severity', headers={'Content-Type': 'application/json', 'Authorization': f'Token {snyk_token}'}, json={"filters": {"orgs": [f"{oid}"], "projects": [f"{i}"]}})
        ic = issue_count.json()
        issue_response = requests.get(f'https://api.snyk.io/rest/orgs/{orgid()}/issues?version=2024-03-12&scan_item.id={i}&scan_item.type=project', headers={'Authorization': f'Token {snyk_token}'})
        ir = issue_response.json()
        all_content.append(ic)
        all_content.append(ir)
    return all_content

with open('results.json', 'a') as outfile:
    json.dump(issuedata(), outfile, indent=4)
