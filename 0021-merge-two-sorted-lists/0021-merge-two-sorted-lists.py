# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        head = ListNode()
        cur=head
        while head1!=None or head2!=None:
            if head2==None or (head1!=None and head1.val<=head2.val):
                cur.next=ListNode(head1.val)
                cur = cur.next
                head1 = head1.next
                
            else:
                cur.next=ListNode(head2.val)
                cur = cur.next
                head2 = head2.next
        return head.next