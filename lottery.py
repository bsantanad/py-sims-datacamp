import numpy as np

# setup
lottery_ticket_cost = 10
num_tickets = 1000
grand_prize = 10000

chance_of_winning = 1 / num_tickets

size = 2000 # controls the number of simulations

# there are two outcomes, either we lose the lottery ticket cost, or we
# gain the grand prize minus the lottery ticket
payoffs = [
    -lottery_ticket_cost, grand_prize - lottery_ticket_cost
]

# there are also to probabilities, the one of loosing is:
# 1 minus the chance of winning, the other is
# the chance of winning
probs = [1 - chance_of_winning, chance_of_winning]

outcomes = np.random.choice(
    a = payoffs,
    size = size,
    p = probs,
    replace = True,
)

# Mean of outcomes.
answer = np.mean(outcomes)
print("Average payoff from {} simulations = {}".format(size, answer))
