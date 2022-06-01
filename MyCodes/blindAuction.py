from multiprocessing.sharedctypes import Value
# from turtle import clear
import os
logo = logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# def highest_bidder(bidding_details):
#     amount = 0
#     highest_bidder = {}
#     for key in bidding_details:
#         if bidding_details[key] > amount:
#             amount = int(bidding_details[key])
#     highest_bidder[key] = amount
#     # print(highest_bidder)
#     print(f"The winner is {key} with a bid of ${highest_bidder[key]}")
# def highest_bidder(bidder_name, bid_amount):
#     bidder_details = {}
#     bid_amounts = []
#     bidder_details[bidder_name] = bid_amount
#     for key in bidder_details:
#         bid_amounts.append(bidder_details[key])
#     highest_bid = max(bid_amounts)
#     print(f"The winner is {bidder_details[highest_bid]} with a bid of ${highest_bid}")
def highest_bidder(bidding_details):
    highest_amount = 0
    highest_bidder = ""
    for key in bidding_details:
        if bidding_details[key] > highest_amount:
            highest_amount = bidding_details[key]
            highest_bidder = key
    print(f"The winner is {highest_bidder} with bid of ${highest_amount}\n")
    
    print(f"The bidders are:\n")
    for key in bidding_details:
        print(f"{key} : ${bidding_details[key]}")



print(logo)

bidding_details = {}
bidding_continues = True
while bidding_continues:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    bidding_details[bidder_name] = bid_amount
    # highest_bidder(bidder_name, bid_amount)
    bidder_availability = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if bidder_availability == "no" or bidder_availability != "yes":
        bidding_continues = False
        highest_bidder(bidding_details)
    else:
        os.system('cls')


    
        


