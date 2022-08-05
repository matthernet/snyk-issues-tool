import json
import requests

CLUSTERS_ID = {
    "Org_name1": "ID1",
    "Org_name2": "ID2",
    "Org_name3": "ID3",
    "Org_name4": "ID4",
    "Org_name5": "ID5",
    "Org_name6": "ID6",
}

url = 'https://api.snyk.io/api/v1/reporting/counts/issues/latest'

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'token API_KEY' #Documentation of how to generate an API_KEY https://docs.snyk.io/snyk-api-info/authentication-for-api
}

params = {'groupBy': 'severity'}

def getIssues(cluster, orgs_ids):
    body ="""
  {
    "filters": {
      "orgs": [""" + '"{}"'.format(orgs_ids) + """],
      "severity": [
        "critical",
        "high",
        "medium",
        "low"
      ],
      "types": [
        "vuln",
        "license",
        "configuration"
      ],
      "languages": [
        "node",
        "javascript",
        "ruby",
        "java",
        "scala",
        "python",
        "golang",
        "php",
        "dotnet",
        "swift-objective-c",
        "elixir",
        "docker",
        "linux",
        "dockerfile",
        "terraform",
        "kubernetes",
        "helm",
        "cloudformation"
      ],
      "projects": [],
      "ignored": false,
      "patched": false,
      "fixable": false,
      "isUpgradable": false,
      "isPatchable": false,
      "isPinnable": false,
      "priorityScore": {
        "min": 0,
        "max": 1000
      }
    }
  }"""
    response = requests.post(url, headers = headers, params=params, data = body)
    js = response.json()
    for each in js['results']:
        print("{:<25} {:<10} {:<10} {:<10} {:<10} {:<10}".format(cluster, each['severity']['critical'], each['severity']['high'], each['severity']['medium'], each['severity']['low'], each['count']))

print ("{:<25} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Organization','Critical','High','Medium','Low','Total'))
for cluster, orgs_ids in CLUSTERS_ID.items():
    getIssues(cluster, orgs_ids)
