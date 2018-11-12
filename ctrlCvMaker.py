import maya.cmds as mc

def cvFlatSquare(*arg):
    mc.curve(d=1,p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)],k=[0,1,2,3,4],n="ctrl1")

def cvFlatCircle(*arg):
    mc.circle(c=(0,0,0),nr=(0,1,0),sw=360,r=1,d=3,ut=True,tol=0.01,s=8,ch=False,n="ctrl1")

def main():
    if mc.window("ctrlCvMaker", exists=True):
        mc.deleteUI("ctrlCvMaker")

    win = mc.window("ctrlCvMaker",title='ctrlCvMaker',width=200)
    mc.columnLayout(adj=True)
    mc.button(label="Square", command = cvFlatSquare)
    mc.button(label="Circle", command = cvFlatCircle)
    mc.showWindow(win)
