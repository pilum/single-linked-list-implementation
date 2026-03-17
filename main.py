class Node():
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self, head: Node=None) -> None:
        """Creates an instance of a LinkedList

        Args:
            head (Node, optional): Defaults to None when no head is given.
        """
        self.head = head

    def append_right(self, n: Node) -> None:
        """Appends a Node to the end of a LinkedList. If the LinkedList is empty the Node will be set as head.

        Args:
            n (Node): Node object
        """
        if self.head == None:
            self.head = n
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = n

    def append_left(self, n: Node) -> None:
        """Appends a Node at the begin of the LinkedList and sets it as new head.

        Args:
            n (Node): Node object
        """
        n.next = self.head
        self.head = n

    def pop_right(self) -> Node:
        """Removes the last Node of a LinkedList. If the LinkedList is empty it returns None. If the LinkedList contains only
        one Node it removes and returns the head node.

        Args:
            n (Node): Node object

        Returns:
            Node: Node object which got removed from the LinkedList
        """
        if self.head == None:
            return None

        if self.head.next == None:
            val = self.head
            self.head = None
            return val

        current = self.head
        while current.next.next != None:
            current = current.next

        val = current.next
        current.next = None

        return val

    def pop_left(self) -> Node:
        """Removes the first (head) Node of the LinkedList.

        Returns:
            Node: Node Object which got removed from the head of the LinkedList.
        """
        if self.head == None:
            return None

        val = self.head
        self.head = self.head.next
        return val



linked_list = LinkedList()
n1 = Node(5)
n2 = Node(6)
n3 = Node(7)

linked_list.append_right(n1)
linked_list.append_right(n2)
linked_list.append_right(n3)

print(n1.next)
print(n2.next)
print(n3.next)

x = linked_list.pop_left()
print(x.value)