import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

minutes=[1,2,3,4,5,6,7,8,9]

player1=[1,2,3,3,4,4,4,4,5]
player2=[1,1,1,1,2,2,2,3,4]
player3=[1,1,1,2,2,2,3,3,3]
labels=['Player1','Player2','Player3']
colors=['r','g','y']

plt.stackplot(minutes,player1,player2,player3, labels=labels,colors=colors)
plt.title('Points earned in each minute')
plt.savefig('stackplot_1.png')
plt.tight_layout()
plt.legend(loc="upper left")
plt.show()