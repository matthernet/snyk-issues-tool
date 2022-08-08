# snyk-issues-tool

<img align="right" src="https://snyk.io/style/asset/logo/snyk-print.svg">

CLI tool that uses the Snyk API to get orgs and issue count sort by severity

The tools require a valid Snyk **API_KEY**, please read the documentation about it [Authentication for API](https://docs.snyk.io/snyk-api-info/authentication-for-api)

## Examples

First you will need to run ```get-orgs.py``` to get all the names and IDs of the orgs that have access to it:
``` bash
# python3 get-orgs.py

Your Snyk orgs names and IDs are:
Org_name1 : 1234abcd-1234-abcd-1234-123456abcdef
Org_name2 : abcd1234-abcd-1234-abcd-abcdef123456
Org_name3 : 1234abcd-1234-abcd-1234-123456abcdef
Org_name4 : abcd1234-abcd-1234-abcd-abcdef123456
Org_name5 : 1234abcd-1234-abcd-1234-123456abcdef
Org_name6 : abcd1234-abcd-1234-abcd-abcdef123456
```


Modify the ```get-issues.py``` file and add the names and IDs from the orgs that you want to get the issues count in the ```CLUSTERS_ID``` list:
```
CLUSTERS_ID = {
    "Org_name1" : "1234abcd-1234-abcd-1234-123456abcdef",
    "Org_name2" : "abcd1234-abcd-1234-abcd-abcdef123456",
    "Org_name3" : "1234abcd-1234-abcd-1234-123456abcdef",
    "Org_name4" : "abcd1234-abcd-1234-abcd-abcdef123456",
    "Org_name5" : "1234abcd-1234-abcd-1234-123456abcdef",
    "Org_name6" : "abcd1234-abcd-1234-abcd-abcdef123456",
}
```

Run ```get-issues.py``` and get the issues count sort by organization and severity:
``` bash
# python3 get-issues.py

Organization              Critical   High       Medium     Low        Total     
Org_name1                 1          22         33         44         100
Org_name2                 2          33         44         55         134
Org_name3                 3          44         55         66         168
Org_name4                 4          55         66         77         202
Org_name5                 5          66         77         88         236
Org_name6                 6          77         88         99         270
```

