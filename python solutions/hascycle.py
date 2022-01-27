class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def hasCycle( head ):
        p1=head
        p2=head
        while (p1 and p2):
            p1=p1.next
            p2=p2.next.next
            if(p1==p2):
                return True
        return False
            
    
n1=ListNode(3)
n2=ListNode(2)
n3=ListNode(0)
n4=ListNode(-4)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n2
hasCycle(n1)
