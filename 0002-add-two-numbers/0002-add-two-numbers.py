# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy node to form the resultant linked list
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Traverse both lists
        while l1 or l2 or carry:
            # Get the current values (0 if the node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Create a new node with the sum of the current digits
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in l1 and l2
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next

        