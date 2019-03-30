#riddler express 2/1/2019
#maze without walls


'''Define directions:
Forward Maze
0-Straight
1-Left
2-Right
3-U-Turn
4- ? (Random/Choice)
5-Smiley
6- X (dead)

Backward Maze
0-Straight
1-Right
2-Left
3-U-Turn
4- ? (Random/Choice)
5-Smiley
6- X (dead)
'''
import numpy as np



mazeF=np.array([1,3,3,4,3,1,6,1,
 2,1,2,1,3,5,3,3,
 0,1,2,1,3,1,6,2,
 3,2,4,2,0,1,4,2,
 2,3,3,2,2,2,0,1,
 0,4,0,1,0,0,1,2,
 2,1,2,4,2,1,4,1,
 1,2,0,2,0,1,2,1])
mazeF=np.reshape(8,8)

mazeB=np.array([2, 3, 3, 4, 3, 2, 6, 2,
       1, 2, 1, 2, 3, 5, 3, 3,
       0, 2, 1, 2, 3, 2, 6, 1,
       3, 1, 4, 1, 0, 2, 4, 1,
       1, 3, 3, 1, 1, 1, 0, 2,
       0, 4, 0, 2, 0, 0, 2, 1,
       1, 2, 1, 4, 1, 2, 4, 2,
       2, 1, 0, 1, 0, 2, 1, 2])
mazeB=mazeB.reshape(8,8)

n=[1,0]
s=[-1,0]
e=[0,-1]
w=[0,1]

#define each individual run
class BackRunner():

    def __init__(self):
        BackRunner.rows=[1,2]
        BackRunner.col=[5,5]
        BackRunner.current=mazeB[2,5]
        state()
        moves()



    def state():
        #define which way we're facing
        face=[]
        face.append(Runner.rows[-2] - Runner.rows[-1])
        face.append(Runner.col[-2] - Runner.col[-1])
        
        N=[1,0]
        S=[-1,0]
        E=[0,-1]
        W=[0,1]

        
        if face==N:
            BackRunner.state=='N'+str(BackRunner.current)
        if face==S:
            BackRunner.state=='S'+str(BackRunner.current)
        if face==E:
            BackRunner.state=='E'+str(BackRunner.current)
        if face==W:
            BackRunner.state=='W'+str(BackRunner.current)
    
    def moves():
        if BackRunner.state==N1 or S2 or E0 or W3:
            sideL()
        if BackRunner.state==N2 or S1 or E3 or W0:
            sideR()
        if BackRunner.state==N0 or S3 or E2 or W1:
            down()
        if BackRunner.state==N3 or S0 or E1 or W2:
            up()

    #functions for sideL, sideR, down, and up
        
    #leftN is different than leftS
    def leftN():
    
    
