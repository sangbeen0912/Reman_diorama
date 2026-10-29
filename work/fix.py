from pathlib import Path
p=Path('work/ramen/dist/scene.js');s=p.read_text(encoding='utf-8-sig');s=s.replace("mix.setTime(isChef?0:3.0);root.updateMatrixWorld(true)","mix.setTime(isChef?0:3.0);if(!isChef)root.position.z=.361*.96;root.updateMatrixWorld(true)")
s=s.replace("isChef?[.1,-.55,Math.PI]","isChef?[-1.05,-.95,Math.PI]")
s=s.replace("[k*.009,-.11,-.15]","[k*.009,-.11,.15]")
s=s.replace("V(.0045,-.11,-.15)","V(.0045,-.11,.15)")
s=s.replace("let from=p.bowl.clone().add(V(0,.19,0));target=from.lerp(mouth, lift*.85);","let tip=p.bowl.clone().lerp(mouth,lift*.92);target=tip.sub(V(0,-.11,.15).applyQuaternion(p.group.quaternion));")
s=s.replace("V(.42,.98,-1.2)","V(-1.35,1.03,-1.28)")
p.write_text(s,encoding='utf-8')
