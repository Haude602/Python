import json
 #string consisting dictionary within dictionary
data = ''' {              
    "name":"Vikrant",
    "phone":{
        "type":"int",
        "number":"9807855119"
    },
    "email":{
        "hide":"yes"
    }
}'''
info=json.loads(data)  #now info is a dictionary

print("name:",info["name"])
print("hide:",info["email"]["hide"])
