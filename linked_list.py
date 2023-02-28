class Node:
    def __init__(self, dataVal=None):
        self.dataVal = dataVal
        self.next = None

class SLinkedList:
    def __init__(self):
        self.headNode = None
        
    def listprint(self, cur):
        if cur:
            print (cur.dataVal)
            self.listprint(cur.next)
    
nums = [1,2,3]
list = SLinkedList()
size = len(nums)
for i in range(0, size):
    if list.headNode is None:
        list.headNode = Node(nums[i])
        cur = list.headNode   
    else:
        newNode = Node(nums[i])
        cur.next = newNode
        cur = cur.next 
       
cur = list.headNode   

newNode = Node(0)
newNode.next =list.headNode
list.headNode = newNode
list.listprint(list.headNode)

newNode = Node(10)
cur = list.headNode
while cur.next is not None:
    cur = cur.next

#print('I am here',cur.dataVal)
cur.next = newNode
list.listprint(list.headNode)
