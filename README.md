# 100 prisoners problem algorithm
The 100 prisoners problem is a mathematical problem in probability theory and combinatorics.

## Problem
The director of a prison offers 100 death row prisoners, who are numbered from 1 to 100, a last chance. A room contains a cupboard with 100 drawers. The director randomly puts one prisoner's number in each closed drawer. The prisoners enter the room, one after another. Each prisoner may open and look into 50 drawers in any order. The drawers are closed again afterwards. If, during this search, every prisoner finds his number in one of the drawers, all prisoners are pardoned. If just one prisoner does not find his number, all prisoners die. Before the first prisoner enters the room, the prisoners may discuss strategy — but may not communicate once the first prisoner enters to look in the drawers. What is the prisoners' best strategy?
If every prisoner selects 50 drawers at random, the probability that a single prisoner finds his number is 50%. Therefore, the probability that all prisoners find their numbers is the product of the single probabilities, which is 0.0000000000000000000000000000008, a vanishingly small number. The situation appears hopeless.

## Solution
Surprisingly, there is a strategy that provides a survival probability of more than 30%. The key to success is that the prisoners do not have to decide beforehand which drawers to open. Each prisoner can use the information gained from the contents of every drawer he already opened to help decide which one to open next. Another important observation is that this way the success of one prisoner is not independent of the success of the other prisoners, because they all depend on the way the numbers are distributed.

To describe the strategy, not only the prisoners, but also the drawers are numbered from 1 to 100, for example row by row starting with the top left drawer. The strategy is now as follows:

  1.Each prisoner first opens the drawer with his own number.
  
  2.If this drawer contains his number he is done and was successful.
  
  3.Otherwise, the drawer contains the number of another prisoner and he next opens the drawer with this number.
  
  4.The prisoner repeats steps 2 and 3 until he finds his own number or has opened 50 drawers.
  
  
By starting with his own number, the prisoner guarantees he is on a sequence of boxes containing his number. The only question is whether this sequence is longer than 50 boxes. The prisoners survive with the cycle-following strategy in more than 30% of cases independently of the number of prisoners.

(Text adapted from https://en.wikipedia.org/wiki/100_prisoners_problem#:~:text=The%20100%20prisoners%20problem%20is,cannot%20communicate%20with%20other%20prisoners.)

# Motivation

This implementation was motivated by Veritasium video (https://youtu.be/iSNsgj1OCLA).

# Run the simulation

Run main.py and alter the parameters as you wish. I made a simulation with 400 prisoners, 400 boxes and 10000 iterations and the result was still above 30% of success rate (30.570000000000004% to be precise).