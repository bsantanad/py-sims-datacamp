'''
dice simulation

simulate throwing dices and seeing if they end up with the same number.
e.g.

throws first dice get's a 5
throws second dice get's a 4
looses

throws first dice get's a 5
throws second dice get's a 5
wins

the simulation counts the number of times that happen in `sims` times.

meaning you can modify the sims variable to make more runs of the simulation
'''
import numpy as np

dice = [1, 2, 3, 4, 5, 6]
probabilities = [1/6] * 6
num_dice = 2
sims = 100 
wins = 0 

for i in range(sims):
    outcome = np.random.choice(
        dice,
        size = num_dice,
        p=probabilities
    )
    if outcome[0] == outcome[-1]:
        wins += 1

print(f'the dices ended up with the same side up {wins} times out of {sims}')
