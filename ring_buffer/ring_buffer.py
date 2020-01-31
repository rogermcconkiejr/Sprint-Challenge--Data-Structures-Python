from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None


    def append(self, item):
        current = self.storage.tail
        if self.storage.length == self.capacity:
                current.value = item
                current = current.prev
                if not current.prev:
                    current = self.storage.tail
                         
        else:
            self.storage.add_to_head(item)
        
        
        # if self.storage.length < self.capacity:
        #     self.storage.add_to_head(item)
        # else:
        #     current.value = item
        #     current = current.next
        #     # if current.prev != True:
        #     #     current.prev = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = [None] *self.storage.length
        current_count = 0
        if self.storage.head == None:
            return list_buffer_contents
        current = self.storage.tail
        while current:
            if current_count == self.storage.length:
                current_count -= 1
            list_buffer_contents[current_count]= current.value
            current_count += 1
            current = current.prev  
            

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
