import requests

"""
Make a request to Unomi to create a rule that marks profiles as "eligible = yes"
when annualIncome < 12000
"""
r = requests.post('http://localhost:8181/cxs/rules/',
auth=('karaf','karaf'),
json ={
  "metadata": {
    "id": "eligibilityRule",
    "name": "Example eligibility rule",
    "description": "Profile annualIncome < 12000"
  },
  "condition": {
    "parameterValues": {
      "subConditions": [
        {
          "parameterValues": {
            "propertyName": "properties.annualIncome",
            "comparisonOperator": "lessThan",
            "propertyValueInt": 12000
          },
          "type": "profilePropertyCondition"
        },
        {
          "type": "profileUpdatedEventCondition",
          "parameterValues": {
          }
        }
      ],
      "operator" : "and"
    },
    "type": "booleanCondition"
  },
  "actions": [
    {
      "parameterValues": {
        "setPropertyName": "properties.eligibility",
        "setPropertyValue": "yes"
      },
      "type": "setPropertyAction"
    }
  ]
})
print("Rule Response Code:", r)
print("Rule Response Content:", r.content)


"""
Make a request to Unomi to create a profile with annualIncome < 12000
"""
r = requests.post('http://localhost:8181/cxs/profiles/',
auth=('karaf','karaf'),
json ={
        "itemId":"10",
        "itemType":"profile",
        "version":None,
        "properties": {
            "firstName": "John",
            "lastName": "Smith",
            "annualIncome": 10000
        },
        "systemProperties":{},
        "segments":[],
        "scores":{},
        "mergedWith":None,
        "consents":{}
    })
print("Profile Response Code:", r)
print("Profile Response Content:", r.content)
