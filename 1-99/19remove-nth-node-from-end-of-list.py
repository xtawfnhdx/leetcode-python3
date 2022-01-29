'''
给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nextAddress = []
        res = ListNode(0, head)
        # 存储头结点
        nextAddress.append(res.next)
        while head:
            nextAddress.append(head.next)
            head = head.next
        if n==len(nextAddress)-1:
            return nextAddress[0].next
        tt = nextAddress[-n - 2]
        tt.next = nextAddress[-n]
    
        return res.next


if __name__ == '__main__':
    s = Solution()
    l3 = ListNode(3)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    
    print(s.removeNthFromEnd(l3,1))
    print(s.removeNthFromEnd(l1, 2))
