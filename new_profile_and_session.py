from requests import post
from datetime import datetime
"""
Make a request to Unomi to create a profile with ID = 10
"""
profile = {
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
}

session = {
    "itemId": "10",
    "itemType":"session",
    "scope":None,
    "version":1,
    "profileId":profile_id,
    "profile": profile,
    "properties":{},
    "systemProperties":{},
    "timeStamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
}

# Create or update profile
r = post('http://localhost:8181/cxs/profiles/'
auth=('karaf','karaf'),
json =profile)
print(r)
print(r.content)


# Create session
r = post('http://localhost:8181/cxs/profiles/sessions/10',
    auth=('karaf', 'karaf'),
    json=session)

print(r)
print(r.content)
