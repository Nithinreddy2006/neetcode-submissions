# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if there are at least k nodes remaining
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        
        if count < k:
            return head  # Not enough nodes, return as-is
        
        # Reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # head is now the tail of the reversed group
        # Recursively reverse the rest and connect
        head.next = self.reverseKGroup(curr, k)
        
        # prev is now the new head of the reversed group
        return prev