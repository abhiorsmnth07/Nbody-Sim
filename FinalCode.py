from vpython import * 

G = 1
M = 1
R = 1 + 10*random()
rsoft = 0.03
w = vector(0,0.05,0)
n = 0
N = 50
stars = []

while n<N:
  Radi = sqrt(random()) * 0.5  
  if Radi < 0.2:
    color = vector(0.2, 0.5, 1)    # Blue
  elif Radi < 0.25:
    color = vector(0.2, 0.2, 0.2)  # Gray  
  elif Radi < 0.39:
    color = vector(1, 1, 0)        # Yellow
  else:
    color = vector(1, 0.3, 0)
  rt = R*vector(2*random()-1,2*random()-1,2*random()-1)
  stars = stars + [sphere(pos=rt,radius=Radi,make_trail=False,retain=100, color = color)]
  n = n + 1

for star in stars:
  star.m = star.radius**3
  star.p = star.m*cross(w,vector(star.pos.x,0,star.pos.z))
  star.F = vector(0,0,0)

t = 0
dt = 0.02

while t<100:
  rate(300)
  for star in stars:
    star.F = vector(0,0,0)
  for i in range(len(stars)):
    for j in range(len(stars)):
      if i!=j:
        rji = stars[i].pos - stars[j].pos
        stars[i].F = stars[i].F - G*stars[i].m*stars[j].m*norm(rji)/(mag(rji)**2+rsoft**2)
        
  for star in stars:
    star.p = star.p + star.F*dt
    star.pos = star.pos + star.p*dt/star.m
  t = t + dt
        
        
        
