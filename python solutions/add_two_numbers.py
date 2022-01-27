class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers( l1 , l2):
        carry=0
        ref=ans=ListNode()
        
        while (l1!=None and l2!=None):
            n=carry+l1.val+l2.val
            if n>=10:
                n = n-10
                carry=1
            else:
                carry=0
            ans.next=ListNode(n)
            ans=ans.next
            l1=l1.next
            l2=l2.next
        while(l1!=None):
            n=carry+l1.val
            if n>=10:
                n = n-10
                carry=1
            else:
                carry=0
            ans.next=ListNode(n)
            
            ans=ans.next
            l1=l1.next
        while(l2!=None):
            n=carry+l1.val
            if n>=10:
                n = n-10
                carry=1
            else:
                carry=0
            ans.next=ListNode(l1)
            ans=ans.next
            l1=l1.next
        return ref.next
def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next
addTwoNumbers(lst2link([2,4,3]),lst2link([5,6,4]))