class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        # find middle node in the list
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        right_pointer = slow.next

        # if fast pointer has next node, then the number of nodes is even
        is_even = fast.next is not None
        
        # Reverse first half of the linked list
        prev = None
        current_node = head
        while current_node != slow:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        if is_even:
            current_node.next = prev
        else:
            current_node = prev

        left_pointer = current_node

        # Iterate from the middle to left and right and compare values
        while left_pointer is not None:
            if left_pointer.val != right_pointer.val:
                return False
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next
        return True
