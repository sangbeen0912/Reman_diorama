from pathlib import Path
p=Path('work/ramen/dist/scene.js');s=p.read_text(encoding='utf-8-sig').replace("i<3?bowl(x,.69):bowl(1.53,z)","i<3?bowl(x,.86):bowl(1.66,z)");p.write_text(s,encoding='utf-8')
