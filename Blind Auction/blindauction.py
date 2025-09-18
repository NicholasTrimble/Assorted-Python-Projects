from art import logo

print(logo)

continue_bidding = True
auction_dict = {}

while continue_bidding == True:
    continue_bidding = input("Would you like to bid? (y/n)")
    continue_bidding = continue_bidding[0].lower()
    if continue_bidding == "y":
        continue_bidding = True
        user_name = input("What is your name? ")
        user_bid = float(input("What is your bid? "))
        auction_dict[user_name] = user_bid

        print(auction_dict)
        print("\n" * 20)
    else:
        continue_bidding = False
        high_bidder = max(auction_dict, key=auction_dict.get)
        max_amount = auction_dict[high_bidder]
        print(f"{high_bidder} had the highest bid at ${max_amount}.")
        print(f"{high_bidder} wins the auction.")