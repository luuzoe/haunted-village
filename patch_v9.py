#!/usr/bin/env python3
# V9: performance pass — cheaper shadows so phones run smoother.
# Trees (140) + fences (40) no longer cast shadows (night, moon 0.22 — their
# shadows are barely visible); houses/player/ghosts still cast. Shadow map 1024->512.
import re
p='/home/hatch/workspace/new-village-game/index.html'
s=open(p,encoding='utf-8').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)>=1, 'NOT FOUND: '+a[:70]
    s=s.replace(a,b,cnt)
rep("const V='V8'","const V='V9'")
rep("moonLight.shadow.mapSize.set(1024,1024)","moonLight.shadow.mapSize.set(512,512)")
rep("g.traverse(o=>{if(o.isMesh){o.castShadow=true;o.receiveShadow=true}});",
    "g.traverse(o=>{if(o.isMesh){o.castShadow=!def.ns;o.receiveShadow=true}});")
rep("const def={s:t.s*rand(0.85,1.25),x,z,ry:rand(0,Math.PI*2),w:1.2,d:1.2};",
    "const def={s:t.s*rand(0.85,1.25),x,z,ry:rand(0,Math.PI*2),w:1.2,d:1.2,ns:1};")
rep("placeModel(fence.scene.clone(),{s:0.01,x:-7,z:fz,ry:0,w:0.6,d:4});",
    "placeModel(fence.scene.clone(),{s:0.01,x:-7,z:fz,ry:0,w:0.6,d:4,ns:1});")
rep("placeModel(fence.scene.clone(),{s:0.01,x:7,z:fz,ry:0,w:0.6,d:4});",
    "placeModel(fence.scene.clone(),{s:0.01,x:7,z:fz,ry:0,w:0.6,d:4,ns:1});")
rep("placeModel(fence.scene.clone(),{s:0.01,x:Math.cos(a)*16,z:-120+Math.sin(a)*16,ry:-a+Math.PI/2,w:0.6,d:4});",
    "placeModel(fence.scene.clone(),{s:0.01,x:Math.cos(a)*16,z:-120+Math.sin(a)*16,ry:-a+Math.PI/2,w:0.6,d:4,ns:1});")
open(p,'w',encoding='utf-8').write(s)
print('V9 patched OK')
