"""
https://leetcode.com/problems/middle-of-the-linked-list/description/

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            print("slow:", slow.val)
            print("fast:", fast.val)
            print("*******")
            slow = slow.next
            fast = fast.next.next


        return slow

inp = [1,2,3,4,5, 6]
head = ListNode(val=inp[0])
head.next = ListNode(val=inp[1])
node = head.next
for i in range(3, len(inp)+1):
    node.next = ListNode(i)
    node = node.next
# while head:
#     print(head.val)
#     head = head.next
result = Solution().middleNode(head=head)
print(result.__dict__)

