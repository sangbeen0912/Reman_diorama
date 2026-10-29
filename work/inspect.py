import struct,json,pathlib
for f in ['sam','chef','seated']:
 b=pathlib.Path('work/ramen/dist/assets/'+f+'.glb').read_bytes(); n=struct.unpack_from('<I',b,12)[0];j=json.loads(b[20:20+n]);pathlib.Path('work/'+f+'.json').write_text(json.dumps(j,indent=2))
 print(f, 'nodes',len(j['nodes']),'skins',len(j.get('skins',[])),'animations',[(a.get('name'),len(a['channels'])) for a in j.get('animations',[])])
 print([(i,x.get('name'),x.get('translation')) for i,x in enumerate(j['nodes']) if any(s in x.get('name','').lower() for s in ['arm','hand','head','spine','pelvis','root'])][:65]); print('materials',[(i,m.get('name')) for i,m in enumerate(j.get('materials',[]))])
