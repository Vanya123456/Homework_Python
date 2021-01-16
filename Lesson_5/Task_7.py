import json

firm_profit = {}
firm_losses = {}
average_profit = []
with open('Task_7_Test.txt', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    name, form, revenue, costs = line.split()
    profit = int(revenue) - int(costs)
    if profit > 0:
        firm_profit[name] = profit
    else:
        firm_losses[name] = profit
    if profit > 0:
        average_profit.append(profit)
average_profit = sum(average_profit) / len(average_profit)
out_info = [firm_profit, firm_losses, {'average_profit': average_profit}]

with open('Task_7_.json', 'w') as f_json:
    json.dump(out_info, f_json)

with open('Task_7_.json') as f_json:
    print(json.load(f_json))
