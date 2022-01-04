class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    lre = ListNode()
    te = lre

    if (not l1 and not l2):
        return
    if not l1:
        return l2
    if not l2:
        return l1

    lre.val, temp = (l1.val + l2.val, 0) if l1.val + l2.val < 10 else ((l1.val + l2.val) % 10, 1)

    l1 = l1.next
    l2 = l2.next

    while (l1 or l2):
        v1 = 0 if not l1 else l1.val
        v2 = 0 if not l2 else l2.val

        sumTemp, temp = (v1 + v2 + temp, 0) if v1 + v2 + temp < 10 else ((v1 + v2 + temp) % 10, 1)

        tempNode = ListNode()
        tempNode.val = sumTemp
        lre.next = tempNode
        lre = lre.next

        if (l1):
            l1 = l1.next
        if (l2):
            l2 = l2.next

    if (temp == 1):
        tempNode = ListNode()
        tempNode.val = 1
        lre.next = tempNode
    return te


if __name__ == "__main__":
    n3 = ListNode(3, )
    n2 = ListNode(2, n3)
    n1 = ListNode(5, n2)

    k3 = ListNode(3, )
    k2 = ListNode(2, k3)
    k1 = ListNode(5, k2)

    print(addTwoNumbers(k1, n1))
