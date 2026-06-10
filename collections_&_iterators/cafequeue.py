class CafeQueue:
    def __init__(self):
        self._queue = []
        self._orders = {}
        self._togo = {}

    def add_customer(self, customer, *orders, to_go=True):
        self._queue.append(customer)
        self._orders[customer] = tuple(orders)
        self._togo[customer] = to_go

    def __len__(self):
        return len(self._queue)

    def __contains__(self, customer):
        return (customer in self._queue)

    def __iter__(self):
        return CafeQueueIterator(self)


class CafeQueueIterator:
    def __init__(self, cafe_queue):
        self._cafe = cafe_queue
        self._position = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            customer = self._cafe._queue[self._position]
        except IndexError:
            raise StopIteration
        orders = self._cafe._orders[customer]
        togo = self._cafe._togo[customer]
        self._position += 1

        return (customer, orders, togo)
