p='/home/hatch/workspace/new-village-game/index.html'
s=open(p).read()
def rep(old,new):
    global s
    assert old in s, 'NOT FOUND: '+old[:80]
    s=s.replace(old,new,1)

rep("""function placeModel(gltf,def){
  const g=gltf.scene;
  g.scale.setScalar(def.s);""",
"""function placeModel(g,def){
  g.scale.setScalar(def.s);""")

rep("const V='V3';","const V='V4';")
rep('<div id="ver">သရဲရွာ V3</div>','<div id="ver">သရဲရွာ V4</div>')

open(p,'w').write(s)
print("V4 patch applied OK")
