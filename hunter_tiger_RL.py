#Creating custom environment for RL agent
import numpy as np
from PIL import Image
import cv2
import pickle
import time
SIZE = 10

class Grid:
    def __init__(self, size=SIZE):
        self.x = np.random.randint(0,size)
        self.y = np.random.randint(0,size)
        
    def subtract(self, other):
        return (self.x - other.x, self.y - other.y)
    
    def isequal(self, other):
        if(self.x - other.x == 0 and self.y - other.y == 0):
            return True
        else:
            return False
    
    def action(self, choice):
        '''
        Gives us total of 8 movement options (0,1,2,3,4,5,6,7).
        '''
        if choice == 0:
            self.move(x=1, y=1)
        elif choice == 1:
            self.move(x=-1, y=-1)
        elif choice == 2:
            self.move(x=-1, y=1)
        elif choice == 3:
            self.move(x=1, y=-1)
        elif choice == 4:
            self.move(x=1, y=0)
        elif choice == 5:
            self.move(x=0, y=1)
        elif choice == 6:
            self.move(x=-1, y=0)
        elif choice == 7:
            self.move(x=0, y=-1)
        
    def move(self, x=False, y=False):
        if not x:
            self.x += np.random.randint(-1,2)
        else:
            self.x += x
        if not y:
            self.y += np.random.randint(-1,2)
        else:
            self.y += y
        
        if self.x < 0:
            self.x = 0
        if self.x >= SIZE:
            self.x = SIZE - 1
        if self.y < 0:
            self.y = 0
        if self.y >= SIZE:
            self.y = SIZE - 1

#Lets train
episodes = 1000
move_penalty = -1
hunter_penalty = - 100
meat_penalty = 50
show_every = 10
learning_rate = 0.2
gamma = 0.9

#for coloring
tiger_key = 1
hunter_key = 2
meat_key = 3

#RGB color coding
dd = {1:(0, 255, 255), 2:(255,0,0), 3:(0,0,255)}

q_table = {}
for a in range(-SIZE+1, SIZE):
    for b in range(-SIZE+1, SIZE):
        for c in range(-SIZE+1, SIZE):
            for d in range(-SIZE+1, SIZE):
                q_table[((a,b),(c,d))]= [np.random.uniform(-8,0) for i in range(8)]
                #for e in range(-SIZE+1, SIZE):
                    #for f in range(-SIZE+1, SIZE):

for eps in range(episodes):
    hunter1 = Grid()
    #hunter2 = Grid()
    meat = Grid()
    tiger = Grid()
    show = False
    if(eps%show_every==0):
        show = True
    
    for i in range(200):
        dstate = (hunter1.subtract(tiger), meat.subtract(tiger))
        action = np.random.randint(0,8)
        tiger.action(action)
        if(tiger.x==hunter1.x and tiger.y==hunter1.y):
            reward = hunter_penalty
        #elif(tiger.x==hunter2.x and tiger.y==hunter2.y):
            #reward = hunter_penalty
        elif(tiger.x==meat.x and tiger.y==meat.y):
            reward = meat_penalty
        else:
            reward = move_penalty
        
        new_dstate = (hunter1.subtract(tiger), meat.subtract(tiger))
        max_future_qval = np.max(q_table[new_dstate])
        current_qval = q_table[dstate][action]
        if reward == meat_penalty:
            new_qval = meat_penalty
        else:
            new_qval = (1 - learning_rate) * current_qval + learning_rate * (reward + gamma * max_future_qval)
        
        q_table[dstate][action] = new_qval
    
    
        if(show):
            env = np.zeros((SIZE, SIZE, 3), dtype=np.uint8) # 3 is the number of channels for RGB image
            env[meat.x][meat.y] = dd[meat_key]
            env[tiger.x][tiger.y] = dd[tiger_key]
            env[hunter1.x][hunter1.y] = dd[hunter_key]
            #env[hunter2.x][hunter2.y] = dd[hunter_key]
            image = Image.fromarray(env, 'RGB')
            image = image.resize((300, 300))
            cv2.imshow("ENV", np.array(image))
            if reward == meat_penalty or reward == hunter_penalty:
                if cv2.waitKey(500) and 0xFF == ord('q'):
                    break
            else:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            if reward == meat_penalty or reward == hunter_penalty:
                break