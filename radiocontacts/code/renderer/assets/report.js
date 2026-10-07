'use strict';
const plotSpecs = JSON.parse(document.getElementById('plot-data').textContent);
const sections = [...document.querySelectorAll('main > section')];
const toc = document.getElementById('toc');
let presentation = new URLSearchParams(location.search).get('view') === 'presentation';
let current = 0;
let slides = [];

function renderPlot(host, variant) {
  const canvas = host.querySelector('.plot-canvas');
  const layout = {paper_bgcolor:'white', plot_bgcolor:'white', font:{family:'Arial, sans-serif',size:14,color:'#172e38'}, margin:{l:72,r:28,t:35,b:65}, autosize:true, hovermode:'closest', ...variant.layout};
  Plotly.react(canvas, variant.data, layout, {responsive:true,displaylogo:false,scrollZoom:false,modeBarButtonsToRemove:['lasso2d','select2d','toImage']});
  host.querySelector('.plot-caption').textContent = variant.caption;
  const rows = [['Series',variant.layout.xaxis?.title?.text || 'Category',variant.layout.yaxis?.title?.text || 'Value','Context']];
  variant.data.filter(trace => !trace.meta?.excludeTable).forEach(trace => {
    (trace.x || []).forEach((x,i) => rows.push([trace.name || '',x,trace.y?.[i] ?? '',trace.hovertext?.[i] ?? '']));
  });
  const table = host.querySelector('table');
  table.replaceChildren();
  const head = document.createElement('thead'), body = document.createElement('tbody');
  rows.forEach((row,i) => {const tr=document.createElement('tr'); row.forEach(value=>{const cell=document.createElement(i===0?'th':'td');cell.textContent=String(value);if(i===0)cell.scope='col';tr.append(cell)});(i===0?head:body).append(tr)});
  table.append(head,body);
  const download=host.querySelector('[download]');
  if(download.dataset.blob)URL.revokeObjectURL(download.dataset.blob);
  const csv=rows.map(row=>row.map(value=>'"'+String(value).replaceAll('"','""')+'"').join(',')).join('\n');
  const url=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));
  download.href=url;download.dataset.blob=url;
}

document.querySelectorAll('[data-plot]').forEach(host => {
  const variants=plotSpecs[host.dataset.plot], keys=Object.keys(variants);
  if(!keys.length)throw new Error('Empty figure: '+host.dataset.plot);
  host.classList.add('plot-shell');
  const tools=document.createElement('div');tools.className='plot-tools';
  const label=document.createElement('label');label.textContent='View';label.htmlFor='select-'+host.dataset.plot;
  const select=document.createElement('select');select.id=label.htmlFor;
  keys.forEach(key=>{const option=document.createElement('option');option.value=key;option.textContent=variants[key].label;select.append(option)});
  tools.append(label,select);if(keys.length===1)tools.hidden=true;
  const canvas=document.createElement('div');canvas.className='plot-canvas';canvas.setAttribute('role','img');canvas.setAttribute('aria-label',variants[keys[0]].label+'; exact values in the data table below');
  const caption=document.createElement('p');caption.className='plot-caption';caption.setAttribute('aria-live','polite');
  const details=document.createElement('details');details.className='doc-only';
  const summary=document.createElement('summary');summary.textContent='View data and download CSV';
  const download=document.createElement('a');download.download=host.dataset.plot+'.csv';download.textContent='Download displayed data';
  const wrap=document.createElement('div');wrap.className='table-wrap';const table=document.createElement('table');wrap.append(table);details.append(summary,download,wrap);
  host.append(tools,canvas,caption,details);
  select.addEventListener('change',()=>{canvas.setAttribute('aria-label',variants[select.value].label+'; exact values in the data table below');renderPlot(host,variants[select.value])});
  renderPlot(host,variants[keys[0]]);
});

function applyMode(anchor) {
  document.body.classList.toggle('presentation',presentation);
  document.getElementById('document-mode').setAttribute('aria-pressed',String(!presentation));
  document.getElementById('presentation-mode').setAttribute('aria-pressed',String(presentation));
  document.getElementById('slide-controls').hidden=!presentation;
  const cited=new Set([...document.querySelectorAll('[data-cite]')].filter(el=>!presentation || !el.closest('.prose,.doc-only,[data-document-only]')).map(el=>el.dataset.cite));
  document.querySelectorAll('[data-reference]').forEach(el=>el.hidden=!cited.has(el.dataset.reference));
  slides=sections.filter(section=>!presentation || (!section.matches('.prose,.doc-only,[data-document-only]') && (section.id!=='bibliography'||cited.size>0)));
  const selected=slides.findIndex(section=>section.id===anchor);
  current=selected>=0?selected:Math.min(current,slides.length-1);
  toc.replaceChildren();
  slides.forEach(section=>{const link=document.createElement('a');link.href='#'+section.id;link.textContent=section.querySelector('h2').textContent;toc.append(link)});
  showSlide(false);
}

function showSlide(scroll=true) {
  sections.forEach(section=>section.hidden=presentation && section!==slides[current]);
  if(presentation && slides[current]){
    document.getElementById('slide-status').textContent=`${current+1} / ${slides.length} · ${slides[current].querySelector('h2').textContent}`;
    if(location.protocol!=='file:')history.replaceState(null,'',`?view=presentation#${slides[current].id}`);
  }
  document.getElementById('previous').disabled=current===0;
  document.getElementById('next').disabled=current===slides.length-1;
  requestAnimationFrame(()=>document.querySelectorAll('.plot-canvas').forEach(el=>{if(el.getClientRects().length)Plotly.Plots.resize(el)}));
  if(scroll)window.scrollTo({top:0,behavior:'instant'});
}

document.getElementById('presentation-mode').addEventListener('click',()=>{
  const visible=sections.filter(section=>section.getBoundingClientRect().bottom>120).sort((a,b)=>Math.abs(a.getBoundingClientRect().top-100)-Math.abs(b.getBoundingClientRect().top-100))[0];
  presentation=true;applyMode(visible?.id);window.scrollTo(0,0);
});
document.getElementById('document-mode').addEventListener('click',()=>{
  const anchor=slides[current]?.id;presentation=false;applyMode(anchor);if(location.protocol!=='file:')history.replaceState(null,'',location.pathname+'#'+anchor);document.getElementById(anchor)?.scrollIntoView();
});
document.getElementById('previous').addEventListener('click',()=>{current=Math.max(0,current-1);showSlide()});
document.getElementById('next').addEventListener('click',()=>{current=Math.min(slides.length-1,current+1);showSlide()});
document.addEventListener('keydown',event=>{
  if(!presentation||event.altKey||event.ctrlKey||event.metaKey||event.target.closest('input,select,textarea,button,a,[contenteditable]'))return;
  if(['ArrowRight','PageDown','ArrowLeft','PageUp','Home','End'].includes(event.key)){
    event.preventDefault();current=event.key==='Home'?0:event.key==='End'?slides.length-1:Math.max(0,Math.min(slides.length-1,current+(['ArrowRight','PageDown'].includes(event.key)?1:-1)));showSlide();
  }
});
document.addEventListener('click',event=>{
  const link=event.target.closest('a[href^="#"]');if(!link)return;
  const target=document.getElementById(link.getAttribute('href').slice(1));if(!target)return;
  if(presentation){const index=slides.indexOf(target.closest('section'));if(index>=0){event.preventDefault();current=index;showSlide();target.scrollIntoView({block:'start'})}}
});
applyMode(location.hash.slice(1));
