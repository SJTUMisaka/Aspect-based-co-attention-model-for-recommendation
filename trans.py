import json
json_data = open('mydata.raw').read()
data = json.loads(json_data)
f = open('new.raw', 'w+', encoding='utf-8')
for item in data['data']:
    output = item['abstract']
    print('<DOC>\n' + output + '\n</DOC>',file = f)