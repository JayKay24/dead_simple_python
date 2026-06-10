from cafequeue import CafeQueue


def brew(order):
    print(f"Making {order}")
    return order


queue = CafeQueue()
queue.add_customer('Newman', 'tea', 'tea', 'tea', 'tea', to_go=False)
queue.add_customer('James', 'medium roast drip, milk, 2 sugar substitutes')
queue.add_customer('Glen', 'americano, no sugar, heavy cream')
queue.add_customer('Jason', 'pumpkin spice latte', to_go=False)

print(len(queue))
print('Glen' in queue)
print('Kyle' in queue)

for customer, orders, to_go in queue:
    for order in orders:
        brew(order)
    if to_go:
        print(f"Order for {customer}!")
    else:
        print(f"Takes order to {customer}")
