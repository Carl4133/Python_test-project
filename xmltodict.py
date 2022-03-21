import xmltodict

with open('data.xml',encoding='UTF-8') as f:
    doc = xmltodict.parse(f.read())
    print(doc['櫥櫃']['外觀'])
    