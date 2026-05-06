const fs=require('fs');
const d=fs.readFileSync('C:/root/.openclaw/workspaces/mercadolibre/ml.txt','utf8');
// Try to find product titles from various patterns
const patterns=[
  /"title":"([^"]+)"/gi,
  /<title>([^<]+)<\/title>/gi,
  /class="item-title">([^<]+)</gi,
  /data-title="([^"]+)"/gi
];
patterns.forEach((p,i)=>{
  const m=d.match(p);
  if(m)console.log('Pattern '+i+':',m.slice(0,10).join('\n'));
});