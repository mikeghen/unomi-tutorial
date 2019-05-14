import requests

"""
Make a request to Unomi to create a profile with ID = 10
"""
r = requests.post('http://localhost:8181/cxs/profiles/',
auth=('karaf','karaf'),
json ={
        "itemId":"10",
        "itemType":"profile",
        "version":None,
        "properties": {
            "firstName": "John",
            "lastName": "Smith"
        },
        "systemProperties":{},
        "segments":[],
        "scores":{},
        "mergedWith":None,
        "consents":{}
    })
print(r)
print(r.content)
