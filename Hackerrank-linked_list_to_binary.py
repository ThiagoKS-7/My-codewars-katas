def convertToNumber(number:ListNode) -> int:
  res = 0
  while head:
    res = 2 * res + head.val
    head = head.next
  return res
