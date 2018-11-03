import csv, random, math

#unused if counter function isn't used
from collections import Counter

	
millnames = ['',' Thousand',' Million',' Billion',' Trillion']	
winningPercent = 0
winCount = 0
gambleCount = 0
winnings = 0.00
log_every_n = 1_000_000

#uses randrange to generate a 5 index list with numbers ranging from 1 to 69
def generate_mm_numbers():
	#create a list
	generated_nums = list()
	# iterate 5 times
	for x in range(0, 5):
		#add a random number between 1 and 70
		generated_nums.append(random.randrange(1, 71))
	return generated_nums

def generate_mm_special_num():
	return random.randrange(1, 26)
	
#reads all winning numbers from a CSV file and adds them to a list	
def read_mm_numbers():
	with open("mm_numbers.csv", "r") as fin:
		csvreader = csv.reader(fin)
		winner_list = list()
		for x in csvreader:
			for num in x:
				winner_list.append(int(num))
		#uncomment the following two lines to find the 5 most common numbers in the winners list
		#most_common = Counter(winner_list).most_common(5)
		#print(most_common)
	
		#reduces the list to a set (including unique values only) then converts back to a list
		winner_list = list(set(winner_list))
	return winner_list

def print_gamble_stats(winCount, gambleCount, winnings):
	winningPercent = (( winCount / gambleCount ) * 100.00 )
	print("Number of wins: "+str(winCount))
	print("Winnings: "+str(millify(winnings)))
	print("Number of tries: "+str(millify(gambleCount)))
	print("Winning percent: "+str(winningPercent))
	print("\n\n")

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])	
	
winner_set = read_mm_numbers()

#using 10 million iterations, check our chosen numbers against the randomly chosen winning numbers
for gamble in range(0, 100_000_000):
	random_set = generate_mm_numbers()
	random_special_num = generate_mm_special_num()
	#chosen_nums = [int(x) for x in input("Enter five numbers between 1 and 69 separate each number by a space, then press enter:").split()]
	#chosen_special_num = input("Enter a number between 1 and 25, then press enter:")
	#chosen_nums = [int(random.randrange(1, 69)) for x in range(0, 4)]
	chosen_nums = [2, 20, 11, 31, 17] #chosen because they appear on winning tickets more often
	chosen_special_num = 6
	matchingNum = 0
	matchingspecial = False
	winnings -= 5.00
	for choice in chosen_nums:
		if choice in random_set:
			matchingNum += 1
	if chosen_special_num == random_special_num:
			matchingspecial = True
	if matchingNum > 3:# winnings of $500 or more count as a win!
		if matchingNum == 4 and not matchingspecial:
			winnings += 500.00
		elif matchingNum == 4 and matchingspecial:
			winnings += 10_000.00
			#print("you won 10,000 dollars!")
			#print("\n\n")
		elif matchingNum == 5 and not matchingspecial:
			winnings += 1_000_000.00
			print("you won 1,000,000 dollars!")
			print("\n\n")
		elif matchingNum and matchingspecial:
			winnings += 1_600_000_000.00
			print("you won the jackpot!!!!")
			print("\n\n")
		winCount += 1
	gambleCount += 1
	if (gambleCount % log_every_n) == 0:
		print_gamble_stats(winCount, gambleCount, winnings)
		
print_gamble_stats(winCount, gambleCount, winnings)
