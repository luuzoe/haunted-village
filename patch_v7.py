p='/home/hatch/workspace/new-village-game/index.html'
s=open(p).read()
def rep(old,new):
    global s
    assert old in s, 'NOT FOUND: '+old[:80]
    s=s.replace(old,new,1)

# COLLIDER FIX: w/d are WORLD meters, not model units (cave was 40*60=2400m covering the whole map = player could never move; pagoda 12*1.4=16.8m made the 8m win impossible)
rep("  const w=(def.w||10)*def.s,d=(def.d||10)*def.s;",
    "  const w=(def.w||10),d=(def.d||10);")
rep("""    if(!cache[h.f])cache[h.f]=await trackLoad(h.f);
    const def={s:h.s,x:h.x,z:h.z,ry:h.ry,yo:h.yo||0,w:9,d:9};""",
"""    if(!cache[h.f])cache[h.f]=await trackLoad(h.f);
    const hb={'house-sundanese.glb':[12,10],'house-east-asian.glb':[9,9],'house-minka.glb':[10,16],'house-hut.glb':[4.5,4.5],'house-old.glb':[9,9]}[h.f.split('/').pop()]||[9,9];
    const def={s:h.s,x:h.x,z:h.z,ry:h.ry,yo:h.yo||0,w:hb[0],d:hb[1]};""")

# ANIMATION FIX: FBX tracks are named 'mixamorigHips' (NO colon) - old strip looked for 'mixamorig:' so nothing matched the GLB bones (Hips, Spine...) and the character stayed frozen in T-pose
rep("p[0]=p[0].replace(/^mixamorig:/,'');","p[0]=p[0].replace(/^mixamorig:?/,'');")

# SPAWN SAFETY: no tree within 12m of spawn (0,150)
rep("while(tries<20&&(Math.abs(x)<18&&Math.abs(z)<18||dist2d(x,z,-178,0)<24));",
    "while(tries<20&&(Math.abs(x)<18&&Math.abs(z)<18||dist2d(x,z,-178,0)<24||dist2d(x,z,0,150)<12));")

rep("const V='V6';","const V='V7';")
rep('<div id="ver">သရဲရွာ V6</div>','<div id="ver">သရဲရွာ V7</div>')

open(p,'w').write(s)
print("V7 collider patch applied OK")
