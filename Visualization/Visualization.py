import tkinter as tk
from tkinter import *
from PIL import ImageTk
import time


fin = open("dataall.txt",'r')

# set time slicing
delay = 0.001
# set radius of circle
rad = 10

t= 0 # for zone remain counter
user =[]
times = []
userID = []
zone = []
fence = []
rtime = []
coords = []
sex = []
age = []

remain = dict()
remain = {1 : 0, 2 : 0, 3 : 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
remaind = dict()
remaind = {1 : 0, 2 : 0, 3 : 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
remainp = dict()
remainp = {1 : 0, 2 : 0, 3 : 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
remainj = dict()
remainj = {1 : 0, 2 : 0, 3 : 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
remainv = dict()
remainv = {1 : 0, 2 : 0, 3 : 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
remaini = dict()
remaini = {1 : 0, 2 : 0, 3 : 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
remainb = dict()
remainb = {1 : 0, 2 : 0, 3 : 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
remainu = dict()
remainu = {1 : 0, 2 : 0, 3 : 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
remains = dict()
remains = {1 : 0, 2 : 0, 3 : 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

x_mul = 760/120
y_mul = 450/70

line = fin.readline().strip().split("\t")

while(1):
    factor = fin.readline()
    factor_string = factor.strip().split("\t")
    if not factor:
        break
    if not userID:
        userID.append(factor_string[0])
    else :
        if userID[-1] != factor_string[0] :
            userID.append(factor_string[0])
    userID.append(factor_string[0])
    times.append(factor_string[1])
    zone.append(factor_string[2])
    fence.append(factor_string[3])
    age.append(factor_string[4])
    sex.append(factor_string[5])
    rtime.append(factor_string[6])
    
total = len(fence)

print(total)

root = tk.Tk()
root.title("Waterpark mapping")
canvas = tk.Canvas(root, width = 1600, height = 620, borderwidth = 0,bg ="white")
canvas.grid()

image = ImageTk.PhotoImage(file = "MAP.PNG")
canvas.create_image(0,0,image= image, anchor = NW)


l = Label(canvas, text = "Y")
l.place(x= 20, y = 38)

l = Label(canvas, text = "X")
l.place(x= 1550, y = 430)

ppd = 10
ppp = 10
ppj = 10
ppv = 10
ppi = 10
ppb = 10
ppu = 10
pps = 10

lastID = "아이디"
print(lastID)
lastfence = "하위"

lasttimed = 0
lasttimep = 0
lasttimej = 0
lasttimev = 0
lasttimei = 0
lasttimeb = 0
lasttimeu = 0
lasttimes = 0

dp=1
dj=1
dv=1
di=1
db=1
du=1
ds=1

pd=1
pj=1
pv=1
pi=1
pb=1
pu=1
ps=1

jd=1
jp=1
jv=1
ji=1
jb=1
ju=1
js=1

vd=1
vj=1
vp=1
vi=1
vb=1
vu=1
vs=1

iid=1
ij=1
iv=1
ip=1
ib=1
iu=1
iis=1

bd=1
bp=1
bj=1
bv=1
bi=1
bu=1
bs=1

ud=1
up=1
uj=1
uv=1
ui=1
ub=1
us=1

sd=1
sp=1
sj=1
sv=1
si=1
sb=1
su=1

lasttimed2 = 0
lasttimep2 = 0
dp2=1
pd2=1

num = 0;
num2 = 1;
ak = 0;
maxc = 0;
maxl = 0;


canvas.create_oval(140, 225, 160, 245, fill = "green")
canvas.create_oval(230, 335, 250, 355, fill = "black")


for i in range(total):
    asdf=0
    if(asdf==0):
        if(ak==0):
            print(ak)
            ak = 1
            num = num +1
            print(num)
        lasttime = int(rtime[i])
        if(fence[i]=="돌핀키즈존"):
            lasttimed2 = lasttimed2 + int(rtime[i])
            if(lastfence=="파도풀"):
                  dp2 = dp2 + 0.1
        if(fence[i]=="파도풀"):
            lasttimep2 = lasttimep2 + int(rtime[i])
            if(lastfence=="돌핀키즈존"):
                  pd2 = pd2 +0.1
    elif(lastfence!=fence[i]):
        ak =0;
    lastfence = fence[i]
maxc = max(lasttimed2, lasttimep2)
maxl = max(dp2, pd2)

for i in range(total):
    asdf=0
    if(asdf==0):
        if(ak==0):
            print(ak)
            ak = 1
            num = num +1
            print(num)
        lasttime = int(rtime[i])
        if(fence[i]=="돌핀키즈존"):
            lasttimed = lasttimed + int(rtime[i])
            #ppd = ppd + lasttimed/150000
            if(lastfence=="파도풀"):
                  dp = dp + 0.1
                  remaind[2] += 1
            if(lastfence=="정규풀"):
                  dj = dj +0.1
                  remaind[3] +=1
            if(lastfence=="바데풀"):
                  dv = dv + 0.1
                  remaind[4] += 1
            if(lastfence=="아일랜드"):
                  di = di +0.1
                  remaind[5] +=1
            if(lastfence=="블루스파"):
                  db = db +0.1
                  remaind[6] +=1
            if(lastfence=="유수풀"):
                  du = du +0.1
                  remaind[7] +=1
            if(lastfence=="스플래시 키즈존"):
                  ds = ds +0.1
                  remaind[8] +=1
            remain[1] += 1
        if(fence[i]=="파도풀"):
            lasttimep = lasttimep + int(rtime[i])  
            #ppp = ppp + lasttimep/150000
            if(lastfence=="돌핀키즈존"):
                  pd = pd +0.1
                  remainp[1] += 1
            if(lastfence=="정규풀"):
                  pj = pj +0.1
                  remainp[3] +=1
            if(lastfence=="바데풀"):
                  pv = pv + 0.1
                  remainp[4] += 1
            if(lastfence=="아일랜드"):
                  pi = pi + 0.1
                  remainp[5] +=1
            if(lastfence=="블루스파"):
                  pb = pb + 0.1
                  remainp[6] +=1
            if(lastfence=="유수풀"):
                  pu = pu +0.1
                  remainp[7] +=1
            if(lastfence=="스플래시 키즈존"):
                  ps = ps +0.1
                  remainp[8] +=1
            remain[2] +=1
        if(fence[i]=="정규풀"):
            lasttimej = lasttimej + int(rtime[i])
            #ppj = ppj + lasttimej/20000
            if(lastfence=="돌핀키즈존"):
                  jd = jd +0.1
                  remainj[1] +=1
            if(lastfence=="파도풀"):
                  jp = jp +0.1
                  remainj[2] +=1
            if(lastfence=="바데풀"):
                  jv = jv + 0.1
                  remainj[4] += 1
            if(lastfence=="아일랜드"):
                  ji = ji + 0.1
                  remainj[5] +=1
            if(lastfence=="블루스파"):
                  jb = jb + 0.1
                  remainj[6] +=1
            if(lastfence=="유수풀"):
                  ju = ju +0.1
                  remainj[7] +=1
            if(lastfence=="스플래시 키즈존"):
                  js = js +0.1
                  remainj[8] +=1
            remain[3] +=1
        if(fence[i]=="바데풀"):
            lasttimev = lasttimev + int(rtime[i])
            #ppv = ppv + lasttimev/20000
            if(lastfence=="돌핀키즈존"):
                  vd = vd +0.1
                  remainv[1] +=1
            if(lastfence=="파도풀"):
                  vp = vp +0.1
                  remainv[2] +=1
            if(lastfence=="정규풀"):
                  vj = vj + 0.1
                  remainv[3] += 1
            if(lastfence=="아일랜드"):
                  vi = vi + 0.1
                  remainv[5] +=1
            if(lastfence=="블루스파"):
                  vb = vb + 0.1
                  remainv[6] +=1
            if(lastfence=="유수풀"):
                  vu = vu +0.1
                  remainv[7] +=1
            if(lastfence=="스플래시 키즈존"):
                  vs = vs +0.1
                  remainv[8] +=1
            remain[4] +=1
        if(fence[i]=="아일랜드"):
            lasttimei = lasttimei + int(rtime[i])
            #ppi = ppi + lasttimei/20000
            if(lastfence=="돌핀키즈존"):
                  iid = iid +0.1
                  remaini[1] +=1
            if(lastfence=="파도풀"):
                  ip = ip +0.1
                  remaini[2] +=1
            if(lastfence=="정규풀"):
                  ij = ij + 0.1
                  remaini[3] += 11
            if(lastfence=="바데풀"):
                  iv = iv +0.1
                  remaini[4] +=1
            if(lastfence=="블루스파"):
                  ib = ib + 0.1
                  remaini[6] +=1
            if(lastfence=="유수풀"):
                  iu = iu +0.1
                  remaini[7] +=1
            if(lastfence=="스플래시 키즈존"):
                  iis = iis +0.1
                  remaini[8] +=1
            remain[5] +=1
        if(fence[i]=="블루스파"):
            lasttimeb = lasttimeb + int(rtime[i])
            #ppb = ppb +lasttimeb/20000
            if(lastfence=="돌핀키즈존"):
                  bd = bd +0.1
                  remainb[1] +=1
            if(lastfence=="파도풀"):
                  bp = bp + 0.1
                  remainb[2] +=1
            if(lastfence=="정규풀"):
                  bj = bj + 0.1
                  remainb[3] += 1
            if(lastfence=="바데풀"):
                  bv = bv + 0.1
                  remainb[4] +=1
            if(lastfence=="아일랜드"):
                  bi = bi + 0.1
                  remainb[5] +=1
            if(lastfence=="유수풀"):
                  bu = bu +0.1
                  remainb[7] +=1
            if(lastfence=="스플래시 키즈존"):
                  bs = bs +0.1
                  remainb[8] +=1
            remain[6] +=1
        if(fence[i]=="유수풀"):
            lasttimeu = lasttimeu + int(rtime[i])
            #ppb = ppb +lasttimeb/20000
            if(lastfence=="돌핀키즈존"):
                  ud = ud +0.1
                  remainu[1] +=1
            if(lastfence=="파도풀"):
                  up = up + 0.1
                  remainu[2] +=1
            if(lastfence=="정규풀"):
                  uj = uj + 0.1
                  remainu[3] += 1
            if(lastfence=="바데풀"):
                  uv = uv + 0.1
                  remainu[4] +=1
            if(lastfence=="아일랜드"):
                  ui = ui + 0.1
                  remainu[5] +=1
            if(lastfence=="블루스파"):
                  ub = ub +0.1
                  remainu[6] +=1
            if(lastfence=="스플래시 키즈존"):
                  us = us +0.1
                  remainu[8] +=1
            remain[7] +=1
        if(fence[i]=="스플래시 키즈존"):
            lasttimes = lasttimes + int(rtime[i])
            #ppb = ppb +lasttimeb/20000
            if(lastfence=="돌핀키즈존"):
                  sd = sd +0.1
                  remains[1] +=1
            if(lastfence=="파도풀"):
                  sp = sp + 0.1
                  remains[2] +=1
            if(lastfence=="정규풀"):
                  sj = sj + 0.1
                  remains[3] += 1
            if(lastfence=="바데풀"):
                  sv = sv + 0.1
                  remains[4] +=1
            if(lastfence=="아일랜드"):
                  si = si + 0.1
                  remains[5] +=1
            if(lastfence=="블루스파"):
                  sb = sb +0.1
                  remains[6] +=1
            if(lastfence=="유수풀"):
                  su = su +0.1
                  remains[7] +=1
            remain[8] +=1
      
    elif(lastfence!=fence[i]):
        ak =0;
    lastfence = fence[i]

   
    ppd = (65*lasttimed)/maxc
    ppp = (65*lasttimep)/maxc
    ppj = (65*lasttimej)/maxc
    ppv = (65*lasttimev)/maxc
    ppi = (65*lasttimei)/maxc
    ppb = (65*lasttimeb)/maxc
    ppu = (65*lasttimeu)/maxc
    pps = (65*lasttimes)/maxc
    
    dpf=(19*dp)/maxl+1
    djf=(19*dj)/maxl+1
    dvf=(19*dv)/maxl+1
    dif=(19*di)/maxl+1
    dbf=(19*db)/maxl+1
    duf=(19*du)/maxl+1
    dsf=(19*ds)/maxl+1
    
    pdf=(19*pd)/maxl+1
    pjf=(19*pj)/maxl+1
    pvf=(19*pv)/maxl+1
    pif=(19*pi)/maxl+1
    pbf=(19*pb)/maxl+1
    puf=(19*pu)/maxl+1
    psf=(19*ps)/maxl+1
    
    jdf=(19*jd)/maxl+1
    jpf=(19*jp)/maxl+1
    jvf=(19*jv)/maxl+1
    jif=(19*ji)/maxl+1
    jbf=(19*jb)/maxl+1
    juf=(19*ju)/maxl+1
    jsf=(19*js)/maxl+1
    
    vdf=(19*vd)/maxl+1
    vjf=(19*vj)/maxl+1
    vpf=(19*vp)/maxl+1
    vif=(19*vi)/maxl+1
    vbf=(19*vb)/maxl+1
    vuf=(19*vu)/maxl+1
    vsf=(19*vs)/maxl+1
    
    iidf=(19*iid)/maxl+1
    ijf=(19*ij)/maxl+1
    ivf=(19*iv)/maxl+1
    ipf=(19*ip)/maxl+1
    ibf=(19*ib)/maxl+1
    iuf=(19*iu)/maxl+1
    iisf=(19*iis)/maxl+1
    
    bdf=(19*bd)/maxl+1
    bpf=(19*bp)/maxl+1
    bjf=(19*bj)/maxl+1
    bvf=(19*bv)/maxl+1
    bif=(19*bi)/maxl+1
    buf=(19*bu)/maxl+1
    bsf=(19*bs)/maxl+1

    udf=(19*ud)/maxl+1
    upf=(19*up)/maxl+1
    ujf=(19*uj)/maxl+1
    uvf=(19*uv)/maxl+1
    uif=(19*ui)/maxl+1
    ubf=(19*ub)/maxl+1
    usf=(19*us)/maxl+1

    sdf=(19*sd)/maxl+1
    spf=(19*sp)/maxl+1
    sjf=(19*sj)/maxl+1
    svf=(19*sv)/maxl+1
    sif=(19*si)/maxl+1
    suf=(19*su)/maxl+1
    sbf=(19*sb)/maxl+1
    
    if(userID[i] != lastID):
        canvas.delete("all")
        canvas.create_image(0,0,image= image, anchor = NW)
        l = Label(canvas, text = '\t Age : ' + age[i], font = ("Helvetica",16))
        l.place(x =0,y =0)
        l = Label(canvas, text = "돌핀 키즈존 : " + str(remain[1]))
        l.place(x = 0, y = 440)
        l = Label(canvas, text = "파도풀 : " + str(remain[2]))
        l.place(x = 200, y = 440)
        l = Label(canvas, text = "정규풀 : " + str(remain[3]))
        l.place(x = 400, y = 440)
        l = Label(canvas, text = "바데풀 : " + str(remain[4]))
        l.place(x = 600, y = 440)
        l = Label(canvas, text = "아일랜드 : " + str(remain[5]))
        l.place(x = 800, y = 440)
        l = Label(canvas, text = "블루스파 : " + str(remain[6]))
        l.place(x = 1000, y = 440)
        l = Label(canvas, text = "유수풀 : " + str(remain[7]))
        l.place(x = 1200, y = 440)
        l = Label(canvas, text = "스플래시 키즈존 : " + str(remain[8]))
        l.place(x = 1400, y = 440)
        
        l = Label(canvas, text = "돌핀 키즈존 -> 파도풀: " + str(remaind[2]))
        l.place(x = 0, y = 460)
        l = Label(canvas, text = "돌핀 키즈존 -> 정규풀: " + str(remaind[3]))
        l.place(x = 200, y = 460)
        l = Label(canvas, text = "돌핀 키즈존 -> 바데풀: " + str(remaind[4]))
        l.place(x = 400, y = 460)
        l = Label(canvas, text = "돌핀 키즈존 -> 아일랜드: " + str(remaind[5]))
        l.place(x = 600, y = 460)
        l = Label(canvas, text = "돌핀 키즈존 -> 블루스파: " + str(remaind[6]))
        l.place(x = 800, y = 460)
        l = Label(canvas, text = "돌핀 키즈존 -> 유수풀: " + str(remaind[7]))
        l.place(x = 1000, y = 460)
        l = Label(canvas, text = "돌핀 키즈존 -> 스플래시 키즈존: " + str(remaind[8]))
        l.place(x = 1200, y = 460)
        
        l = Label(canvas, text = "파도풀 -> 돌핀 키즈존 : " + str(remainp[1]))
        l.place(x = 0, y = 480)
        l = Label(canvas, text = "파도풀 -> 정규풀 : " + str(remainp[3]))
        l.place(x = 200, y = 480)
        l = Label(canvas, text = "파도풀 -> 바데풀 : " + str(remainp[4]))
        l.place(x = 400, y = 480)
        l = Label(canvas, text = "파도풀 -> 아일랜드 : " + str(remainp[5]))
        l.place(x = 600, y = 480)
        l = Label(canvas, text = "파도풀 -> 블루스파 : " + str(remainp[6]))
        l.place(x = 800, y = 480)
        l = Label(canvas, text = "파도풀 -> 유수풀 : " + str(remainp[7]))
        l.place(x = 1000, y = 480)
        l = Label(canvas, text = "파도풀 -> 스플래시 키즈존 : " + str(remainp[8]))
        l.place(x = 1200, y = 480)
        
        l = Label(canvas, text = "정규풀 -> 돌핀키즈존 : " + str(remainj[1]))
        l.place(x = 0, y = 500)
        l = Label(canvas, text = "정규풀 -> 파도풀 : " + str(remainj[2]))
        l.place(x = 200, y = 500)
        l = Label(canvas, text = "정규풀 -> 바데풀 : " + str(remainj[4]))
        l.place(x = 400, y = 500)
        l = Label(canvas, text = "정규풀 -> 아일랜드 : " + str(remainj[5]))
        l.place(x = 600, y = 500)
        l = Label(canvas, text = "정규풀 -> 블루스파 : " + str(remainj[6]))
        l.place(x = 800, y = 500)
        l = Label(canvas, text = "정규풀 -> 유수풀 : " + str(remainj[7]))
        l.place(x = 1000, y = 500)
        l = Label(canvas, text = "정규풀 -> 블루스파 : " + str(remainj[8]))
        l.place(x = 1200, y = 500)
        
        l = Label(canvas, text = "바데풀 -> 돌핀키즈존 : " + str(remainv[1]))
        l.place(x = 0, y = 520)
        l = Label(canvas, text = "바데풀 -> 파도풀 : " + str(remainv[2]))
        l.place(x = 200, y = 520)
        l = Label(canvas, text = "바데풀 -> 정규풀 : " + str(remainv[3]))
        l.place(x = 400, y = 520)
        l = Label(canvas, text = "바데풀 -> 아일랜드 : " + str(remainv[5]))
        l.place(x = 600, y = 520)
        l = Label(canvas, text = "바데풀 -> 블루스파 : " + str(remainv[6]))
        l.place(x = 800, y = 520)
        l = Label(canvas, text = "바데풀 -> 유수풀 : " + str(remainv[7]))
        l.place(x = 1000, y = 520)
        l = Label(canvas, text = "바데풀 -> 스플래시 키즈 : " + str(remainv[8]))
        l.place(x = 1200, y = 520)
        
        l = Label(canvas, text = "아일랜드 -> 돌핀키즈존 : " + str(remaini[1]))
        l.place(x = 0, y = 540)
        l = Label(canvas, text = "아일랜드 -> 파도풀 : " + str(remaini[2]))
        l.place(x = 200, y = 540)
        l = Label(canvas, text = "아일랜드 -> 정규풀 : " + str(remaini[3]))
        l.place(x = 400, y = 540)
        l = Label(canvas, text = "아일랜드 -> 바데풀 : " + str(remaini[4]))
        l.place(x = 600, y = 540)
        l = Label(canvas, text = "아일랜드 -> 블루스파 : " + str(remaini[6]))
        l.place(x = 800, y = 540)
        l = Label(canvas, text = "아일랜드 -> 유수풀 : " + str(remaini[7]))
        l.place(x = 1000, y = 540)
        l = Label(canvas, text = "아일랜드 -> 스플래시 키즈존 : " + str(remaini[8]))
        l.place(x = 1200, y = 540)
        
        l = Label(canvas, text = "블루스파 -> 돌핀키즈존 : " + str(remainb[1]))
        l.place(x = 0, y = 560)
        l = Label(canvas, text = "블루스파 -> 파도풀 : " + str(remainb[2]))
        l.place(x = 200, y = 560)
        l = Label(canvas, text = "블루스파 -> 정규풀 : " + str(remainb[3]))
        l.place(x = 400, y = 560)
        l = Label(canvas, text = "블루스파 -> 바데풀 : " + str(remainb[4]))
        l.place(x = 600, y = 560)
        l = Label(canvas, text = "블루스파 -> 아일랜드 : " + str(remainb[5]))
        l.place(x = 800, y = 560)
        l = Label(canvas, text = "블루스파 -> 유수풀 : " + str(remainb[7]))
        l.place(x = 1000, y = 560)
        l = Label(canvas, text = "블루스파 -> 스플래시 키즈존 : " + str(remainb[8]))
        l.place(x = 1200, y = 560)

        l = Label(canvas, text = "유수풀 -> 돌핀키즈존 : " + str(remainu[1]))
        l.place(x = 0, y = 580)
        l = Label(canvas, text = "유수풀 -> 파도풀 : " + str(remainu[2]))
        l.place(x = 200, y = 580)
        l = Label(canvas, text = "유수풀 -> 정규풀 : " + str(remainu[3]))
        l.place(x = 400, y = 580)
        l = Label(canvas, text = "유수풀 -> 바데풀 : " + str(remainu[4]))
        l.place(x = 600, y = 580)
        l = Label(canvas, text = "유수풀 -> 아일랜드 : " + str(remainu[5]))
        l.place(x = 800, y = 580)
        l = Label(canvas, text = "유수풀 -> 블루스파 : " + str(remainu[6]))
        l.place(x = 1000, y = 580)
        l = Label(canvas, text = "유수풀 -> 스플래시 키즈존 : " + str(remainu[8]))
        l.place(x = 1200, y = 580)

        l = Label(canvas, text = "스플래시 키즈존 -> 돌핀키즈존 : " + str(remains[1]))
        l.place(x = 0, y = 600)
        l = Label(canvas, text = "스플래시 키즈존 -> 파도풀 : " + str(remains[2]))
        l.place(x = 200, y = 600)
        l = Label(canvas, text = "스플래시 키즈존 -> 정규풀 : " + str(remains[3]))
        l.place(x = 400, y = 600)
        l = Label(canvas, text = "스플래시 키즈존 -> 바데풀 : " + str(remains[4]))
        l.place(x = 600, y = 600)
        l = Label(canvas, text = "스플래시 키즈존 -> 아일랜드 : " + str(remains[5]))
        l.place(x = 800, y = 600)
        l = Label(canvas, text = "스플래시 키즈존 -> 블루스파 : " + str(remains[6]))
        l.place(x = 1000, y = 600)
        l = Label(canvas, text = "스플래시 키즈존 -> 유수풀 : " + str(remains[7]))
        l.place(x = 1200, y = 600)
        
        canvas.create_oval(535-ppd, 345-ppd, 555+ppd, 365+ppd, fill = "salmon")
        canvas.create_line(530,355,490,205, width=dpf, fill = "red")
        canvas.create_line(250,160,535,345, width=djf, fill = "red")
        canvas.create_line(550,360,1115,185, width=dvf, fill = "blue")
        canvas.create_line(1265,165,550,360, width=dif, fill = "blue")
        canvas.create_line(1385,275,550,360, width=dbf, fill = "blue")
        canvas.create_line(530,355,145,230, width=duf, fill = "red")
        canvas.create_line(235,340,530,355, width=dsf, fill = "red")
        
        canvas.create_oval(495-ppp, 195-ppp, 515+ppp, 215+ppp, fill = "royalblue")
        canvas.create_line(560,355,520,205, width=pdf, fill = "blue")
        canvas.create_line(255,165,500,200, width=pjf, fill = "red")
        canvas.create_line(510,210,1115,185, width=pvf, fill = "blue")
        canvas.create_line(510,210,1265,165, width=pif, fill = "blue")
        canvas.create_line(510,210,1385,275, width=pbf, fill = "blue")
        canvas.create_line(500,200,145,230, width=puf, fill = "red")
        canvas.create_line(235,340,500,200, width=psf, fill = "red")
        
        canvas.create_oval(250-ppj, 160-ppj, 270+ppj, 180+ppj, fill = "greenyellow")
        canvas.create_line(270,180,555,365, width=jdf, fill = "blue")
        canvas.create_line(265,175,510,210, width=jpf, fill = "blue")
        canvas.create_line(265,175,1115,185, width=jvf, fill = "blue")
        canvas.create_line(265,175,1265,165, width=jif, fill = "blue")
        canvas.create_line(265,175,1385,275, width=jbf, fill = "blue")
        canvas.create_line(255,165,145,230, width=juf, fill = "red")
        canvas.create_line(235,340,255,165, width=jsf, fill = "red")
        
        canvas.create_oval(1100-ppv, 170-ppv, 1120+ppv, 190+ppv, fill = "orange")
        canvas.create_line(1105,175,540,350, width=vdf, fill = "red")
        canvas.create_line(1105,175,500,200, width=vpf, fill = "red")
        canvas.create_line(1105,175,255,165, width=vjf, fill = "red")
        canvas.create_line(1265,165,1115,185, width=vif, fill = "blue")
        canvas.create_line(1385,275,1115,185, width=vbf, fill = "blue")
        canvas.create_line(1105,175,145,230, width=duf, fill = "red")
        canvas.create_line(235,340,1105,175, width=dsf, fill = "red")
        
        canvas.create_oval(1250-ppi, 150-ppi, 1270+ppi, 170+ppi, fill = "ivory")
        canvas.create_line(1255,155,540,350, width=iidf, fill = "red")
        canvas.create_line(1255,155,500,200, width=ipf, fill = "red")
        canvas.create_line(1255,155,255,165, width=ijf, fill = "red")
        canvas.create_line(1255,155,1105,175, width=ivf, fill = "red")
        canvas.create_line(1385,270,1265,160, width=ibf, fill = "blue")
        canvas.create_line(1255,155,145,230, width=duf, fill = "red")
        canvas.create_line(235,340,1255,155, width=dsf, fill = "red")
        
        canvas.create_oval(1370-ppb, 260-ppb, 1390+ppb, 280+ppb, fill = "blue")
        canvas.create_line(1375,265,540,350, width=bdf, fill = "red")
        canvas.create_line(1375,265,500,200, width=bpf, fill = "red")
        canvas.create_line(1375,265,255,165, width=bjf, fill = "red")
        canvas.create_line(1375,265,1105,175, width=bvf, fill = "red")
        canvas.create_line(1375,270,1255,160, width=bif, fill = "red")
        canvas.create_line(1375,265,145,230, width=duf, fill = "red")
        canvas.create_line(235,340,1375,265, width=dsf, fill = "red")

        canvas.create_oval(140-ppu, 225-ppu, 160+ppu, 245+ppu, fill = "green")
        canvas.create_line(155, 240,550,360, width=udf, fill = "blue")
        canvas.create_line(155, 240,510,210, width=upf, fill = "blue")
        canvas.create_line(155, 240,265,175, width=ujf, fill = "blue")
        canvas.create_line(155, 240,1115,185, width=uvf, fill = "blue")
        canvas.create_line(155, 240,1265,165, width=uif, fill = "blue")
        canvas.create_line(155, 240,1385,275, width=ubf, fill = "blue")
        canvas.create_line(155, 235,245,345, width=usf, fill = "blue")

        canvas.create_oval(230-pps, 335-pps, 250+pps, 355+pps, fill = "black")
        canvas.create_line(245, 350,550,360, width=sdf, fill = "blue")
        canvas.create_line(245, 350,510,210, width=spf, fill = "blue")
        canvas.create_line(245, 350,265,175, width=sjf, fill = "blue")
        canvas.create_line(245, 350,1115,185, width=svf, fill = "blue")
        canvas.create_line(245, 350,1265,165, width=sif, fill = "blue")
        canvas.create_line(245, 350,1385,275, width=suf, fill = "blue")
        canvas.create_line(145,235,235, 345, width=suf, fill = "red")
        
        num2 = num2 +1
        canvas.update()
    lastID = userID[i]
mainloop()

#존 두개 추가 + 라인 맥시멈 추가
print(num)
