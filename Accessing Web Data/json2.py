import json
#input is a list of dictinaries
input='''
[
    {
        "id":"001",
        "x":"2",
        "Name":"Vikrant"
    },
    {
        "id":"009",
        "x":"7",
        "Name":"Panjiyar"
    }
]'''

info = json.loads(input)   #info is a list
print ("user count:",len(input))
for item in info:   #here item is dictionary
    print("name",item["Name"])
    print("id:",item["id"])