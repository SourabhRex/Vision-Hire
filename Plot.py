import matplotlib.pyplot as plt
import matplotlib.animation as animation
# Get the Figure
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_facecolor((0,0,0)) # Set the background to black
# 
def animate(i):
	ax.clear()
	xs = []
	ys = []
	zs = []
	graph_data = open('result.csv','r').read() # Open file.csv generated by Face.py
	lines = graph_data.split('\n')
	for line in lines[1:]:
		if len(line) > 1: # Skip the first labels line in csv file
			x, y,z= line.split(',')
			xs.append(float(x))
			ys.append(float(y))
			zs.append(float(z))
            
			print(xs,ys,zs)
	# Lets add these lists xs, ys , zs to the plot		
	ax.clear()
	ax.plot(xs, ys,'-o', color = (0,1,0.25))
	ax.plot(xs, zs,'--', color = (1,1,0.25))
    
	ax.set_xlabel("Frame_count")
	ax.set_ylabel("EAR AND MAR value")
	ax.set_title("Live Plot for EAR & MAR")
	fig.tight_layout() # To remove outside borders
	ax.yaxis.grid(True)
	ax.legend()
    
# Lets call the animation function 	
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()