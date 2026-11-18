// Example Exam Lab dataset: every question shape, valid under scripts/check.js.
// Build it with:  python3 scripts/build.py assets/template.html assets/example-data.js demo.html
const CONFIG={
  course:"Intro to Psychology", exam:"Quiz 1",
  subtitle:"Lectures 1–2 · Example dataset · MCQ + T/F + written",
  lectures:[
    {id:"L1",name:"Perception",prio:"High"},
    {id:"L2",name:"Memory",prio:"Medium"}
  ],
  mock:{enabled:true,minutes:10},
  notes:["<mark>Highest weight</mark>: perception (L1)."],
  style:["4-option MCQ, a few True/False statements, one short written definition."],
  accent:null,
  storageKey:"examlab_example_psych_quiz1"
};

const B=[
{l:"L1",h:1,q:"Top-down processing in perception means that:",
 o:[["Expectations shape what we perceive","Correct: interpretation is guided by what we already know and expect."],
    ["Perception is built only from raw sensory input, step by step","That describes bottom-up processing, the opposite direction."],
    ["Sensory receptors adapt to a constant stimulus","That is sensory adaptation, a different concept from the same lecture."],
    ["Attention is limited to a single stimulus at a time","That is a claim about selective attention, not about processing direction."]],
 k:"Top-down = knowledge → perception; bottom-up = stimulus → perception."},
{l:"L1",t:"tf",q:"Statement: two people watching the same event always perceive it the same way.",
 o:[["False","Expectations and motives change what each observer notices and remembers."],["True","Not true: perception is an active interpretation, not a passive copy."]],
 k:"Perception is interpretation, so observers can legitimately differ."},
{l:"L2",q:"Which memory store holds information for only a fraction of a second to a few seconds?",
 o:[["Sensory memory","Correct: sensory memory holds a brief, high-capacity trace of the input."],
    ["Short-term memory","Short-term memory lasts around 20–30 seconds without rehearsal."],
    ["Long-term memory","Long-term memory is durable and has no practical time limit."],
    ["Procedural memory","Procedural memory is a type of long-term memory for skills."]],
 k:"Sensory → short-term → long-term, from shortest to longest duration."},
{l:"L2",t:"tf",q:"Statement: rehearsal helps move information from short-term to long-term memory.",
 o:[["True","Rehearsal, especially elaborative rehearsal, supports encoding into long-term memory."],["False","Not false: rehearsal is a standard route into long-term memory."]],
 k:"Rehearsal is the bridge from short-term to long-term memory."},
{l:"L2",t:"written",q:"Define encoding and give one example.",
 a:"<p><b>Encoding</b> is the process of converting information into a form that can be stored in memory.</p><p>Example: linking a new term to a vivid image so it is easier to remember later.</p>",
 k:"Encoding is the first stage: encoding → storage → retrieval."}
];

const M=[
{l:"L1",q:"A reader skims past a typo without noticing it. Which process best explains this?",
 o:[["Top-down processing","Correct: expectations make the reader see the intended word."],
    ["Bottom-up processing of each individual letter","Careful letter-by-letter processing would catch the typo."],
    ["Sensory adaptation to printed text","Adaptation is about constant stimuli fading, not about typos."],
    ["Retrieval failure from long-term memory","The word is recognised, so retrieval is not the issue."]],
 k:"Expectation can override the actual input."},
{l:"L2",t:"tf",q:"Statement: memory works like a video recording that can be replayed exactly.",
 o:[["False","Memory is reconstructive: recall rebuilds events and can change them."],["True","Not true: memories are reconstructed, not replayed."]],
 k:"Memory is reconstructive, not a recording."}
];

const G={
  L1:{pts:["<b>Top-down</b> vs <b>bottom-up</b> processing: direction of influence.","Perception is an active interpretation of sensory input."],
      traps:["Confusing sensory adaptation with top-down processing."]},
  L2:{pts:["Three stores: <b>sensory</b>, <b>short-term</b>, <b>long-term</b>.","Stages: encoding → storage → retrieval."],
      traps:["Treating memory as an exact recording."]}
};
