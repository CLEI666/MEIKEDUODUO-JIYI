const fs=require('fs');
const d=fs.readFileSync('C:/root/.openclaw/workspaces/mercadolibre/ml2.txt','utf8');
// Search for bestseller items - ML uses li items with positions
const lines=d.split('\n');
const itemLines=lines.filter(l=>l.includes('item_id')||l.includes('product-id')||l.includes('"id":"MLM'));
console.log('Found',itemLines.length,'item lines');
if(itemLines.length>0)console.log(itemLines.slice(0,5).join('\n'));
// Also try JSON search
const jsonMatch=d.match(/\{.*?"item_id".*?\}/g);
if(jsonMatch)console.log('JSON items:',jsonMatch.slice(0,5));
// Find prices
const priceMatch=d.match(/"price":[0-9]+/gi);
if(priceMatch)console.log('prices found:',priceMatch.slice(0,10).join('\n'));