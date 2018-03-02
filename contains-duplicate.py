class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
