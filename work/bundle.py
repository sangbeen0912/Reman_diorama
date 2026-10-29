import pathlib,re,base64,json,posixpath
root=pathlib.Path('work/ramen/dist');imports={}
for f in root.glob('assets/**/*.js'):
 key=f.relative_to(root).as_posix();s=f.read_text(encoding='utf-8-sig')
 def sub(m):
  name=m.group(1)
  if name.startswith('.'):name='lib/'+posixpath.normpath(posixpath.join(posixpath.dirname(key),name))
  return "from '"+name+"'"
 s=re.sub(r"from '([^']+)'",sub,s)
 imports['three' if f.name=='three.module.js' else 'lib/'+key]='data:text/javascript;base64,'+base64.b64encode(s.encode()).decode()
s=(root/'scene.js').read_text(encoding='utf-8-sig');s=s.replace("from './assets/","from 'lib/assets/");s=s.replace("'./assets/sam.glb'","'data:model/gltf-binary;base64,"+base64.b64encode((root/'assets/sam.glb').read_bytes()).decode()+"'")
h=(root/'index.html').read_text(encoding='utf-8-sig');h=re.sub(r'<script type="importmap">.*?</script>','<script type="importmap">'+json.dumps({'imports':imports})+'</script>',h);h=h.replace('<script type="module" src="./scene.js"></script>','<script type="module">'+s+'</script>')
pathlib.Path('outputs/01_비오는골목.html').write_text(h,encoding='utf-8');print('standalone',len(h))
