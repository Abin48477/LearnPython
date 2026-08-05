import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y= [3,4,5,6,7,]
# z = [7,15,4,21,13]
# #Plot with different markers
# plt.plot(x,y,marker="o",linestyle="-",color="b",label="Circular Marker")
# plt.plot(x, [i-1 for i in y],marker="^",linestyle="--",color='r',label="Triangle Marker")
# plt.plot(x,z,color=(0.1,0.2,0.5),marker="^",linestyle="solid",label="RGB Line")

# #Add title anf labels
# plt.title("Plot with Different Markers")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")


# #show legend
# plt.legend()
# plt.grid(True,axis="x",linestyle="--",linewidth=0.5,color ="gray")
# plt.grid(True,axis= "y",linestyle="-",linewidth=0.7 ,color="red")
# #Display the plot
# plt.show()

#create a figure 
plt.figure(figsize=(10,5))
#first Subplot
plt.subplot(1,2,1)
plt.plot(x,y,marker='o' ,linestyle='-' ,color='blue')
plt.title("Subplot 1")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

#seconf subplot
plt.subplot(1,2,2)
plt.plot(x,y,marker='^' ,linestyle='--' ,color='red')
plt.title("Subplot 2")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.tight_layout()
plt.show()
