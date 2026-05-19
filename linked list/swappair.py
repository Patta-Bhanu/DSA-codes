class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next


class Solution:
    def swapPairs(self, head):

        dummy=ListNode(0,head)
        prev,curr=dummy,head

        while curr and curr.next:

            second=curr.next
            nextnode=second.next

            curr.next=nextnode
            second.next=curr
            prev.next=second

            prev=curr
            curr=nextnode

        return dummy.next


def create_ll(arr):

    dummy=ListNode(0)
    temp=dummy

    for num in arr:
        temp.next=ListNode(num)
        temp=temp.next

    return dummy.next


def print_ll(head):

    while head:
        print(head.val,end=" -> " if head.next else "")
        head=head.next

    print()


arr=[1,2,3,4]

head=create_ll(arr)

obj=Solution()

ans=obj.swapPairs(head)

print_ll(ans)