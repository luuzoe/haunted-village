p='/home/hatch/workspace/new-village-game/index.html'
s=open(p).read()
def rep(old,new):
    global s
    assert old in s, 'NOT FOUND: '+old[:80]
    s=s.replace(old,new,1)

# 1. STORY: each clue carries a story fragment
rep("{id:0,name:'ဒိုင်ယာရီ စာမျက်နှာ',x:-52,z:-33},","{id:0,name:'ဒိုင်ယာရီ စာမျက်နှာ',x:-52,z:-33,story:'မမေသူရဲ့ နောက်ဆုံး စာမျက်နှာ — \\'ဒီည လပြည့်ညမှာ စေတီနားက တစ်ခုခု ငါ့ကို ခေါ်နေတယ်... ငါ သွားကြည့်မယ်။ ငါ ပြန်မလာခဲ့ရင် အကိုရေ... ငါ့ကို ရှာပါ။\\''},")
rep("{id:1,name:'အမွေ လက်ဖွဲ့',x:78,z:-18},","{id:1,name:'အမွေ လက်ဖွဲ့',x:78,z:-18,story:'အဖွားရဲ့ လက်ဖွဲ့ — \\'ဒီလက်ဖွဲ့ကို ဝတ်ထားရင် သရဲ မကပ်ဘူး\\' လို့ အဖွားပြောခဲ့တယ်။ မမေသူက ဒါကို ဘာလို့ ဒီမှာ ထားခဲ့တာလဲ?'},")
rep("{id:2,name:'ဓာတ်ပုံ အဟောင်း',x:62,z:-38},","{id:2,name:'ဓာတ်ပုံ အဟောင်း',x:62,z:-38,story:'လွန်ခဲ့တဲ့ ၁၀ နှစ်က ဓာတ်ပုံ — မမေသူနောက်မှာ အနီဝတ်ထားတဲ့ မိန်းမတစ်ယောက် ရပ်နေတယ်။ သူ့မျက်နှာ... မရှိဘူး။'},")
rep("{id:3,name:'မီးအိမ်',x:-88,z:-63},","{id:3,name:'မီးအိမ်',x:-88,z:-63,story:'မမေသူရဲ့ မီးအိမ် — ၁၀ နှစ် ကြာပြီးတာတောင် ခုထိ နွေးနေတယ်။ သူ ဒီရွာမှာ ခုထိ ရှိနေတုန်းပဲ...'},")
rep("{id:4,name:'ရွာသော့',x:67,z:-83}","{id:4,name:'ရွာသော့',x:67,z:-83,story:'စေတီရဲ့ ရှေးဟောင်း သော့ — ဒီသော့နဲ့မှ ကျိန်စာကို ဖြေနိုင်မယ်။ စေတီနားမှာ သူ စောင့်နေတယ်...'}")
rep("grp.userData={clueId:c.id,name:c.name,baseY:grp.position.y};","grp.userData={clueId:c.id,name:c.name,story:c.story,baseY:grp.position.y};")

# 2. STORY CARD: show the fragment when a clue is picked up
rep("function toast(msg,ms){const t=$('toast');t.textContent=msg;t.style.display='block';clearTimeout(t._h);t._h=setTimeout(()=>{t.style.display='none'},ms||2600)}",
"""function toast(msg,ms){const t=$('toast');t.textContent=msg;t.style.display='block';clearTimeout(t._h);t._h=setTimeout(()=>{t.style.display='none'},ms||2600)}
function showStory(d){$('storyTitle').textContent='📜 '+d.name;$('storyText').textContent=d.story;$('storyCard').style.display='flex'}
$('storyClose').addEventListener('click',()=>{$('storyCard').style.display='none'});""")
rep("    toast('📜 ရပြီ: '+nc.clue.userData.name+' ('+S.clues+'/'+S.clueTotal+')');",
"    toast('📜 ရပြီ: '+nc.clue.userData.name+' ('+S.clues+'/'+S.clueTotal+')');\n    showStory(nc.clue.userData);")

# 3. STORY CARD HTML + CSS
rep('#ver{position:absolute;bottom:4px;right:6px;font-size:10px;color:#666;z-index:21}',
"""#ver{position:absolute;bottom:4px;right:6px;font-size:10px;color:#666;z-index:21}
#storyCard{position:absolute;inset:0;z-index:40;display:none;align-items:center;justify-content:center;background:rgba(0,0,0,.72);padding:20px}
#storyCard .scard{background:#160a06;border:2px solid #8a6d2f;border-radius:14px;max-width:480px;padding:20px;color:#f0e0c0}
#storyCard h3{margin:0 0 10px;color:#ffd700;font-size:18px}
#storyCard p{font-size:15px;line-height:1.9;margin:0 0 14px}""")
rep('<div id="rotatePrompt">',
"""<div id="storyCard"><div class="scard"><h3 id="storyTitle"></h3><p id="storyText"></p><button class="btn" id="storyClose">ဆက်သွားမယ်</button></div></div>
<div id="rotatePrompt">""")

# 4. MENU STORY INTRO
rep("<p>ရွာမှာ လူတစ်ယောက် ပျောက်နေတယ်။ သဲလွန်စ ၅ ခု ရှာပြီး ရွာရဲ့ ကျိန်စာကို ဖြေရမယ်။ သရဲတွေ လိုက်ရင် ပြေး — ပုန်းရင် ရပ်နေရမယ်။ အရုဏ်တက်ခါနီး လွတ်မြောက်ရမယ်။</p>",
"<p>လွန်ခဲ့တဲ့ ၁၀ နှစ်က လပြည့်ညမှာ လမင်းရွာက မိန်းကလေး မမေသူ စေတီနားမှာ ပျောက်သွားတယ်။ အဲဒီညထဲက ရွာတစ်ခုလုံး ကျိန်စာမိပြီး ညနက်တိုင်း သရဲတွေ ထွက်လာတယ်။ မင်းက မမေသူရဲ့ အကို Xander — သဲလွန်စ ၅ ခု ရှာပြီး ကျိန်စာကို ဖြေရမယ်။ သရဲတွေ လိုက်ရင် ပြေး — ပုန်းရင် ရပ်နေရမယ်။</p>")

# 5. WARM WINDOWS on houses
rep("let moonLight,hemiLight,moonMesh;","let moonLight,hemiLight,moonMesh;\nlet fireflies=null,fireBase=[];")
rep("""async function buildVillage(){""",
"""const winGeo=new THREE.PlaneGeometry(0.9,1.1);
const winMat=new THREE.MeshBasicMaterial({color:0xffb84d});
function addWindows(def){
  const gy=groundH(def.x,def.z)+(def.yo||0);
  for(const s of [-1,1]){
    const w=new THREE.Mesh(winGeo,winMat);
    const fx=Math.sin(def.ry||0),fz=Math.cos(def.ry||0);
    const rx=Math.sin((def.ry||0)+Math.PI/2),rz=Math.cos((def.ry||0)+Math.PI/2);
    w.position.set(def.x+fx*(def.d/2+0.15)+rx*s*1.6,gy+2.1,def.z+fz*(def.d/2+0.15)+rz*s*1.6);
    w.rotation.y=def.ry||0;
    scene.add(w);
  }
}
async function buildVillage(){""")
rep("""    placeModel(cache[h.f].scene.clone(),def);
  }""",
"""    placeModel(cache[h.f].scene.clone(),def);
    addWindows(def);
  }""")

# 6. MOON GLOW + FIREFLIES
rep("""  moonMesh=new THREE.Mesh(moonGeo,moonMat);
  moonMesh.position.set(160,210,-260);
  moonMesh.lookAt(0,0,0);
  scene.add(moonMesh);""",
"""  moonMesh=new THREE.Mesh(moonGeo,moonMat);
  moonMesh.position.set(160,210,-260);
  moonMesh.lookAt(0,0,0);
  scene.add(moonMesh);
  const glowC=document.createElement('canvas');glowC.width=glowC.height=128;const gx=glowC.getContext('2d');const grd=gx.createRadialGradient(64,64,4,64,64,64);grd.addColorStop(0,'rgba(220,230,255,0.55)');grd.addColorStop(1,'rgba(220,230,255,0)');gx.fillStyle=grd;gx.fillRect(0,0,128,128);
  const moonGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(glowC),transparent:true,depthWrite:false,fog:false}));
  moonGlow.scale.set(90,90,1);moonGlow.position.copy(moonMesh.position);scene.add(moonGlow);
  const fireGeo=new THREE.BufferGeometry();
  const firePos=new Float32Array(120*3);
  for(let i=0;i<120;i++){const x=rand(-150,150),z=rand(-150,150),y=rand(1,3.5);firePos.set([x,y,z],i*3);fireBase.push([x,y,z,rand(0,Math.PI*2)])}
  fireGeo.setAttribute('position',new THREE.BufferAttribute(firePos,3));
  fireflies=new THREE.Points(fireGeo,new THREE.PointsMaterial({color:0xaaff66,size:0.18,transparent:true,opacity:0.85}));
  scene.add(fireflies);""")

# 7. ANIMATE FIREFLIES in gameLoop
rep("""  if(Math.random()<dt*0.02)owlSound();""",
"""  if(fireflies){const p=fireflies.geometry.attributes.position;for(let i=0;i<120;i++){const b=fireBase[i];p.array[i*3]=b[0]+Math.sin(S.playT*0.5+b[3])*1.5;p.array[i*3+1]=b[1]+Math.sin(S.playT*0.8+b[3]*2)*0.5;p.array[i*3+2]=b[2]+Math.cos(S.playT*0.4+b[3])*1.5}p.needsUpdate=true}
  if(Math.random()<dt*0.02)owlSound();""")

rep("const V='V7';","const V='V8';")
rep('<div id="ver">သရဲရွာ V7</div>','<div id="ver">သရဲရွာ V8</div>')

open(p,'w').write(s)
print("V8 patch applied OK")
