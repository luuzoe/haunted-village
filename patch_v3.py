p='/home/hatch/workspace/new-village-game/index.html'
s=open(p).read()
def rep(old,new):
    global s
    assert old in s, 'NOT FOUND: '+old[:80]
    s=s.replace(old,new,1)

for a,b in [
  ("loadRealSound('ambience','assets/sounds/night-ambience.wav');","loadRealSound('ambience','assets/sounds/night-ambience.mp3');"),
  ("loadRealSound('owl','assets/sounds/owl-hoot.wav');","loadRealSound('owl','assets/sounds/owl-hoot.mp3');"),
  ("loadRealSound('woodstep','assets/sounds/footsteps-grass.wav');","loadRealSound('woodstep','assets/sounds/footsteps-grass.mp3');"),
  ("loadRealSound('dog','assets/sounds/dog-bark.flac');","loadRealSound('dog','assets/sounds/dog-bark.mp3');"),
  ("loadRealSound('whisper','assets/sounds/whisper-female.wav');","loadRealSound('whisper','assets/sounds/whisper-female.mp3');"),
  ("loadRealSound('thunder','assets/sounds/thunder-distant.wav');","loadRealSound('thunder','assets/sounds/thunder-distant.mp3');"),
  ("loadRealSound('drone','assets/sounds/drone-eerie.wav');","loadRealSound('drone','assets/sounds/drone-eerie.mp3');"),
]:
    rep(a,b)

rep("""  setStage('🏠 ရွာအိမ်တွေ တင်နေသည်…');
  const cache={};""",
"""  setStage('🏠 ရွာအိမ်တွေ တင်နေသည်…');
  await Promise.all([...new Set(VILLAGE.map(h=>h.f))].map(f=>trackLoad(f)));
  const cache={};""")

rep("""  setStage('🌳 သစ်ပင်တွေ စိုက်နေသည်…');
  const treeCache={};""",
"""  setStage('🌳 သစ်ပင်တွေ စိုက်နေသည်…');
  await Promise.all(TREES.map(t=>trackLoad(t.f)));
  const treeCache={};""")

rep("""  setStage('⛰️ တောင်တွေ တင်နေသည်…');
  const cave=await trackLoad('assets/village/mountain-cave.glb');""",
"""  setStage('⛰️ တောင်တွေ တင်နေသည်…');
  const [cave,green,well,fence]=await Promise.all([trackLoad('assets/village/mountain-cave.glb'),trackLoad('assets/village/mountain-green.glb'),trackLoad('assets/village/stone-well.glb'),trackLoad('assets/village/fence-pack.glb')]);""")

rep("""  const green=await trackLoad('assets/village/mountain-green.glb');
  const gm=green.scene;""",
"""  const gm=green.scene;""")

rep("""  const well=await trackLoad('assets/village/stone-well.glb');
  placeModel(well.scene,{s:0.006,x:0,z:-8,ry:0,w:2,d:2});
  const fence=await trackLoad('assets/village/fence-pack.glb');""",
"""  placeModel(well.scene,{s:0.006,x:0,z:-8,ry:0,w:2,d:2});""")

rep("""  const k=await trackLoad('assets/ghost-kuntilanak.glb');""",
"""  const [k,sh]=await Promise.all([trackLoad('assets/ghost-kuntilanak.glb'),trackLoad('assets/ghost-shazia.glb')]);""")

rep("""  const sh=await trackLoad('assets/ghost-shazia.glb');
  const sg=new THREE.Group();""",
"""  const sg=new THREE.Group();""")

rep("""    await buildVillage();
    buildClues();
    await loadPlayer();
    await loadGhosts();""",
"""    await Promise.all([buildVillage(),loadPlayer(),loadGhosts()]);
    buildClues();""")

rep("const V='V2';","const V='V3';")
rep('<div id="ver">သရဲရွာ V2</div>','<div id="ver">သရဲရွာ V3</div>')

open(p,'w').write(s)
print("V3 patch applied OK")
