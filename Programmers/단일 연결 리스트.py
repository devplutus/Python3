class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def init_list():
    global node1
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4

def print_list():
    global node1
    node = node1
    while node:
        print(node.data)
        node = node.next

def insert_node(data):
    global node1

    new_node = Node(data)
    prev_node = node1
    next_node = node1.next

    try:

        while next_node.data <= data:
            prev_node = next_node
            next_node = next_node.next

    except:
        prev_node.next = new_node

    else:
        prev_node.next = new_node
        new_node.next = next_node

def delete_node(data):
    global node1

    prev_node = node1
    next_node = node1.next

    if(prev_node.data == data):
        del prev_node
        return

    while next_node:
        if(next_node.data == data):
            prev_node.next = next_node.next
            del next_node
            return

        prev_node = next_node
        next_node = next_node.next

if __name__ == "__main__":
    init_list()
    insert_node(5)
    delete_node(5)
    print_list()

    