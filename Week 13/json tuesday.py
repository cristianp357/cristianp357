#json and dictinonaries and their usage together 9:42
#pre populate dictionaries, it accounts for the keys without haveing to worry about it in the body of your code
# ex: 4 words can prepopulate with 4 keys
# you can treat dictionaries as variables but not variables

import json
data = '''
[
    { "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    } ,
    { "id" : "009",
        "x" : "7",
        "name" : "Brent"
    }
]'''

j_data = json.loads(data)

for d in j_data:
    print(d['id'])
    d['y'] = int(d['id'])* int (d['x'])
    d['x'] =
