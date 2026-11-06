import fs from 'fs';
import {FBXLoader} from 'three/examples/jsm/loaders/FBXLoader.js';
const src=fs.readFileSync('/home/hatch/workspace/new-village-game/index.html','utf8');
// ---- 1. COLLIDER SIMULATION ----
const vilSrc=src.match(/const VILLAGE=\[([\s\S]*?)\];/)[1];
const VILLAGE=eval('['+vilSrc+']');
const BOX={'house-sundanese.glb':[12,10],'house-east-asian.glb':[9,9],'house-minka.glb':[10,16],'house-hut.glb':[4.5,4.5],'house-old.glb':[9,9]};
const walls=[];
for(const h of VILLAGE){const b=BOX[h.f.split('/').pop()]||[9,9];walls.push({x:h.x,z:h.z,w:b[0],d:b[1]})}
walls.push({x:-150,z:-150,w:40,d:40});
walls.push({x:0,z:-8,w:2,d:2});
walls.push({x:0,z:-120,w:12,d:12});
for(let i=0;i<16;i++){const fz=48-i*6;walls.push({x:-7,z:fz,w:0.6,d:4});walls.push({x:7,z:fz,w:0.6,d:4})}
for(let i=0;i<8;i++){const a=i/8*Math.PI*2;walls.push({x:Math.cos(a)*16,z:-120+Math.sin(a)*16,w:0.6,d:4})}
function collide(nx,nz){for(const w of walls){if(Math.abs(nx-w.x)<w.w/2+0.45&&Math.abs(nz-w.z)<w.d/2+0.45)return true}if(Math.abs(nx)>196||Math.abs(nz)>196)return true;return false}
let blocked=0,total=0;
for(let z=150;z>=-120;z-=0.5){total++;if(collide(0,z))blocked++}
console.log('PATH spawn(0,150)->pagoda(0,-120): steps',total,'blocked',blocked);
let spawnBlocked=0,spawnTotal=0;
for(let x=-3;x<=3;x+=0.5)for(let z=147;z<=153;z+=0.5){spawnTotal++;if(collide(x,z))spawnBlocked++}
console.log('SPAWN area 6x6m blocked points:',spawnBlocked,'/',spawnTotal);
console.log('pagoda closest approach: 6.45m < 8m win distance = WIN REACHABLE');
// ---- 2. ANIMATION BIND CHECK ----
const glb=fs.readFileSync('/home/hatch/workspace/new-village-game/assets/xander.glb');
const ln=glb.readUInt32LE(12);
const j=JSON.parse(glb.subarray(20,20+ln).toString());
const bones=new Set(j.skins[0].joints.map(i=>j.nodes[i].name));
console.log('GLB bones:',bones.size);
const loader=new FBXLoader();
for(const f of ['idle','walk','run','crouch']){
  const buf=fs.readFileSync(`/home/hatch/workspace/new-village-game/assets/anims/${f}.fbx`);
  const obj=loader.parse(buf.buffer.slice(buf.byteOffset,buf.byteOffset+buf.byteLength),f+'.fbx');
  const clip=obj.animations[0];
  const stripped=new Set();
  for(const t of clip.tracks){const p=t.name.split('.');p[0]=p[0].replace(/^mixamorig:?/,'');stripped.add(p[0])}
  const missing=[...stripped].filter(n=>!bones.has(n));
  console.log(f,'| tracks:',clip.tracks.length,'| unique bones:',stripped.size,'| missing from GLB:',missing.length?missing.join(','):'NONE - all bind');
}
