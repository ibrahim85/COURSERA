import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''


data1 = '''
{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
}'''




info = json.loads(data)
print 'Name:',info["name"]
print 'Hide:',info["email"]["hide"]

print '\n'


info2 = json.loads(data1)
print 'ID:', info2['id']
print 'X:', info2['x']
print 'Name:', info2['name']