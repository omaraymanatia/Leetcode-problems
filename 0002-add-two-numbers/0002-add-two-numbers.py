# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=''
        num2=''
        head1=l1
        head2=l2
        while head1!=None:
            num1+=str(head1.val)
            head1=head1.next
        while head2!=None:
            num2+=str(head2.val)
            head2=head2.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        num = int(num1) + int(num2)
        ans = str(num)[::-1]
        head = ListNode()
        cur = head
        for val in ans:
            cur.next = ListNode(int(val))
            cur=cur.next
        return head.next