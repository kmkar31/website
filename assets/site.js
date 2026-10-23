(function(){
  var d=document, root=d.documentElement;

  // theme toggle
  var tb=d.getElementById('theme');
  if(tb){tb.addEventListener('click',function(){
    var cur=root.getAttribute('data-theme');
    if(!cur){cur=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}
    var next=cur==='dark'?'light':'dark';
    root.setAttribute('data-theme',next);
    try{localStorage.setItem('theme',next)}catch(e){}
  });}

  // project filter, with a spoken result count
  var fs=d.querySelectorAll('.filter');
  if(fs.length){
    var rows=d.querySelectorAll('#project-list li'), empty=d.getElementById('empty'), live=d.getElementById('filter-status');
    fs.forEach(function(b){b.addEventListener('click',function(){
      fs.forEach(function(x){x.classList.remove('active');x.setAttribute('aria-pressed','false');});
      b.classList.add('active');b.setAttribute('aria-pressed','true');
      var f=b.getAttribute('data-filter'), shown=0;
      rows.forEach(function(c){
        var ok=f==='all'||(' '+c.getAttribute('data-tags')+' ').indexOf(' '+f+' ')>-1;
        c.hidden=!ok; if(ok){shown++;}
      });
      empty.hidden=shown>0;
      if(live){live.textContent='Showing '+shown+' of '+rows.length+' projects';}
    });});
  }

  // images that fail to load (e.g. a dead hotlink) drop out instead of leaving empty boxes
  function gone(i){var f=i.closest('figure');if(f){f.classList.add('broken-fig');var r=f.parentNode;if(r&&r.classList.contains('fig-row')&&!r.querySelector('figure:not(.broken-fig)')){r.style.display='none';}}}
  d.querySelectorAll('.about-top .portrait').forEach(function(i){
    function nop(){i.parentNode.classList.add('no-portrait');}
    if(i.complete&&i.naturalWidth===0){nop();}else{i.addEventListener('error',nop);}
  });
  d.querySelectorAll('.project figure img').forEach(function(i){
    if(i.complete&&i.naturalWidth===0){gone(i);}else{i.addEventListener('error',function(){gone(i);});}
  });

  // image lightbox: figure images are real links to the full image, so they work without JS
  var lb=d.getElementById('lightbox');
  if(lb){
    var lbi=lb.querySelector('img'), closeBtn=lb.querySelector('.lb-close'), opener=null;
    function close(){lb.hidden=true;if(opener){opener.focus();opener=null;}}
    d.addEventListener('click',function(e){
      var a=e.target.closest&&e.target.closest('.project a.zoom');
      if(a){e.preventDefault();opener=a;var im=a.querySelector('img');lbi.src=a.href;lbi.alt=im?im.alt:'';lb.hidden=false;closeBtn.focus();}
      else if(!lb.hidden){close();}
    });
    d.addEventListener('keydown',function(e){
      if(lb.hidden)return;
      if(e.key==='Escape'){close();}
      else if(e.key==='Tab'){e.preventDefault();closeBtn.focus();}
    });
  }
})();
