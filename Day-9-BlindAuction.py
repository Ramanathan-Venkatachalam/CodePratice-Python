bidders = False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Ramu": 123, "James": 321}
  for key in bidding_record:
    bid_amount = bidding_record[key]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = key
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidders:
  name = str(input("What is your Name: "))
  price = int(input("What is the Bid Amount: Rs."))

  bids = {}
  bids[name] = price
  next_bidder = input("Are there any other bidders? Type 'yes or 'no'. ")
  if next_bidder == "no":
    bidders = True
    find_highest_bidder(bids)
  #elif next_bidder == "yes":
    #clear()