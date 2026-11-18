// Usage: node check.js data.js  — quality gates for an Exam Lab dataset. Exit code 1 on hard errors.
const fs=require('fs');const src=fs.readFileSync(process.argv[2],'utf8');
const {CONFIG,B,M,G}=new Function(src+';return {CONFIG,B,M,G};')();
let err=0,warn=0;const E=m=>{console.log('ERROR',m);err++;},W=m=>{console.log('WARN ',m);warn++;};
const lecs=new Set(CONFIG.lectures.map(x=>x.id));
const all=[...B.map((q,i)=>({...q,_id:'b'+i})),...M.map((q,i)=>({...q,_id:'m'+i}))];
const seen=new Map();let longest=0,obj=0;
for(const q of all){const t=q.t||'mcq';
  if(!lecs.has(q.l))E(`${q._id} unknown lecture "${q.l}"`);
  if(!q.q||q.q.length<8)E(`${q._id} missing question text`);
  const key=q.q.trim().toLowerCase();if(seen.has(key))E(`${q._id} duplicate of ${seen.get(key)}`);seen.set(key,q._id);
  if(t==='written'){if(!q.a||q.a.length<20)E(`${q._id} written question without a real model answer`);continue;}
  if(!Array.isArray(q.o))E(`${q._id} no options`);
  if(t==='tf'&&(q.o.length!==2||!q.o.every(o=>/^(true|false)$/i.test(o[0]))))E(`${q._id} tf must have exactly True/False`);
  if(t==='mcq'&&(q.o.length<3||q.o.length>5))E(`${q._id} mcq needs 3-5 options`);
  q.o.forEach((o,j)=>{if(!o[0]||!o[1]||o[1].length<2)E(`${q._id} option ${j} missing text or explanation`);});
  const txt=q.o.map(o=>o[0].trim().toLowerCase());if(new Set(txt).size!==txt.length)E(`${q._id} repeated option text`);
  if(!q.k)W(`${q._id} no key idea (k)`);
  if(t==='mcq'){obj++;const L=q.o.map(o=>o[0].length);const mx=Math.max(...L.slice(1));if(L[0]===Math.max(...L))longest++;if(L[0]>1.6*mx)W(`${q._id} correct answer much longer than distractors (${L[0]} vs ${mx})`);
    if(q.o.some(o=>/all of the above|none of the above/i.test(o[0])))E(`${q._id} uses All/None of the above (breaks shuffling)`);}
}
const tfs=all.filter(q=>q.t==='tf');if(tfs.length){const nt=tfs.filter(q=>/^true$/i.test(q.o[0][0])).length,r=nt/tfs.length;
  console.log(`T/F answers: ${nt} True / ${tfs.length-nt} False`);
  if(r<0.3||r>0.7){(tfs.length>=4?E:W)(`T/F answers unbalanced (${Math.round(r*100)}% True) — keep True between 30% and 70%`);}}
const share=obj?longest/obj:0;console.log(`mcq where correct is longest: ${longest}/${obj} (${Math.round(share*100)}%)`);
if(share>0.5)E('length cue too strong: >50% of MCQs have the correct answer as the longest option — rewrite distractors');
for(const l of lecs){const n=B.filter(q=>q.l===l).length;if(!n)W(`lecture ${l} has no practice questions`);if(!G[l])W(`lecture ${l} has no study guide entry`);}
const bt=new Set(B.map(q=>q.q.trim().toLowerCase()));M.forEach((q,i)=>{if(bt.has(q.q.trim().toLowerCase()))E(`m${i} mock question copied from bank`);});
console.log(`bank ${B.length} · mock ${M.length} · errors ${err} · warnings ${warn}`);process.exit(err?1:0);
