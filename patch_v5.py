p='/home/hatch/workspace/new-village-game/index.html'
s=open(p).read()
def rep(old,new):
    global s
    assert old in s, 'NOT FOUND: '+old[:80]
    s=s.replace(old,new,1)

rep("import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';",
"import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';\nimport {FBXLoader} from 'three/addons/loaders/FBXLoader.js';")

rep("'assets/flashlight-real.glb':10916480};",
"'assets/flashlight-real.glb':10916480,'assets/anims/idle.fbx':1799520,'assets/anims/walk.fbx':1377264,'assets/anims/run.fbx':1351344,'assets/anims/crouch.fbx':1527280};")

rep("""function trackLoad(url){
  if(loadCache[url])return loadCache[url];
  const sz=LOAD_SIZES[url]||0;
  loadCache[url]=new Promise((res,rej)=>{
    loader.load(url,(g)=>{LOAD_TOTAL.done+=sz;updLoadBar();res(g)},undefined,(e)=>{rej(e)});
  });
  return loadCache[url];
}""",
"""function trackLoad(url){
  if(loadCache[url])return loadCache[url];
  const sz=LOAD_SIZES[url]||0;
  loadCache[url]=new Promise((res,rej)=>{
    loader.load(url,(g)=>{LOAD_TOTAL.done+=sz;updLoadBar();res(g)},undefined,(e)=>{rej(e)});
  });
  return loadCache[url];
}
const fbxLoader=new FBXLoader();
function trackFBX(url){
  if(loadCache[url])return loadCache[url];
  const sz=LOAD_SIZES[url]||0;
  loadCache[url]=new Promise((res,rej)=>{
    fbxLoader.load(url,(g)=>{LOAD_TOTAL.done+=sz;updLoadBar();res(g)},undefined,(e)=>{rej(e)});
  });
  return loadCache[url];
}
const anims={};
let curAnim=null,curAct=null;
async function loadAnims(){
  setStage('🏃 လှုပ်ရှားမှု တင်နေသည်…');
  const defs={idle:'assets/anims/idle.fbx',walk:'assets/anims/walk.fbx',run:'assets/anims/run.fbx',crouch:'assets/anims/crouch.fbx'};
  for(const k in defs){
    const fbx=await trackFBX(defs[k]);
    const clip=fbx.animations[0];
    clip.tracks.forEach(t=>{const p=t.name.split('.');p[0]=p[0].replace(/^mixamorig:/,'');t.name=p.join('.')});
    anims[k]=clip;
  }
}
function playAnim(name){
  if(!playerMixer||!anims[name]||curAnim===name)return;
  const act=playerMixer.clipAction(anims[name]);
  act.reset().fadeIn(0.25).play();
  if(curAct)curAct.fadeOut(0.25);
  curAct=act;curAnim=name;
}""")

rep("""  scene.add(playerMesh);
  if(g.animations&&g.animations.length)playerMixer=new THREE.AnimationMixer(playerMesh);""",
"""  scene.add(playerMesh);
  playerMixer=new THREE.AnimationMixer(playerMesh);""")

rep("await Promise.all([buildVillage(),loadPlayer(),loadGhosts()]);",
"await Promise.all([buildVillage(),loadPlayer(),loadGhosts(),loadAnims()]);")

rep("""  if(playerMesh){
    playerMesh.position.copy(playerPos);
    playerMesh.rotation.y=S.yaw+Math.PI;
    playerMesh.visible=!S.fpp;
  }""",
"""  if(playerMesh){
    playerMesh.position.copy(playerPos);
    playerMesh.rotation.y=S.yaw+Math.PI;
    playerMesh.visible=!S.fpp;
  }
  const moving=Math.hypot(playerVel.x,playerVel.z)>0.4;
  playAnim(S.hide?'crouch':moving?(S.run&&S.stamina>0?'run':'walk'):'idle');
  if(playerMixer)playerMixer.update(dt);""")

rep("const V='V4';","const V='V5';")
rep('<div id="ver">သရဲရွာ V4</div>','<div id="ver">သရဲရွာ V5</div>')

open(p,'w').write(s)
print("V5 patch applied OK")
