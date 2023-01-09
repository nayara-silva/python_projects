import os
import art

bid_list = {}
end_auction = False

def check_winner(bids):
    highest_bid = 0
    winner = ""
    
    for bidder in bids:
        bid_value = bids[bidder]
        if bid_value > highest_bid:
            highest_bid = bid_value
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
    
def screen_clear():
    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")
    
    
while end_auction == False:
    print(art.logo)
    
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    
    bid_list[name] = bid
    
    more_bidders = input("Are there any other bidders? Tipe 'yes' or no'. ").lower()
    screen_clear()
    
    if more_bidders == 'no':
        check_winner(bid_list)
        end_auction = True
        
    
    
        

        

