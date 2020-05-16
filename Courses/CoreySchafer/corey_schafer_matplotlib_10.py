import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=[5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
y=[7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]
sizes=np.arange(1, len(x))*50
print(sizes)

plt.scatter(x,y, s=sizes, c=y, cmap='Blues',edgecolors='black')

cbar=plt.colorbar()
#plt.xscale('log')
#plt.yscale('log')
cbar.set_label('Satisfaction')
plt.savefig('scatter1.png')
plt.show()
