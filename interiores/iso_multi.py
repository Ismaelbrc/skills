import json, math, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MPoly
import matplotlib.colors as mc

P1=(0.3,0.0); P2=(0.0,3.4); P3=(1.4,4.5); P4=(2.95,4.0); P5=(2.9,0.0); PTS=[P1,P2,P3,P4,P5]
SCENE=json.loads(open("/tmp/scene.json").read())
L=np.array([0.35,0.85,0.4]); L/=np.linalg.norm(L)
def shade(col,n):
    r,g,b=mc.to_rgb(col); n=np.array(n,float); nn=np.linalg.norm(n)
    if nn>0:n/=nn
    f=0.5+0.5*max(0,float(n@L)); return (min(1,r*f),min(1,g*f),min(1,b*f))

# coleta faces 3D uma vez: (pts3d, color, normal, alpha, edge, zbias)
RAW=[]
def face(pts,color,normal,alpha=1.0,edge='#2c2f3340',zbias=0.0): RAW.append((pts,color,normal,alpha,edge,zbias))
def box(x,z,w,d,h,lift,color,alpha=1.0):
    x0,x1=x,x+w; z0,z1=z,z+d; y0,y1=lift,lift+h
    c=[(x0,y0,z0),(x1,y0,z0),(x1,y0,z1),(x0,y0,z1),(x0,y1,z0),(x1,y1,z0),(x1,y1,z1),(x0,y1,z1)]
    face([c[4],c[5],c[6],c[7]],color,(0,1,0),alpha)
    face([c[0],c[1],c[5],c[4]],color,(0,0,-1),alpha)
    face([c[3],c[2],c[6],c[7]],color,(0,0,1),alpha)
    face([c[1],c[2],c[6],c[5]],color,(1,0,0),alpha)
    face([c[0],c[3],c[7],c[4]],color,(-1,0,0),alpha)
face([(p[0],0,p[1]) for p in PTS],"#c79c75",(0,1,0),1.0,'#8a6a48',0.05)
for w in SCENE["walls"]:
    a=(w["x1"],w["z1"]); b=(w["x2"],w["z2"]); h=w.get("h",2.6)
    if not((a[1]+b[1])/2>2.2 or (a[0]+b[0])/2>2.5): continue
    solid=len(w["openings"])==0; col="#e9e2d2" if solid else "#cfe8f3"; al=1.0 if solid else 0.4
    face([(a[0],0,a[1]),(b[0],0,b[1]),(b[0],h,b[1]),(a[0],h,a[1])],col,(b[1]-a[1],0,-(b[0]-a[0])),al,'#aaa',0.02)
for f in SCENE["furniture"]:
    box(f["x"],f["z"],f["w"],f["d"],f["h"],f.get("lift",0),f["color"],0.98)
    if f.get("top"): box(f["x"],f["z"],f["w"],f["d"],0.04,f["h"]+f.get("lift",0),f.get("topColor","#333"))

def render(ax,AZ,EL,title):
    AZ=math.radians(AZ); EL=math.radians(EL)
    def proj(p):
        x,y,z=p; x1=x*math.cos(AZ)+z*math.sin(AZ); z1=-x*math.sin(AZ)+z*math.cos(AZ)
        return (x1, y*math.cos(EL)+z1*math.sin(EL)), z1*math.cos(EL)-y*math.sin(EL)
    fs=[]
    for pts,color,normal,alpha,edge,zb in RAW:
        pr=[proj(p) for p in pts]; poly=[a[0] for a in pr]; dep=sum(a[1] for a in pr)/len(pr)+zb
        fs.append((dep,poly,shade(color,normal),edge,alpha))
    fs.sort(key=lambda t:-t[0])
    for dep,poly,fc,ec,al in fs: ax.add_patch(MPoly(poly,closed=True,facecolor=fc,edgecolor=ec,linewidth=0.4,alpha=al))
    xs=[p[0] for _,poly,_,_,_ in fs for p in poly]; ys=[p[1] for _,poly,_,_,_ in fs for p in poly]
    ax.set_xlim(min(xs)-0.2,max(xs)+0.2); ax.set_ylim(min(ys)-0.2,max(ys)+0.2)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_title(title,fontsize=11,weight='bold')

fig,axs=plt.subplots(1,3,figsize=(20,7)); fig.patch.set_facecolor("#eef1f3")
for a in axs: a.set_facecolor("#eef1f3")
render(axs[0],-35,28,"Vista geral (isométrica)")
render(axs[1],-8,16,"Da porta, olhando pra dentro")
render(axs[2],-40,66,"Quase de cima (planta baixa 3D)")
plt.tight_layout(); plt.savefig("/home/user/skills/interiores/saidas/varanda-render3d-angulos.png",dpi=115,bbox_inches='tight',facecolor="#eef1f3")
print("ok")
