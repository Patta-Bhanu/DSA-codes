class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next


class Solution:
    def rotateRight(self, head, k):

        if not head or not head.next:
            return head

        temp=head
        count=1

        while temp.next:
            temp=temp.next
            count+=1

        k=k%count

        if k==0:
            return head

        temp.next=head

        rem=count-k

        temp=head

        for i in range(rem-1):
            temp=temp.next

        newhead=temp.next
        temp.next=None

        return newhead


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


arr=[1,2,3,4,5]
k=2

head=create_ll(arr)

obj=Solution()

ans=obj.rotateRight(head,k)

print_ll(ans)