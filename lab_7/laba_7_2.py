class Node:
    def __init__(self, customer_name, items_count):
        self.customer_name = customer_name
        self.items_count = items_count
        self.next = None

class Queue:
    def __init__(self, cashier_id):
        self.head = None
        self.tail = None
        self.cashier_id = cashier_id
        self.size = 0
    
    def enqueue(self, customer_name, items_count):
        new_node = Node(customer_name, items_count)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Customer '{customer_name}' with {items_count} items added to cashier {self.cashier_id}")
    
    def dequeue(self):
        if self.head is None:
            print(f"Cashier {self.cashier_id}: Queue is empty")
            return None
        
        customer_name = self.head.customer_name
        items_count = self.head.items_count
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
        
        self.size -= 1
        print(f"Cashier {self.cashier_id}: Served customer '{customer_name}' with {items_count} items")
        return customer_name
    
    def display(self):
        if self.head is None:
            print(f"Cashier {self.cashier_id}: Queue is empty")
            return
        
        print(f"Cashier {self.cashier_id} queue:")
        current = self.head
        position = 1
        while current:
            print(f"  {position}. {current.customer_name} ({current.items_count} items)")
            current = current.next
            position += 1
    
    def is_empty(self):
        return self.head is None
    
    def get_size(self):
        return self.size

class SupermarketSystem:
    def __init__(self, num_cashiers):
        self.cashiers = [Queue(i+1) for i in range(num_cashiers)]
    
    def add_customer(self, customer_name, items_count):
        min_queue = min(self.cashiers, key=lambda q: q.get_size())
        min_queue.enqueue(customer_name, items_count)
    
    def serve_customer(self, cashier_id):
        if 1 <= cashier_id <= len(self.cashiers):
            self.cashiers[cashier_id - 1].dequeue()
        else:
            print("Invalid cashier ID")
    
    def display_all_queues(self):
        print("\n=== Current state of all cashiers ===")
        for cashier in self.cashiers:
            cashier.display()
        print()

print("=== SUPERMARKET QUEUE MANAGEMENT SYSTEM ===\n")

system = SupermarketSystem(3)

print("--- Adding customers ---")
system.add_customer("John", 15)
system.add_customer("Mary", 8)
system.add_customer("Bob", 20)
system.add_customer("Alice", 5)
system.add_customer("Tom", 12)
system.add_customer("Sarah", 7)

system.display_all_queues()

print("--- Serving customers ---")
system.serve_customer(1)
system.serve_customer(2)
system.serve_customer(1)

system.display_all_queues()

print("--- Adding more customers ---")
system.add_customer("David", 10)
system.add_customer("Emma", 3)

system.display_all_queues()

print("--- Serving remaining customers ---")
system.serve_customer(3)
system.serve_customer(1)
system.serve_customer(2)

system.display_all_queues()