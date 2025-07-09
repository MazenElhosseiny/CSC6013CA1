# class Node
#
# Instance variables:
#    Data - the value
#    Next - the next node

class Node:
    def __init__(self, d):
        self.Data = d
        self.Next = None

class LinkedList:
    def __init__(self, d=None):
        if (d == None): # an empty list
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header
    def nextCurrent(self):
        if (self.Current.Next is not None):
            self.Current = self.Current.Next
        else:
            self.Current = self.Header
    def resetCurrent(self):
        self.Current = self.Header
    def getCurrent(self):
        if (self.Current is not None):
            return self.Current.Data
        else:
            return None
    def insertBeginning(self, d):
        if (self.Header is None): # if list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:                     # if list not empty
            Tmp = Node(d)
            Tmp.Next = self.Header
            self.Header = Tmp
    def insertCurrentNext(self, d):
        if (self.Header is None): # if list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:                     # if list not empty
            Tmp = Node(d)
            Tmp.Next = self.Current.Next
            self.Current.Next = Tmp
    def removeBeginning(self):
        if (self.Header is None): # if list is empty
            return None
        else:                     # if list not empty
            ans = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header
            return ans
    def removeCurrentNext(self):
        if (self.Current.Next is None): # if there is no node
            return None                 #        after Current
        else:                           # if there is
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return ans
    def printList(self,msg="====="):
        p = self.Header
        print("====",msg)
        while (p is not None):
            print(p.Data, end=" ")
            p = p.Next
        if (self.Current is not None):
            print("Current:", self.Current.Data)
        else:
            print("Empty Linked List")
        input("----------------")

def main():
    numbers = []
    with open("data.txt", "r") as file:
        for line in file:
            numbers.append(int(line.strip()))
    numbers.sort()
    L = LinkedList()
    i = len(numbers)
    while i > 0:
        i -= 1
        L.insertBeginning(numbers[i])
    L.printList()
    while True:
        choice = input("Enter a number to look for in the Linked List: ")
        if not choice:
            print("No input received.")
        else:
            try:
                choice_int = int(choice)
                break
            except ValueError:
                print("Invalid Input. Please enter integer value.")

    L.resetCurrent()
    while L.getCurrent() is not None:
        if L.getCurrent() == choice_int:
            ans = L.removeBeginning()
            print(f"{ans} removed from the head of the Linked List")
        if L.Current.Next is not None and L.Current.Next.Data == choice_int:
            ans = L.removeCurrentNext()
            print(f"{ans} removed from the Linked List")
            L.printList()
        L.nextCurrent()

            

main()

