'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2 :
            return list1
        if not list1 or not list2:
            return list1 if not list2 else list2
        tempNode = ListNode()
        HeadNode = ListNode()
        while True:
            if not list1 or not list2:
                if list1:
                    tempNode.next = list1
                if list2:
                    tempNode.next = list2
                return HeadNode.next
            if list1.val <= list2.val:
                if HeadNode.next is None:
                    HeadNode.next = list1
                    tempNode = list1
                    list1 = list1.next
                else:
                    tempNode.next = list1
                    tempNode = tempNode.next
                    list1 = list1.next
            else:
                if HeadNode.next is None:
                    HeadNode.next = list2
                    tempNode = list2
                    list2 = list2.next
                else:
                    tempNode.next = list2
                    tempNode = tempNode.next
                    list2 = list2.next


if __name__ == "__main__":
    s = Solution()
    l4 = ListNode(4)
    l2 = ListNode(2, l4)
    l1 = ListNode(1, l2)
    
    x4 = ListNode(4)
    x3 = ListNode(3, x4)
    x1 = ListNode(1, x3)
    
    #res = s.mergeTwoLists(l1, x1)
    #print(res)
    res = s.mergeTwoLists(ListNode(2), ListNode(1))
    res = s.mergeTwoLists([], [])
    print(res)
    res = s.mergeTwoLists([], x3)
    print(res)
