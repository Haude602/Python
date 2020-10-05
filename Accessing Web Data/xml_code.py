import xml.etree.ElementTree as ET  #name of library
data = '''
<person>
    <name>vikrant</name>
    <phone type="int">
        9807855119
    </phone>
    <email hide="yes"/>
</person> ''' #here data is storing just a multiline string
tree=ET.fromstring(data)    #form a tree by using data 
print('name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))