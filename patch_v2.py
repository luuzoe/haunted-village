import re
p='/home/hatch/workspace/new-village-game/index.html'
s=open(p).read()
def rep(old,new):
    global s
    assert old in s, 'NOT FOUND: '+old[:80]
    s=s.replace(old,new,1)

rep("@media (orientation:landscape){.screen h1{font-size:30px}.screen p{font-size:13px}.btn{padding:10px 22px}#loadBarWrap{bottom:10px}#minimap{width:92px;height:92px}}",
"@media (orientation:landscape){.screen h1{font-size:30px}.screen p{font-size:13px}.btn{padding:10px 22px}#loadBarWrap{bottom:10px}#minimap{width:92px;height:92px}#joy{width:104px;height:104px;bottom:14px;left:12px}#joyKnob{left:27px;top:27px;width:50px;height:50px}.abtn{width:56px;height:56px;font-size:12px}#actions{bottom:14px;right:10px;gap:8px}#stam{bottom:128px;left:12px;width:104px}#stamLbl{bottom:140px;left:12px}#pauseBtn{top:108px}}\n#rotatePrompt{position:absolute;inset:0;z-index:50;display:none;flex-direction:column;align-items:center;justify-content:center;gap:14px;background:rgba(0,0,0,.92);color:#eee;text-align:center;padding:20px}\n#rotatePrompt .ph{font-size:56px}\n#rotatePrompt .pt{font-size:22px;font-weight:900;color:#ff3333}\n#rotatePrompt .ps{font-size:14px;color:#bbb;line-height:1.7}")

rep('<div id="ver">သရဲရွာ V1</div>',
'<div id="ver">သရဲရွာ V2</div>\n<div id="rotatePrompt"><div class="ph">📱🔄</div><div class="pt">ဖုန်းကို Landscape လှည့်ပါ</div><div class="ps">ဂိမ်းက Landscape နဲ့ ဆော့ရတာ အကောင်းဆုံးပါ<br>ဖုန်းကို ဘေးတိုက်လှည့်လိုက်ပါ</div></div>')

rep("const V='V1';","const V='V2';")

rep("""function setFloorInfo(){$('floorInfo').textContent=fmtTime()}""",
"""function setFloorInfo(){$('floorInfo').textContent=fmtTime()}
function checkRotate(){
  const portrait=innerHeight>innerWidth;
  const rp=$('rotatePrompt');
  if(!rp)return;
  rp.style.display=(portrait&&S.started)?'flex':'none';
}
function tryLandscape(){
  try{
    if(document.documentElement.requestFullscreen)document.documentElement.requestFullscreen().catch(()=>{});
  }catch(e){}
  try{
    if(screen.orientation&&screen.orientation.lock)screen.orientation.lock('landscape').catch(()=>{});
  }catch(e){}
}""")

rep("""$('startBtn').addEventListener('click',()=>{
  ac();""",
"""$('startBtn').addEventListener('click',()=>{
  ac();
  tryLandscape();
  checkRotate();""")

rep("""addEventListener('resize',()=>{
  if(!camera||!renderer)return;""",
"""addEventListener('resize',()=>{
  checkRotate();
  if(!camera||!renderer)return;""")

open(p,'w').write(s)
print("V2 patch applied OK")
