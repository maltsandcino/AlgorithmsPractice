from collections import deque
import time
import threading

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]
    
##Place Order Driver

def add_item(orders):
    for item in orders:
        time.sleep(0.5)
        print(f"Placing order for {item}")
        order_queue.enqueue(item)

##Serve Order Driver
def serve_queue(order_queue):
    time.sleep(1)
    while not order_queue.is_empty():
        time.sleep(1.0)
        current_item = order_queue.dequeue()
        print(f"The {current_item} is being served")
### Actual instructions to demonstrate the queue's operations, Multithreading in order to have the program take orders simultaneously with serving orders at different rates:
        
orders = ['pizza','samosa','pasta','biryani','burger', 'Iced cream', 'soup', 'crepes', 'cinnamon bobka', 'marble rye']
order_queue = Queue()

t1 = threading.Thread(target=add_item, args=(orders,))
t2 = threading.Thread(target=serve_queue, args=(order_queue,))

t1.start()
t2.start()


### Use a Queue to display the numbers 1 - 10 in binary

def produce_binary_numbers(n):
    bq = Queue()
    bq.enqueue("1")

    for i in range(n):
        front = bq.dequeue()
        print("  ", front)
        bq.enqueue(front + "0")
        bq.enqueue(front + "1")

produce_binary_numbers(10)