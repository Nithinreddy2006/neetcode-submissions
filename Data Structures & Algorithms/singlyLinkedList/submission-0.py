from typing import List

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        
        if index == 0:
            self.head = self.head.next
            return True
        
        curr = self.head
        i = 0
        
        while curr.next:
            if i == index - 1:
                curr.next = curr.next.next
                return True
            curr = curr.next
            i += 1
        
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values