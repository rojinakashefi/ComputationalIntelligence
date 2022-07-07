import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
(bests, avg, worsts) = ([], [], [])

with open('learning_curve.txt', 'r') as file:
  lines = file.readlines()

for line in lines:
  best, worst, mean = line.split()
  bests.append(float(best))
  worsts.append(float(worst))
  avg.append(float(mean))

plt.plot(bests, label='best')
plt.plot(avg, label='average')
plt.plot(worsts, label='worst')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend()
plt.show()
