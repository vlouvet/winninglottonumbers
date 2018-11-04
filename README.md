# Winning Lotto Numbers

Uses various methods to find numbers likely to win the
*Mega Millions Lotto prizes ($500 and up)*.

This project uses only built-in libraries wherever possible.
All data was collected on publicly available sources.

The program has three basic operation modes:
 1. Allow the user to interactively enter their Mega Million numbers.
 2. Randomly select Mega Million numbers.
 3. Use hard-coded list of Mega Million numbers. **(Enabled by default)**

# How to use it

1. Open the `winners.py` file in a text editor and change the value in
   line 10 to the total number of money you want to spend on lotto
   tickets. **(defaults to 2,000,000)**
2. Run the program from the terminal with no arguments
   (`python winners.py`)
3. The program will "gamble" for you by purchasing a ticket for 2.
4. If the guessed numbers match at least 4 of the numbers in the
   MegaMillions drawing, **you win!**
5. If the user wins the jackpot (hard-coded to a value of 1.6 billion)
   the program ends
6. The program also ends if the user's winnings drop down to 0 before
   winning the jackpot.

To "improve" a user's chances, the program keeps a list (`running_list`)
of the most recent winning numbers.
Every 100,000 guesses, the program then finds the 5 most common numbers,
and updates the `chosen_nums` list to be these 5 numbers.
The same process happens with the MegaBall number.

In testing, I have found an average winning rate of .0125 %.
This includes prizes of $500 or more.
