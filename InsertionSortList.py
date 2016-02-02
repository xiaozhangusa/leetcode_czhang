# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last, cur= head, head
        cnt = 0
        while cur:
        # while cnt < 2:
            # print "cur: ", cur.val
            self.printList(head)
            if cur.val < last.val:
                # print "case 1: ", cur.val, last.val
                if last == head:
                    last.next = cur.next
                    head = cur
                    cur.next = last
                    cur = last
                    print "last == head"
                    self.printList(head)
                else:
                    print "last != head"
                    last_tmp, cur_tmp = head, head
                    while cur_tmp.val < cur.val:
                        last_tmp = cur_tmp
                        cur_tmp = cur_tmp.next
                    if cur_tmp == head:
                        last.next = cur.next
                        cur.next = head
                        head = cur
                        cur = last.next
                    else:
                        last.next = cur.next
                        last_tmp.next = cur
                        cur.next = cur_tmp
                        if cur_tmp is last:
                            last = cur
                        cur = last.next
                    self.printList(head)
            else:
                # print "case 2: ", cur.val, last.val
                last = cur
                cur = cur.next
            cnt += 1
            print "cnt: ", cnt
        print "final head: ", head.val
        return head

    def printList(self, head):
        if head == None:
            print "empty list"
        else:
            cur = head
            while cur:
                print str(cur.val) + '->',
                cur = cur.next
            else:
                print '.'


def main():
    sol = Solution()
    hd = ListNode(2)
    nd1 = ListNode(3)
    hd.next = nd1
    nd2 = ListNode(1)
    nd1.next = nd2
    nd3 = ListNode(5)
    nd2.next = nd3
    nd4 = ListNode(4)
    nd3.next = nd4
    nd5 = ListNode(-4)
    nd4.next = nd5
    print "-------------- before ---------------"
    sol.printList(hd)
    print
    print "-------------- sort ---------------"
    hd =sol.insertionSortList(hd)
    print
    print "-------------- after ---------------"
    sol.printList(hd)
    return

if __name__ == "__main__":
    main()