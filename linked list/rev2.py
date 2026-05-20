from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        for _ in range(right - left):

            nxt = curr.next

            curr.next = nxt.next

            nxt.next = prev.next

            prev.next = nxt

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
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

obj = Solution()

new_head = obj.reverseBetween(head, 2, 4)

print_list(new_head)