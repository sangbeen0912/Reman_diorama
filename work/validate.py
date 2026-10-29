import pathlib,re,json,zipfile
r=pathlib.Path('work/ramen/dist');missing=[]
for p in r.rglob('*.js'):
 for n in re.findall(r"from ['\"]([^'\"]+)['\"]",p.read_text(encoding='utf-8-sig')):
  if n.startswith('.') and not (p.parent/n).resolve().exists():missing.append((str(p),n))
assert not missing,missing
j=json.loads(pathlib.Path('outputs/02_prompt_coach.json').read_text(encoding='utf-8'));assert len(j['acceptance_tests'])==8
z=zipfile.ZipFile('outputs/03_발표자료.pptx');assert z.testzip() is None
slides=[n for n in z.namelist() if re.fullmatch('ppt/slides/slide[0-9]+.xml',n)];assert len(slides)==6
print('Dependency imports resolved; JSON valid; PPTX ZIP valid, 6 slides.')
for p in pathlib.Path('outputs').iterdir():print(p.name,p.stat().st_size)
