class PriorityQueue:   #priority queue to add orders according to the priority
    def __init__(self):
        self.array = [(None, None, None)]  # Holds orders with (order_name, priority, counter)
        self.counter = 0  # Tracks insertion order
    # get parent,left,right child methods for checking in priority
    def getParent(self, i):
        return i // 2

    def getLeftChild(self, i):
        return 2 * i

    def getRightChild(self, i):
        return 2 * i + 1

    def add_order(self, order_name, priority):   # adding new orders 
        self.counter += 1   # if priority is same then it compares counter (it means who ordered first)
        self.array.append((order_name, priority, self.counter))
        self.heapify_up(len(self.array) - 1)   # calling function to rearrange queue accordingly

    def heapify_up(self, i):  # rearranging queue accordingly after addding a order.
        if i > 1:
            parent = self.getParent(i)
            if (self.array[i][1] < self.array[parent][1] or
                (self.array[i][1] == self.array[parent][1] and self.array[i][2] < self.array[parent][2])):  # comparing counter if priorities are same
                self.array[i], self.array[parent] = self.array[parent], self.array[i]
                self.heapify_up(parent)   # reccursion to rearrange if priority is higher

    def delete_order(self):  #deletion of orders
        if len(self.array) > 2:
            temp = self.array[1]
            self.array[1] = self.array.pop()  # stores last order in first position
            self.heapify_down(1)   # to rearrange after last order coming to first position
            return temp
        elif len(self.array) == 2:
            return self.array.pop(1)
        else:
            return None   # if number of orders is 1 or 0 then it return None because there will be no orders

    def heapify_down(self, i): # rearranging queue after an order is removed from queue
        current = i
        left = self.getLeftChild(i)
        right = self.getRightChild(i)

        if left < len(self.array):
            if (self.array[left][1] < self.array[current][1] or
                (self.array[left][1] == self.array[current][1] and self.array[left][2] < self.array[current][2])):
                current = left

        if right < len(self.array):
            if (self.array[right][1] < self.array[current][1] or
                (self.array[right][1] == self.array[current][1] and self.array[right][2] < self.array[current][2])):
                current = right

        if current != i:
            self.array[i], self.array[current] = self.array[current], self.array[i]
            self.heapify_down(current)

class OrderNode:  # Doubly Linked List Node for Order History
    def __init__(self, order_name, priority): # creating node that stores details of order.
        self.order_name = order_name
        self.priority = priority
        self.delivered = False  # Status of order initially not delivered
        self.next = None
        self.prev = None
#doubly linked list implementation
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_order(self, order_name, priority): #adding order
        new_node = OrderNode(order_name, priority)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def check_order_status(self, order_name): # checking order status of given order whether delivered or not.
        current = self.head
        while current:
            if current.order_name == order_name:
                return f"Order {order_name}: {'Delivered' if current.delivered else 'Pending'}"
            current = current.next
        return "Order not found!"

    def change_order_status(self, order_name): # marking order as delivered.
        current = self.head
        while current:
            if current.order_name == order_name:
                current.delivered = True
                return f"Order {order_name} has been marked as delivered."
            current = current.next
        return "Order not found!"

    def print_orders(self):   ## printing all the orders in the history.
        current = self.head
        if current is None:
            print("No orders in the history.")
            return
        while current:
            print(f"Order: {current.order_name}, Priority: {current.priority}, Status: {'Delivered' if current.delivered else 'Pending'}")
            current = current.next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# Stack Implementation to undo redo orders.
class Stack: # linked list based implementation of stack
    def __init__(self):
        self.top = None

    def push(self,data): # insertion into the stack
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode

    def pop(self): #deletion from the stack from the top
        if self.top is None:
            return "stack is empty"
        else:
            temp = self.top.data
            self.top = self.top.next
            return temp

    def peek(self): # does not delete ut only returns the last added element
        if self.top is None:
            return "stack is empty"
        else:
            return self.top.data

    def is_empty(self): # checking if thr stack is empty
        return self.top is None
#binary search tree node
class MenuNode:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:  # binary search tree implementation for Menu items
    def __init__(self):
        self.root = None

    def insert(self, name, price): #inserting dish name and its price
        if self.root is None: #inserting first item as root node.
            self.root = MenuNode(name, price)
        else:
            self.recursive_insertion(self.root, name, price) # call for the recursive insetion

    def recursive_insertion(self, node, name, price): # using recursion to insert orders and maintain the property of bst
        newnode = MenuNode(name, price)
        if price < node.price: # adding towards left
            if node.left is None:
                node.left = newnode
                newnode.parent = node
            else:
                self.recursive_insertion(node.left, name, price)
        elif price > node.price: # adding towards right
            if node.right is None:
                node.right = newnode
                newnode.parent = node
            else:
                self.recursive_insertion(node.right, name, price)

    def inorder(self, node,result):  # displays the menu in the ascending order of prices
        if node:
            self.inorder(node.left,result)
            result.append((node.name , node.price))
            self.inorder(node.right,result)

# Graph Class for Delivery Locations
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.graph:
            self.graph[from_node] = {}
        if to_node not in self.graph:
            self.graph[to_node] = {}
        self.graph[from_node][to_node] = weight
        self.graph[to_node][from_node] = weight  # Assuming undirected graph

    def dijkstra(self, start, end):
        distances = {node: float('infinity') for node in self.graph}
        distances[start] = 0
        visited = set()
        path = {}

        while len(visited) < len(self.graph):
            # Find the unvisited node with the smallest distance
            current_node = None
            for node in distances:
                if node not in visited:
                    if current_node is None or distances[node] < distances[current_node]:
                        current_node = node

            if distances[current_node] == float('infinity'):
                break  # All remaining nodes are inaccessible

            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                if neighbor not in visited:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        path[neighbor] = current_node

        return distances, self.get_path(path, start, end)

    def get_path(self, path, start, end):
        current = end
        total_path = []
        while current != start:
            total_path.append(current)
            current = path.get(current)
            if current is None:
                return []  # In case no path exists
        total_path.append(start)
        return total_path[::-1]  # Return reversed path

# the driver class for the program all the adts are combined to work together here
class FoodOrderingSystem:
    def __init__(self):
        self.order_queue = PriorityQueue()
        self.order_history = DoubleLinkedList()
        self.menu_tree = BinarySearchTree()
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.graph = Graph()

        # Initializing some delivery routes
        self.graph.add_edge("Restaurant", "Customer1", 5)
        self.graph.add_edge("Restaurant", "Customer2", 10)
        self.graph.add_edge("Customer1", "Customer3", 3)
        self.graph.add_edge("Customer2", "Customer3", 2)

    def add_order(self, order_name, priority, customer): # adding orders in the queue,dll,stack
        self.order_queue.add_order(order_name, priority)
        self.order_history.add_order(order_name, priority)
        self.undo_stack.push(("add", order_name))
        print(f"Order {order_name} added with priority {priority}")

        # Calculating the shortest path for delivery using the dijkstras algorithm
        distances, path = self.graph.dijkstra("Restaurant", customer)
        if distances[customer] == float('infinity'):
            print(f"No path found to {customer}.")
        else:
            print(f"Shortest distance to {customer}: {distances[customer]} units.")
            print(f"Delivery path: {' -> '.join(path)}")

    def process_order(self): # preparing the order with highest priority
        temp = self.order_queue.delete_order()
        if temp:
            order_name, priority, _ = temp
            print(f"Processing {order_name} with priority {priority}")
            self.order_history.change_order_status(order_name)
            self.undo_stack.push(("process", order_name))
        else:
            print("No more orders to process")

    def undo(self): #using stack for undo opratioins and at the samee tiime adding in redo stack also
        if not self.undo_stack.is_empty():
            action, order_name = self.undo_stack.pop()
            if action == "add":
                self.order_queue.delete_order()  #  removal of the last added order
                print(f"Undo: Order {order_name} removed.")
            elif action == "process":
                self.order_history.change_order_status(order_name)  #  marking the order as pending again
                print(f"Undo: Order {order_name} marked as pending.")

    def redo(self): # using stack for redo operations after the performation of undo if needed
        if not self.redo_stack.is_empty():
            action, order_name = self.redo_stack.pop()
            if action == "add":
                self.add_order(order_name, 1, "Customer1")  # again ading the order
                print(f"Redo: Order {order_name} added.")
            elif action == "process":
                self.process_order() # again processing the order

    def add_menu_item(self, name, price): # adding new items to the menu
        self.menu_tree.insert(name, price)
        print(f"Menu item {name} with price {price} added")

    def view_menu(self): # view mwnu calls the inorder in bst
        print("Menu Items:")
        result=[]
        self.menu_tree.inorder(self.menu_tree.root,result)
        for x in result:
            print(x)
        print()

    def view_order_history(self): #calls the print orders in dll
        print("Order History:")
        self.order_history.print_orders()

    def check_order_status(self, order_name):
        print(self.order_history.check_order_status(order_name))

if __name__ == "__main__":  # Fixed __main__ check
    system = FoodOrderingSystem()

    # Adding menu items with price
    system.add_menu_item("Pizza", 10.99)
    system.add_menu_item("Burger", 5.99)
    system.add_menu_item("Pasta", 7.99)
    system.view_menu()  # View menu items

    # Adding orders
    system.add_order("Order1", 1, "Customer1")  # VIP
    system.add_order("Order2", 2, "Customer2")  # Regular
    system.add_order("Order3", 2, "Customer3")  # Regular

    # Processing orders
    system.process_order()  # Should process Order1
    system.process_order()  # Should process Order2

    # View order history
    system.view_order_history()

    # Check order status
    system.check_order_status("Order2")

    # Undo the last process action
    system.undo()
    system.view_order_history()
    # Redo the last undone action
    system.redo()

    # View final order history
    system.view_order_history()
