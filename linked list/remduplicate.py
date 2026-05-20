from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(
        self,
        head: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if prev.next == curr:
                prev = prev.next

            else:
                prev.next = curr.next

            curr = curr.next

        return dummy.next


def print_list(head):

    temp = head

    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next

    print("None")


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)

obj = Solution()

new_head = obj.deleteDuplicates(head)

print_list(new_head)