'''Please write a program that simulates and outputs the result of 100 rolls of a fair 20-sided die. 
What is your estimate for the average of those roles (including the standard deviation of that estimated average)? 
What is your estimate for the expected value of a single roll of a 20-sided die (including the standard deviation 
of that expected value)? Briefly explain why the two estimates are or are not the same. *'''

import random

def diceroll_simulation(num_sides, num_rolls):
    rolls = []
    dice_values = list(range(1, num_sides+1))

    for _ in range(num_rolls):
        rolls.append(random.choice(dice_values))

    avg = sum(rolls)/num_rolls
    stdev = ( sum([(roll - avg)**2 for roll in rolls]) / num_rolls ) ** 0.5

    expected_avg = sum(dice_values) / num_sides
    expected_stdev = ( sum([(roll - expected_avg)**2 for roll in dice_values]) / num_sides ) ** 0.5

    print(f'Expected avg (infinite trials): {expected_avg}')
    print(f'Expected standard deviation (infinite trials): {round(expected_stdev, 2)}')
    print(f'Results from {num_rolls} trials of rolling a {num_sides}-sided die:')
    print(f'Average value: {round(avg, 2)}')
    print(f'Standard deviation: {round(stdev, 2)}\n')

    return 

if __name__=='__main__':
    diceroll_simulation(20, 1)
    diceroll_simulation(20, 100)