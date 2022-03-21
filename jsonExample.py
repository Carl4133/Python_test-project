import json
with open('data.json',encoding='UTF-8') as f:
    doc = json.loads(f.read())
    print(doc['日期時間'])