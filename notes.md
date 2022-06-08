========================
 statistical simulation
========================

random variable, is a qty that can take on many values based on chance

two types:
- continuous: infinite possible values
- discrete: finite set of possible values like a dice

probability distribution

is a mapping for the set of possible outcomes of a random variable to the
probability of observing that value.

np.random.choice() given a 1-D array get a random sample

Poisson dist is used for modeling the average rate at which events
occur

-----------
simulations
-----------

framework that models real world systems.

- characterized by repeated random sampling
- gives us an approximate solution

simulation steps:
1. define the set of outcomes associated with a random variable 
2. assign probability to each of this outcomes
3. define the relationship between multiple random variables
4. draw samples from the probability dist
5. analyze samples outcomes
