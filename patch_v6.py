p='/home/hatch/workspace/new-village-game/index.html'
s=open(p).read()
def rep(old,new):
    global s
    assert old in s, 'NOT FOUND: '+old[:80]
    s=s.replace(old,new,1)

# 1. DARKER NIGHT
rep("scene.fog=new THREE.FogExp2(0x05070f,0.011);","scene.fog=new THREE.FogExp2(0x05070f,0.016);")
rep("hemiLight=new THREE.HemisphereLight(0x334466,0x0a0f08,0.35);","hemiLight=new THREE.HemisphereLight(0x1c2636,0x05070a,0.10);")
rep("moonLight=new THREE.DirectionalLight(0xbfd0ff,0.7);","moonLight=new THREE.DirectionalLight(0xbfd0ff,0.22);")
rep("x.fillStyle='#1d2b12';","x.fillStyle='#101a0b';")
rep("flashLight=new THREE.SpotLight(0xfff2cc,90,18,0.45,0.35,1);","flashLight=new THREE.SpotLight(0xfff2cc,150,24,0.45,0.35,1);")

# 2. MORE HOUSES: 18 -> 41
rep("""  {f:'assets/village/house-hut.glb',s:1.8,x:90,z:90,ry:1.9}
];""",
"""  {f:'assets/village/house-hut.glb',s:1.8,x:90,z:90,ry:1.9},
  {f:'assets/village/house-sundanese.glb',s:1.0,x:115,z:-70,ry:0.7},
  {f:'assets/village/house-east-asian.glb',s:1.0,x:140,z:-30,ry:-1.2},
  {f:'assets/village/house-hut.glb',s:1.8,x:115,z:0,ry:2.0},
  {f:'assets/village/house-minka.glb',s:0.4,x:145,z:30,ry:0.3},
  {f:'assets/village/house-old.glb',s:0.85,x:110,z:60,ry:1.5,yo:2.0},
  {f:'assets/village/house-sundanese.glb',s:1.0,x:160,z:-60,ry:-0.5},
  {f:'assets/village/house-east-asian.glb',s:1.0,x:165,z:10,ry:2.6},
  {f:'assets/village/house-hut.glb',s:1.8,x:130,z:85,ry:-2.2},
  {f:'assets/village/house-minka.glb',s:0.4,x:-115,z:-80,ry:1.1},
  {f:'assets/village/house-sundanese.glb',s:1.0,x:-140,z:-20,ry:-0.9},
  {f:'assets/village/house-east-asian.glb',s:1.0,x:-120,z:20,ry:0.8},
  {f:'assets/village/house-hut.glb',s:1.8,x:-150,z:50,ry:-1.7},
  {f:'assets/village/house-old.glb',s:0.85,x:-110,z:80,ry:2.4,yo:2.0},
  {f:'assets/village/house-minka.glb',s:0.4,x:-165,z:-50,ry:-2.6},
  {f:'assets/village/house-sundanese.glb',s:1.0,x:-135,z:-100,ry:0.2},
  {f:'assets/village/house-east-asian.glb',s:1.0,x:-40,z:-130,ry:1.9},
  {f:'assets/village/house-hut.glb',s:1.8,x:40,z:-135,ry:-0.4},
  {f:'assets/village/house-minka.glb',s:0.4,x:-80,z:-135,ry:2.9},
  {f:'assets/village/house-old.glb',s:0.85,x:80,z:-125,ry:-1.3,yo:2.0},
  {f:'assets/village/house-sundanese.glb',s:1.0,x:-45,z:130,ry:0.6},
  {f:'assets/village/house-east-asian.glb',s:1.0,x:45,z:135,ry:-2.5},
  {f:'assets/village/house-hut.glb',s:1.8,x:-100,z:130,ry:1.3},
  {f:'assets/village/house-minka.glb',s:0.4,x:100,z:125,ry:-0.7}
];""")

# 3. MORE TREES: 58 -> 140
rep("{f:'assets/village/tree-realistic.glb',s:0.7,n:26},","{f:'assets/village/tree-realistic.glb',s:0.7,n:60},")
rep("{f:'assets/village/tree-palm.glb',s:0.1,n:14},","{f:'assets/village/tree-palm.glb',s:0.1,n:30},")
rep("{f:'assets/village/tree-models.glb',s:0.6,n:18}","{f:'assets/village/tree-models.glb',s:0.6,n:50}")

# 4. FENCES: 4 segments -> 40 (path both sides + pagoda ring)
rep("""  for(let i=0;i<4;i++){
    const fx=-30+i*20;
    placeModel(fence.scene.clone(),{s:0.01,x:fx,z:70,ry:0,w:0.6,d:4});
  }""",
"""  for(let i=0;i<16;i++){
    const fz=48-i*6;
    placeModel(fence.scene.clone(),{s:0.01,x:-7,z:fz,ry:0,w:0.6,d:4});
    placeModel(fence.scene.clone(),{s:0.01,x:7,z:fz,ry:0,w:0.6,d:4});
  }
  for(let i=0;i<8;i++){
    const a=i/8*Math.PI*2;
    placeModel(fence.scene.clone(),{s:0.01,x:Math.cos(a)*16,z:-120+Math.sin(a)*16,ry:-a+Math.PI/2,w:0.6,d:4});
  }""")

# 5. DOG + OWL MORE OFTEN
rep("function owlSound(){if(S.playT-lastOwl<70)return;lastOwl=S.playT;playReal('owl',0.5)}","function owlSound(){if(S.playT-lastOwl<45)return;lastOwl=S.playT;playReal('owl',0.5)}")
rep("function dogSound(){if(S.playT-lastDog<90)return;lastDog=S.playT;playReal('dog',0.35)}","function dogSound(){if(S.playT-lastDog<45)return;lastDog=S.playT;playReal('dog',0.5)}")
rep("if(Math.random()<dt*0.01)owlSound();","if(Math.random()<dt*0.02)owlSound();")
rep("if(Math.random()<dt*0.008)dogSound();","if(Math.random()<dt*0.025)dogSound();")

# 6. DEBUG PROBE (for movement verification)
rep("let stepAcc=0,stepCount=0;","let stepAcc=0,stepCount=0;\nwindow.__hv={get pos(){return {x:playerPos.x,z:playerPos.z}},get joy(){return joyVec},get started(){return S.started},get ver(){return V}};")

rep("const V='V5';","const V='V6';")
rep('<div id="ver">သရဲရွာ V5</div>','<div id="ver">သရဲရွာ V6</div>')

open(p,'w').write(s)
print("V6 patch applied OK")
