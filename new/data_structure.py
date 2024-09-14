from typing import Optional,List, Any


class ListNode1:
    def __init__(self, x):
        self.val = x
        self.next = None

n1 = ListNode1(1)
n2 = ListNode1(2)
n3 = ListNode1(3)

n1.next= n2
n2.next = n3

#
# print(n1.next.next.val)


class Solution:
    """
    递归版：链表反转
    """
    def reverseBookList(self, head: Any) -> List[int]:
        return self.reverseBookList(head.next) + [head.val] if head else []
# solution = Solution()
# reverse_list = solution.reverseBookList(n1)
# print(reverse_list)

def reverse(heads):
    print(type(heads))
    cur = heads
    pre = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

reverse(n1)

print(n1.val)
print(n1.next)


