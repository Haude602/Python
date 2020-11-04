#using API of google maps(google geocoding api)
import urllib.request,urllib.parse,urllib.error
import json
#Note that google is increasingly requiirng keys
#for this API

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = input('Enter location')
    if len(address)<1: break
    #concatinating string to make a single url (+) also 2nd part of url
    #  is encoded version of location  to get api 
    url=serviceurl+urllib.parse.urlencode({'address':address}) #{'address':address}) gives 
                                                                #dictionar of address
    print("retrieving ",url)
    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print("Retrieved",len(data),"characters")
    try:
        js=json.loads(data)
    except:
        js= None
    if not js or 'status' not in js or js['status'] != 'OK': #If any of this condition comes
        print('====Failure To Retrieve=====')
        print(data)
        continue
    print(json.dumps(js,indent=4)) #json.dmps is opposite of json.load .so,it prints json wit indent of 4
         
    lat=js["results"][0]["geometry"]["location"]["lat"] #We can extract anything required after  
    lng=js["results"][0]["geometry"]["location"]["lng"] #printing upper statement (js)
    print('lat',lat,'lng',lng)
    location =js['results'][0]['formatted_address']
    print(location)


