# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1, l2):
        # 進位用
        temp = 0
        # 指向同一個節點，first追蹤每一個節點，result最後查看所有的節點
        first = result = ListNode(0)
        
        while l1 or l2:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            # 進位, 每個digit的和
            temp, digit_sum = divmod(val_1 + val_2 + temp, 10)

            first.next = ListNode(digit_sum)
            first = first.next
            # 如果沒有值則回傳None代表沒了
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if temp:# 如果最後一個temp還有代表最後一個digit必須要進位
            first.next = ListNode(temp)
         # 最後的結果
        return result.next
