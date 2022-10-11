# Dynamic Algorithms

weights = [5, 3, 1, 6, 8, 4, 11, 12]
prices = [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500]

def dynamic(n,capc,weights,prices):
    # base case number 1
    if n == 0 or capc == 0:
        return 0

    # base case 2 to avoid filling up the bag more than needed
    if (weights[n-1]>capc): # if the last add will fill the bag...
        return dynamic(n-1,capc,weights,prices) #repeate
    else:
        # Here we check for the maximum out of all the possibilities when returning them
        return max(prices[n-1] + dynamic(n-1,capc-weights[n-1],weights,prices),
                   dynamic(n-1,capc,weights,prices))
    
n = 8 # number of items
capc = 20 # weight limit
 
print(f"The maximum profits is : {dynamic(n,capc,weights,prices)}", end = "\n\n")

#################################################################
####################################################
# Greedy Algorithms 

profit_ratio = [] # The ration between the price and the weight so that we can define which is more profitable
compination = [] # tuble of all the info

# make the tuble
for i in  range(len(weights)):
    profit_ratio.append(prices[i]/weights[i]) 
for i in range(len(weights)):
    compination.append ((i, profit_ratio[i], weights[i], prices[i]))

compination.sort(key=lambda tup: tup[1], reverse=True) 

# The Alg
bag = {}
profits = int(0)
total_weight = int(0)
indexes = []
def greedy(capacity):
    global profits, bag, total_weight, indexes
    for i in range(len(compination)):
        index, prof, weight, price = compination[i]
        
        if capacity - weight >= 0:
            capacity = capacity - weight
            bag[f"bellte with weight {weight}"] = 1
            profits = profits + price 
            total_weight = total_weight + weight
            indexes.append(index)
        else:
            continue

greedy (20)
# print (compination, end="\n\n")
print (bag, profits, total_weight, end = "\n\n")