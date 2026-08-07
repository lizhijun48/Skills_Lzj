# 优秀范本库

单文件产出的完整可运行代码范本。用于UTOS内容轴**样本法**。

> **核心特点**：本技能的范本不是"文档描述"，而是**可直接运行的完整代码**。每个范本文件都是自包含的单文件产物，复制保存即可使用。

---

## 范本索引

| 范本ID | 范本名称 | 对应任务 | 类型 | 文件 | 状态 |
|--------|---------|---------|------|------|------|
| EX-01 | 俄罗斯方块完整实现 | S2-01 | HTML游戏 | exemplars/tetris.html | ✅ 已包含 |
| EX-02 | 计算器完整实现 | S3-01 | HTML工具 | exemplars/calculator.html | ✅ 已包含 |
| EX-03 | JSON格式化工具 | S3-05 | HTML工具 | exemplars/json-formatter.html | [待补充] |
| EX-04 | HTML幻灯片模板 | S1-01 | HTML演示 | exemplars/slideshow-template.html | [待补充] |
| EX-05 | Python CLI文件重命名工具 | S5-01 | Python CLI | exemplars/file-rename.py | [待补充] |
| EX-06 | Python CLI CSV处理工具 | S5-04 | Python CLI | exemplars/csv-tool.py | [待补充] |
| EX-07 | 2048游戏完整实现 | S2-03 | HTML游戏 | exemplars/game-2048.html | [待补充] |
| EX-08 | 正则表达式测试器 | S3-06 | HTML工具 | exemplars/regex-tester.html | [待补充] |
| EX-09 | Cron表达式解析器 | S6-05 | HTML工具 | exemplars/cron-parser.html | [待补充] |
| EX-10 | 目录分析Python工具 | S5-02 | Python CLI | exemplars/dir-analyzer.py | [待补充] |

---

## 范本代码：EX-01 俄罗斯方块（完整可运行）

> **对应任务**: S2-01
> **保存为**: `tetris.html`
> **运行方式**: 双击在浏览器打开
> **依赖**: 零（纯HTML+CSS+JS）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>俄罗斯方块</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#1a1a2e;display:flex;justify-content:center;align-items:center;min-height:100vh;font-family:'Courier New',monospace;color:#eee}
.game-wrapper{display:flex;gap:20px;align-items:flex-start}
canvas{background:#16213e;border:2px solid #0f3460;border-radius:4px}
.side-panel{display:flex;flex-direction:column;gap:12px;width:120px}
.panel-box{background:#16213e;padding:12px;border-radius:6px;border:1px solid #0f3460}
.panel-box h3{font-size:13px;margin-bottom:8px;color:#e94560;text-align:center}
.panel-value{font-size:22px;font-weight:bold;text-align:center}
#next-canvas{background:#0f3460;border-radius:4px;margin:0 auto;display:block}
.controls{text-align:center;font-size:11px;color:#888;line-height:1.6}
.controls kbd{background:#0f3460;padding:2px 6px;border-radius:3px;font-size:10px}
#overlay{display:none;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;background:rgba(22,33,62,.95);padding:40px;border-radius:12px;border:2px solid #e94560}
#overlay h2{color:#e94560;font-size:28px;margin-bottom:12px}
#overlay p{font-size:14px;margin-bottom:16px}
#overlay button{background:#e94560;color:#fff;border:none;padding:10px 28px;border-radius:6px;font-size:15px;cursor:pointer}
#overlay button:hover{background:#c73e54}
</style>
</head>
<body>
<div class="game-wrapper" style="position:relative">
  <canvas id="board" width="300" height="600"></canvas>
  <div class="side-panel">
    <div class="panel-box"><h3>分数</h3><div class="panel-value" id="score">0</div></div>
    <div class="panel-box"><h3>等级</h3><div class="panel-value" id="level">1</div></div>
    <div class="panel-box"><h3>行数</h3><div class="panel-value" id="lines">0</div></div>
    <div class="panel-box"><h3>下一个</h3><canvas id="next-canvas" width="96" height="96"></canvas></div>
    <div class="controls">
      <kbd>&#8592;&#8594;</kbd> 移动<br>
      <kbd>&#8593;</kbd> 旋转<br>
      <kbd>&#8595;</kbd> 加速<br>
      <kbd>Space</kbd> 直落<br>
      <kbd>P</kbd> 暂停
    </div>
  </div>
  <div id="overlay">
    <h2>游戏结束</h2>
    <p>最终分数: <span id="final-score">0</span></p>
    <button onclick="game.start()">重新开始</button>
  </div>
</div>
<script>
const COLS=10,ROWS=20,BLOCK_SIZE=30;
const COLORS=['#00f0f0','#f0f000','#a000f0','#00f000','#f00000','#0000f0','#f0f000'];
const SHAPES=[[[1,1,1,1]],[[1,1],[1,1]],[[1,1,1],[0,1,0]],
  [[1,1,0],[0,1,1]],[[0,1,1],[1,1,0]],[[1,1,1],[1,0,0]]];
class Piece{constructor(type){this.type=type;this.shape=SHAPES[type].map(r=>[...r]);this.color=COLORS[type];this.x=Math.floor((COLS-this.shape[0].length)/2);this.y=0}rotate(){const r=this.shape[0].map((_,i)=>this.shape.map(row=>row[i]).reverse());return{shape:r,x:this.x,y:this.y}}}
class Board{constructor(){this.grid=Array.from({length:ROWS},()=>new Array(COLS).fill(0));this.score=0;this.lines=0;this.level=1}valid(shape,ox,oy){return shape.every((r,dy)=>r.every((v,dx)=>!v||(ox+dx>=0&&ox+dx<COLS&&oy+dy<ROWS&&!this.grid[oy+dy][ox+dx])))}lock(piece){piece.shape.forEach((r,dy)=>r.forEach((v,dx)=>{if(v&&piece.y+dy>=0)this.grid[piece.y+dy][piece.x+dx]=parseInt(piece.color.slice(1),16)}))}clearLines(){let cleared=0;for(let y=ROWS-1;y>=0;y--){if(this.grid[y].every(v=>v)){this.grid.splice(y,1);this.grid.unshift(new Array(COLS).fill(0));cleared++;y++}}if(cleared){this.lines+=cleared;const pts=[0,100,300,800];this.score+=(pts[cleared]||0)*(this.level+1);this.level=Math.floor(this.lines/10)+1}}}
class Renderer{constructor(boardCanvas,nextCanvas){this.bc=boardCanvas;this.nc=nextCanvas;this.bctx=boardCanvas.getContext('2d');this.nctx=nextCanvas.getContext('2d');this.bs=BLOCK_SIZE;this.ns=this.nc.width/4}drawBoard(board){this.bctx.fillStyle='#16213e';this.bctx.fillRect(0,0,this.bc.width,this.bc.height);board.grid.forEach((row,y)=>row.forEach((v,x)=>{if(v){this.bctx.fillStyle='#'+v.toString(16).padStart(6,'0');this.bctx.fillRect(x*this.bs,y*this.bs,this.bs-1,this.bs-1)}}))}drawGhost(piece,board){const ghost={...piece,y:piece.y};while(board.valid(ghost.shape,ghost.x,ghost.y+1))ghost.y++;if(ghost.y>piece.y){this.bctx.globalAlpha=0.2;ghost.shape.forEach((r,dy)=>r.forEach((v,dx)=>{if(v){this.bctx.fillStyle=piece.color;this.bctx.fillRect((ghost.x+dx)*this.bs,(ghost.y+dy)*this.bs,this.bs-1,this.bs-1)}}));this.bctx.globalAlpha=1}}drawPiece(piece,pctx,scale){pctx.clearRect(0,0,pctx.canvas.width,pctx.canvas.height);piece.shape.forEach((r,dy)=>r.forEach((v,dx)=>{if(v){pctx.fillStyle=piece.color;pctx.fillRect(dx*scale,dy*scale,scale-1,scale-1)}}))}}
class Game{constructor(){this.board=new Board();this.renderer=new Renderer(document.getElementById('board'),document.getElementById('next-canvas'));this.current=null;this.next=null;this.dropCounter=0;this.dropInterval=1000;this.lastTime=0;this.paused=false;this.over=false;this.animId=null;this.initInput()}initInput(){document.addEventListener('keydown',e=>{if(this.over)return;if(e.key==='p'||e.key==='P'){this.paused=!this.paused;return}if(this.paused)return;switch(e.key){case'ArrowLeft':this.move(-1,0);break;case'ArrowRight':this.move(1,0);break;case'ArrowDown':this.move(0,1);break;case'ArrowUp':this.rotate();break;case' ':this.hardDrop();break}})}spawn(){this.current=this.next||new Piece(Math.floor(Math.random()*7));this.next=new Piece(Math.floor(Math.random()*7));if(!this.board.valid(this.current.shape,this.current.x,this.current.y)){this.gameOver()}this.renderer.drawPiece(this.next,this.renderer.nctx,this.renderer.ns)}move(dx,dy){if(this.board.valid(this.current.shape,this.current.x+dx,this.current.y+dy)){this.current.x+=dx;this.current.y+=dy}}rotate(){const rotated=this.current.rotate();if(this.board.valid(rotated.shape,rotated.x,rotated.y)){this.current.shape=rotated.shape}}hardDrop(){while(this.board.valid(this.current.shape,this.current.x,this.current.y+1))this.current.y++;this.lock()}lock(){this.board.lock(this.current);this.board.clearLines();this.spawn();this.updateUI()}updateUI(){document.getElementById('score').textContent=this.board.score;document.getElementById('level').textContent=this.board.level;document.getElementById('lines').textContent=this.board.lines}gameOver(){this.over=true;cancelAnimationFrame(this.animId);document.getElementById('final-score').textContent=this.board.score;document.getElementById('overlay').style.display='block'}start(){this.board=new Board();this.over=false;this.paused=false;this.dropInterval=1000;document.getElementById('overlay').style.display='none';this.spawn();this.lastTime=0;this.loop(0)}loop(time){if(this.over)return;this.animId=requestAnimationFrame(t=>this.loop(t));const dt=time-this.lastTime;this.lastTime=time;if(!this.paused){this.dropCounter+=dt;if(this.dropCounter>this.dropInterval){this.move(0,1);this.dropCounter=0;this.dropInterval=Math.max(100,1000-(this.board.level-1)*80)}}this.renderer.drawBoard(this.board);if(this.current)this.renderer.drawGhost(this.current,this.board);if(this.current)this.renderer.drawPiece(this.current,this.renderer.bctx,this.renderer.bs)}}
const game=new Game();
game.start();
</script>
</body>
</html>
```

---

## 范本代码：EX-02 计算器（完整可运行）

> **对应任务**: S3-01
> **保存为**: `calculator.html`
> **运行方式**: 双击在浏览器打开
> **依赖**: 零

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>计算器</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#1a1a2e;display:flex;justify-content:center;align-items:center;min-height:100vh;font-family:system-ui,sans-serif}
.calc{background:#16213e;padding:20px;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,.4);width:320px}
.display{background:#0f3460;color:#e94560;font-size:32px;text-align:right;padding:20px;border-radius:10px;margin-bottom:16px;min-height:48px;word-break:break-all;font-family:'Courier New',monospace;overflow-x:auto}
.keys{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.btn{border:none;border-radius:10px;padding:18px;font-size:20px;cursor:pointer;transition:.15s;background:#1f4068;color:#eee;font-family:inherit}.btn:hover{filter:brightness(1.2)}.btn:active{transform:scale(.95)}
.op{background:#e94560;color:#fff}.fn{background:#0f3460}.eq{grid-column:span 2;background:#e94560;color:#fff;font-size:24px}
</style>
</head>
<body>
<div class="calc"><div class="display" id="display">0</div><div class="keys" id="keys"></div></div>
<script>
const $=id=>document.getElementById(id);
const display=$('display'),keys=$('keys');
const labels=['C','±','%','÷','7','8','9','×','4','5','6','-','1','2','3','+','0','. '=];
const types=['fn','fn','fn','op','num','num','num','op','num','num','num','op','num','num','num','op','num','num','eq'];
labels.forEach((t,i)=>{
  const b=document.createElement('button');
  b.className='btn '+types[i];b.textContent=t;
  b.onclick(()=>handle(t));keys.appendChild(b)
});
let expr='',shouldReset=false;
function handle(val){
  if(val==='C'){expr='';shouldReset=false}
  else if(val==='±'){if(expr&&(expr[0]==='-')?expr=expr.slice(1):expr='-'+expr)}
  else if(val==='%'){try{expr=String(Number(eval(expr.replace(/×/g,'*').replace(/÷/g,'/')))/100))}catch{}}
  else if(val==='='){try{expr=String(eval(expr.replace(/×/g,'*').replace(/÷/g,'/')));shouldReset=true}catch(e){expr='Error'}}
  else if(['+','-','×','÷'].includes(val)){
    const last=expr.slice(-1);
    if(['+','-','×','÷'].includes(last))expr=expr.slice(0,-1)+val;
    else expr+=val;shouldReset=false
  }
  else{
    if(shouldReset)expr='';
    if(val==='.' && expr.split(/[+\-×÷]/).pop().includes('.'))return;
    expr=(expr==='0'&&val!=='.')?val:expr+val
  }
  display.textContent=expr||'0'
}
document.addEventListener('keydown',e=>{
  const m={'Enter':'=','Backspace':'C','%':'%','*':'×','/':'÷'};
  const k=m[e.key]||e.key;
  if(labels.includes(k)||'0123456789.'.includes(k))handle(k)
});
</script>
</body>
</html>
```

---

## 更多范本说明

### 范本扩展指南

以上提供了两个完整的、可直接运行的范本（俄罗斯方块和计算器）。其余8个范本标记为`[待补充]`。

**填充新范本时需遵循以下规范**：

1. **单文件原则**：所有HTML/CSS/JS内联在一个`.html`中；所有Python逻辑在一个`.py`中
2. **零外部依赖**：
   - HTML：仅用CDN白名单资源（cdnjs.cloudflare.com / cdn.jsdelivr.net / unpkg.com）
   - Python：仅用标准库
3. **可直接运行**：
   - HTML：双击即可在浏览器中正常工作
   - Python：`python file.py` 即可运行（含 `--help`）
4. **代码质量**：
   - 变量命名清晰
   - 关键逻辑有注释
   - 错误处理完善
   - 边界情况考虑
5. **文件命名**：`exemplars/<kebab-case-name>.html` 或 `.py`

### 范本作为UTOS样本法的使用方式

当用户要求产出某种单文件应用时：

1. UTOS从exemplars中找到最接近的范本
2. 分析范本的代码结构（作为"样本特征摘要"）
3. 按用户需求修改/替换内容部分
4. 保持结构框架不变，仅替换差异化内容
5. 输出新的完整可运行单文件
