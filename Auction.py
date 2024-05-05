# It asks for the name of the user
# asks for the bid
# asks for repetition -> yes or no
# if yes repeats process
# if no shows the highest bidder.

should_continue = True
name_list = []
bid_list = []

while should_continue:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))

    name_list.append(name)
    bid_list.append(bid)

    continuity = input("Are there any more bidder? -> Yes or No").lower()

    if continuity == "no":
        should_continue = False

great_index = 0

for i in range(len(bid_list)):
    if great_index < i:
        great_index = i

print(f'The highest bidder is {name_list[great_index]} with an amount of ${bid_list[great_index]}')





