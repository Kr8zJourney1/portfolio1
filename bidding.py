# This is a lesson i was working through.
bidding = True
bidders = {}
highest_bid = 0
winning_bidder = ""

while bidding:
    name = input("What is your name? ").lower()
    print("\n" * 100)
    amount = int(input("What is your bid? $"))
    print("\n" * 100)
    bidders[name] = amount

    others = input("Are there other bidders? Type 'yes' or 'no': ").lower()
    print("\n" * 100)
    if others == "no":
        bidding = False
    elif others != "yes":
        print("Invalid entry. Ending bidding.")
        bidding = False

##### I had so trouble with this part of the code but was able to work it out.###

for bidder_name, bid_amount in bidders.items():
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winning_bidder = bidder_name
###########################################

print(f"The winning bidder is {winning_bidder.title()} with a bid of ${highest_bid}.")

# Big Thanks You!!! to Dr. Angela Yu, Developer and Lead Instructor. My instructor at Udemy. Because of her help I can code.
