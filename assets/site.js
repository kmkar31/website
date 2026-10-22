(function(){
  var d=document, root=d.documentElement;
  root.classList.add('js');

  // theme toggle
  var tb=d.getElementById('theme');
  if(tb){tb.addEventListener('click',function(){
    var cur=root.getAttribute('data-theme');
    if(!cur){cur=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}
    var next=cur==='dark'?'light':'dark';
    root.setAttribute('data-theme',next);
    try{localStorage.setItem('theme',next)}catch(e){}
  });}

  // scroll reveal
  var els=[].slice.call(d.querySelectorAll('.reveal'));
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});
    },{rootMargin:'0px 0px -8% 0px',threshold:.05});
    els.forEach(function(el,i){el.style.transitionDelay=Math.min((i%6)*60,300)+'ms';io.observe(el);});
  } else { els.forEach(function(el){el.classList.add('in');}); }
  // safety net: never leave content hidden if the observer misses something
  setTimeout(function(){els.forEach(function(el){
    if(el.getBoundingClientRect().top<innerHeight*1.3){el.classList.add('in');}
  });},2500);
  addEventListener('load',function(){setTimeout(function(){els.forEach(function(el){
    if(el.getBoundingClientRect().top<innerHeight){el.classList.add('in');}
  });},300);});

  // project filter
  var fs=d.querySelectorAll('.filter');
  if(fs.length){
    var cards=d.querySelectorAll('#project-grid .card'), empty=d.getElementById('empty');
    fs.forEach(function(b){b.addEventListener('click',function(){
      fs.forEach(function(x){x.classList.remove('active');});
      b.classList.add('active');
      var f=b.getAttribute('data-filter'), shown=0;
      cards.forEach(function(c){
        var ok=f==='all'||(' '+c.getAttribute('data-tags')+' ').indexOf(' '+f+' ')>-1;
        c.hidden=!ok; if(ok){shown++;c.classList.add('in');}
      });
      empty.hidden=shown>0;
    });});
  }

  // image lightbox
  var lb=d.getElementById('lightbox');
  if(lb){
    var lbi=lb.querySelector('img');
    d.addEventListener('click',function(e){
      var t=e.target;
      if(t.tagName==='IMG'&&t.closest('.project figure')){lbi.src=t.src;lbi.alt=t.alt;lb.hidden=false;}
      else if(!lb.hidden){lb.hidden=true;}
    });
    d.addEventListener('keydown',function(e){if(e.key==='Escape'){lb.hidden=true;}});
  }
})();
