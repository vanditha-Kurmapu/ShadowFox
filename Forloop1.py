import random

rolls = 20
count_6 = 0
count_1 = 0
two_sixes_in_row = 0
previous_roll = None

for i in range(rolls):
    roll = random.randint(1, 6)
    print("Roll", i+1, ":", roll)

    if roll == 6:
        count_6 += 1

    if roll == 1:
        count_1 += 1

    if roll == 6 and previous_roll == 6:
        two_sixes_in_row += 1

    previous_roll = roll

print("\nStatistics:")
print("Number of times rolled a 6:", count_6)
print("Number of times rolled a 1:", count_1)
print("Number of times two 6s in a row:", two_sixes_in_row)