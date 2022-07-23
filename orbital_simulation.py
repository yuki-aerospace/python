from numpy import *
from matplotlib.pyplot import *
from matplotlib.animation import *
from vpython import * 

# figure out what the maximum height you can launch a tennis ball with an air cannon

# intial values
g = 9.8
x0 = y0 = 0


#user put the value of initial velocity, launch angle (,and wheter consider air resistance.)
v0 = float(input('what is the intial velocity?'))
theta = float(input('what is the launch angle?'))*pi/180

v0_x = v0 * cos(theta)
v0_y = v0 * sin(theta)

def horizontal_dist(t):
    return v0_x * t

def vertical_dist(t):
    return v0_y * t - 0.5 * g * t**2
'''
tt = v0_y/g

print("maximum height is:", vertical_dist(tt), "m")
print("horizontal distance is:", horizontal_dist(tt), "m")
'''

# Caluculate xmax, ymax, tmax
tmax = 2 * v0_y/g
xmax = horizontal_dist(tmax)
ymax = vertical_dist(tmax/2)

# create animation↓
fig = figure()
anim = [] # put data for the animation here
time = arange(0, tmax+1, 0.5) # time scale from 0s to tmax+1 s, every 0.5s
x_all = [] # put data of x here
y_all = []# put data of y here

for t in time:
    x = [horizontal_dist(t)]
    y = [vertical_dist(t)]

    x_all.append(x[0])
    y_all.append(y[0])

    im = plot(x,y,'o', x_all,y_all, '--', color='red',markersize=10, linewidth = 2, aa=True)
    anim.append(im)

anim = ArtistAnimation(fig, anim) # create aniamtion

xlabel('Horizontal Distance (m)', fontsize = 18) 
ylabel('Height (m)', fontsize = 18)
xlim(0, xmax+100)
ylim(-10,ymax+100)
hlines([0], 0, 2000, linestyles="-")  # draw a line of y=0

show() 

anim.save("t.gif", writer='imagemagick')

