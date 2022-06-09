import numpy as np

# setup
lottery_ticket_cost = 10
num_tickets = 1000
grand_prize = 10000

chance_of_winning = 1 / num_tickets

# there are two outcomes, either we lose the lottery ticket cost, or we
# gain the grand prize minus the lottery ticket
gains = [
    -lottery_ticket_cost, grand_prize - lottery_ticket_cost
]

# there are also to probabilities, the one of loosing is:
# 1 minus the chance of winning, the other is
# the chance of winning 
probability = [1 - chance_of_winning, chance_of_winning]

outcome = np.random.choice(
    a = gains,
    size = 1,
    p = probability,
    replace = True,
)

# as you can imagine this is almost always a lose, not a gain
print(outcome)
