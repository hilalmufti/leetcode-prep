from typing import List
class ListNode:
    def __init__(self, value: int = 0, next: 'ListNode' = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        current: ListNode = self.head
        i: int = 0
        while i < index:
            current = current.next
            i += 1
        return current.value

    def insertHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)
        self.length += 1
        if self.length == 1:
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        if self.length == 0:
            self.insertHead(val)
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
            self.length += 1

    def remove(self, index: int) -> bool:
        removeable: bool = self.get(index) != -1
        if removeable:
            if index != 0:
                current: ListNode = self.head
                i: int = 0
                while i < index - 1:
                    current = current.next
                    i += 1
                current.next = current.next.next
            else:
                self.head = self.head.next
            self.length -= 1
        return removeable

    def getValues(self) -> List[int]:
        out: list = []
        current: ListNode = self.head
        while current is not None:
            out.append(current.value)
            current = current.next
        return out

    def __str__(self):
        return str(self.getValues())


def main():
    l: LinkedList = LinkedList()
    l.insertHead(1)
    print(l)
    l.insertHead(2)
    print(l)
    l.insertTail(3)
    print(l)
    l.insertTail(4)
    print(l)
    l.insertHead(5)
    print(l)
    print(l.get(0))
    print(l.get(2))
    print(l.get(4))
    print(l.remove(2))
    print(l)
    print(l.remove(0))
    print(l)
    l.insertHead(6)
    print(l)
    l.insertTail(7)
    print(l)
    print(l.getValues())
    print(l.get(5))


if __name__ == "__main__":
    main()
