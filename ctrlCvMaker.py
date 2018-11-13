import maya.cmds as mc

def cvFlatSquare(*args):
    mc.curve(d=1,p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)],k=[0,1,2,3,4],n="ctrl1")

def cvFlatCircle(*args):
    mc.circle(c=(0,0,0),nr=(0,1,0),sw=360,r=1,d=3,ut=True,tol=0.01,s=8,ch=False,n="ctrl1")

def cvFlatTriangle(*args):
    pass

def cvObjCube(*args):
    mc.curve(d=1,p=[(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,-0.5,0.5),(0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],n="ctrl1")

def cvObjSphere(*args):
    pass

def ctrlLocator(*args):
    pass

def main():
    if mc.window("ctrlCvMaker", exists=True):
        mc.deleteUI("ctrlCvMaker")

    win = mc.window("ctrlCvMaker",title='ctrlCvMaker',width=200)
    mc.columnLayout(adj=True)
    mc.button(label="Square", command = cvFlatSquare)
    mc.button(label="Circle", command = cvFlatCircle)
    mc.button(label="Triangle", command = cvFlatTriangle)
    mc.button(label="Cube", command = cvObjCube)
    mc.button(label="Sphere", command = cvObjSphere)
    mc.button(label="Locator", command = ctrlLocator)
    mc.showWindow(win)
