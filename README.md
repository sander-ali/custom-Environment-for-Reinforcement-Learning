# Custom-Environment-for-Reinforcement-Learning
A simple Q-learning implementation for custom environment. There is one hunter and one tiger. The scenario is simple, Tiger has to fetch the meat and run without getting caught. For further simplicity, the hunter remains still. You can change the parameters accordingly but due to crude coding, qtable consumes a lot of memory and space so I have just trained it for 1000 episodes and show the results at every 10th step. You can vary the Grid size as well.  

I have used 10 but you can use 5.   

Let me know if you have problem running the code.   

You can add more hunters if you want. just move the q_table from line 85 to line 88 and disable the comments on line 86, 87, 91, 104, 105, and 127.  

Also modify the q_table command as: q_table[((a,b),(c,d),(e,f))]= [np.random.uniform(-8,0) for i in range(8)]  

The demo video is uploaded on my YouTube Channel https://www.youtube.com/channel/UCY0_XtpzqA-4UwtRRIn7S5w

![snap1](https://user-images.githubusercontent.com/26203136/158773115-b448a896-78a3-4e95-8af8-8150b69bfc38.jpg)
