import json
j=json.load(open('work/sam.json'));print([(i,n.get('name'),n.get('rotation'),n.get('scale'),n.get('translation')) for i,n in enumerate(j['nodes']) if i>52]);print(j['scenes'])
