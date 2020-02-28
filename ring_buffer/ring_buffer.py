from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        pass

        # If capacity is full
        if self.storage.length == self.capacity:
            # Replace oldest
            self.current.value = item
            # Reset oldest
            self.current = self.current.next
        else:
            # Add item to tail (most recent)
            self.storage.add_to_tail(item)

            if self.storage.length == self.capacity:
                self.storage.tail.next = self.storage.head
            else:
                # Reset oldeset also if you dont put this base case then the get wont work
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # added count to make sure we dont go over the limit cause fixed size
        count = 0
        node = self.storage.head
        while count is not self.storage.length:
            count += 1
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
