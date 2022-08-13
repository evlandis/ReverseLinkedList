# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    #iterative approach
    def reverseList(self, head):
        #create a prev node to link behind the traversal
        #T O(n), M O(1)
        curr, prev=head,None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev

"""
class Solution(object):
    #recursive approach
    def reverseList(self, head):
        if not head:
            return None
        #T O(n), M O(n)
        newHead=head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next=head
        head.next = None
        
        return newHead
"""
