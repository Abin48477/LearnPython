import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# heart coordinates
t = np.linspace(0, 2 * np.pi, 1000)
x=16 * np.sin(t) ** 3
y=13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# setup figure
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal')
ax.axis('off')

# empty plot element
line, = ax.plot([], [], color='red', linewidth=3)
fill= None
text = ax.text(0, 0, "",color='red',fontsize=22,fontweight='bold',ha='center',va='center')

# update function for animation

def update(frame):
    global fill

    if frame<len(x):
        line.set_data(x[:frame],y[:frame])

    if frame==len(x):
        fill=ax.fill(x,y,color='pink',alpha=0.6)

    if frame>len(x):
        alpha=min((frame-len(x))/30,1)
        text.set_text("I Love You")
        text.set_alpha(alpha)
    return line,text
total_frames=len(x)+40
ani= FuncAnimation(fig,update,frames=total_frames,interval=10,blit=False)
plt.show()