# Food Ordering System

A comprehensive Python-based food ordering management system that demonstrates the implementation of multiple data structures and algorithms including Priority Queues, Doubly Linked Lists, Stacks, Binary Search Trees, and Graphs.

## Features

### 1. **Priority-Based Order Management**
- Orders are processed based on priority levels (1 = VIP, 2 = Regular, etc.)
- Orders with the same priority are handled in FIFO (First In, First Out) order
- Implemented using a Min-Heap Priority Queue

### 2. **Order History Tracking**
- Complete order history with delivery status tracking
- Implemented using Doubly Linked List
- Check status of any order (Pending/Delivered)
- Mark orders as delivered

### 3. **Undo/Redo Functionality**
- Undo recent actions (adding orders, processing orders)
- Redo previously undone actions
- Implemented using Stack data structure

### 4. **Menu Management**
- Add menu items with prices
- View menu sorted by price (ascending order)
- Implemented using Binary Search Tree (BST)

### 5. **Delivery Route Optimization**
- Find shortest delivery path from restaurant to customer
- Calculate minimum delivery distance
- Implemented using Graph with Dijkstra's algorithm

## Data Structures Used

| Data Structure | Purpose | Implementation |
|---------------|---------|----------------|
| **Min-Heap Priority Queue** | Order queue management | Array-based heap with heapify operations |
| **Doubly Linked List** | Order history tracking | Bidirectional node traversal |
| **Stack** | Undo/Redo operations | Linked list-based stack |
| **Binary Search Tree** | Menu item storage | Price-based BST ordering |
| **Graph** | Delivery route network | Adjacency list with weighted edges |

## Class Structure

### `PriorityQueue`
- `add_order(order_name, priority)`: Add order to queue
- `delete_order()`: Remove and return highest priority order
- `heapify_up(i)`: Maintain heap property after insertion
- `heapify_down(i)`: Maintain heap property after deletion

### `DoubleLinkedList`
- `add_order(order_name, priority)`: Add order to history
- `check_order_status(order_name)`: Check if order is delivered/pending
- `change_order_status(order_name)`: Mark order as delivered
- `print_orders()`: Display all orders in history

### `Stack`
- `push(data)`: Add element to stack
- `pop()`: Remove and return top element
- `peek()`: View top element without removing
- `is_empty()`: Check if stack is empty

### `BinarySearchTree`
- `insert(name, price)`: Add menu item
- `inorder(node, result)`: Traverse tree in sorted order

### `Graph`
- `add_edge(from_node, to_node, weight)`: Add delivery route
- `dijkstra(start, end)`: Find shortest path between locations

### `FoodOrderingSystem` (Main Driver Class)
- `add_order(order_name, priority, customer)`: Add new order
- `process_order()`: Process highest priority order
- `undo()`: Undo last action
- `redo()`: Redo last undone action
- `add_menu_item(name, price)`: Add item to menu
- `view_menu()`: Display menu sorted by price
- `view_order_history()`: Display all orders
- `check_order_status(order_name)`: Check specific order status

## Usage Example

```python
# Initialize the system
system = FoodOrderingSystem()

# Add menu items
system.add_menu_item("Pizza", 10.99)
system.add_menu_item("Burger", 5.99)
system.add_menu_item("Pasta", 7.99)

# View menu (sorted by price)
system.view_menu()

# Add orders with priority (1 = VIP, 2 = Regular)
system.add_order("Order1", 1, "Customer1")  # VIP
system.add_order("Order2", 2, "Customer2")  # Regular
system.add_order("Order3", 2, "Customer3")  # Regular

# Process orders (highest priority first)
system.process_order()  # Processes Order1 (VIP)
system.process_order()  # Processes Order2 (first regular)

# View order history
system.view_order_history()

# Check specific order status
system.check_order_status("Order2")

# Undo last action
system.undo()

# Redo undone action
system.redo()
```

## Sample Output

```
Menu item Pizza with price 10.99 added
Menu item Burger with price 5.99 added
Menu item Pasta with price 7.99 added
Menu Items:
('Burger', 5.99)
('Pasta', 7.99)
('Pizza', 10.99)

Order Order1 added with priority 1
Shortest distance to Customer1: 5 units.
Delivery path: Restaurant -> Customer1

Order Order2 added with priority 2
Shortest distance to Customer2: 10 units.
Delivery path: Restaurant -> Customer2

Processing Order1 with priority 1
Order Order1 has been marked as delivered.

Order History:
Order: Order1, Priority: 1, Status: Delivered
Order: Order2, Priority: 2, Status: Pending
Order: Order3, Priority: 2, Status: Pending
```

## Algorithm Complexities

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Add Order (Priority Queue) | O(log n) | O(n) |
| Process Order | O(log n) | O(1) |
| Add to History | O(1) | O(n) |
| Check Order Status | O(n) | O(1) |
| Undo/Redo | O(1) | O(n) |
| Add Menu Item | O(log n) average | O(n) |
| View Menu | O(n) | O(n) |
| Dijkstra's Algorithm | O(V²) | O(V) |

Where n = number of orders/items, V = number of vertices in graph

## Key Features

- **Priority Handling**: VIP orders are automatically prioritized
- **FIFO for Same Priority**: Orders with identical priority are processed in order received
- **Order Tracking**: Complete history with delivery status
- **Flexible Menu**: Dynamic menu management with price-based sorting
- **Route Optimization**: Automatic calculation of shortest delivery path
- **Action History**: Full undo/redo support for operations

## Requirements

- Python 3.x
- No external dependencies required

## Running the Program

```bash
python food_ordering_system.py
```

## Future Enhancements

- Add GUI interface
- Implement customer authentication
- Add order cancellation feature
- Support for order modifications
- Real-time order tracking
- Database integration for persistence
- Multiple restaurant support
- Advanced delivery route optimization with traffic data

## License

This project is open source and available for educational purposes.

## Author

Created as a demonstration of data structures and algorithms in Python.
