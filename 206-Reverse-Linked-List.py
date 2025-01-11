# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        currNode = head
        while currNode is not None:
            next = currNode.next
            currNode.next = dummyNode.next
            dummyNode.next = currNode
            currNode = next
        return dummyNode.next