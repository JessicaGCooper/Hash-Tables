class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_capacity = 8
        self.size = 0
        self.size_up_ratio = 0.7
        self.size_down_ratio = 0.2
        self.storage = [None] * self.capacity
        self.current_size_ratio = 0
        
    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hashed_key = 5381
        for char in key:
            hashed_key = ((hashed_key * 33) + ord(char))
        return hashed_key & 0xffffffff


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        
        if node is None:
            self.resize()
            self.storage[index] = HashTableEntry(key, value)
            self.size += 1
        else:
            prev = None
            while node is not None and node.key != key:
                    prev = node
                    node = node.next
            if node is not None and node.key == key:
                    node.value = value
            else:
                self.resize()
                node = prev
                node.next = HashTableEntry(key, value)
                self.size += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)
        node = self.storage[index]
        prev = None

        while node is not None and node.key != key:
                prev = node
                node = node.next
        if node is None:
            print('Warning: the key is not found.')
        elif node.key == key:
            self.size -= 1
            value = node.value
            if prev is None:
                self.storage[index] = node.next
                self.desize()
            else:
                prev.next = prev.next.next
                self.desize()
            return value


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        
        if self.storage[index] is None:
            return None
        else:
            while node is not None and node.key != key:
                    node = node.next
            if node is not None and node.key == key:
                    value = node.value
                    node = node.next
                
                    return value
            else:
                return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.current_size_ratio = float(self.size/self.capacity)

        if self.current_size_ratio >= self.size_up_ratio:
            old_storage = self.storage
            self.capacity = self.capacity * 2
            new_storage = [None] * self.capacity
            self.storage = new_storage
            self.size = 0


            # old_size = self.size
            ##this and the last line keep the integrity of the count since the put method will add to the count
            ##perhaps resetting to zero at the beginning of the resize would have the same effect?

            for stored_node in old_storage:
                while stored_node is not None:
                    self.put(stored_node.key, stored_node.value)
                        # index = self.hash_index(stored_node.key)
                        # new_node = new_storage[index]

                        # if new_node is None:
                        #     new_storage[index] = HashTableEntry(stored_node.key, stored_node.value)
                        # else:
                        #     prev = None
                        #     while new_node is not None and new_node.key != stored_node.key:
                        #         prev = new_node
                        #         new_node = new_node.next
                        #     if new_node is not None and new_node.key == stored_node.key:
                        #         new_node.value = stored_node.value
                        #     else:
                        #         new_node = prev
                        #         new_node.next = HashTableEntry(stored_node.key, stored_node.value)
                    stored_node = stored_node.next
                    ##above line & the while loop iterates through any linked list stored as an element in the storage list
                    ##the for loop iterates through the storage list

            # self.size = old_size

    def desize(self):
        self.current_size_ratio = float(self.size/self.capacity)

        if self.current_size_ratio <= self.size_down_ratio and self.capacity//2 >= self.min_capacity:
            old_storage = self.storage
            self.capacity = self.capacity//2
            new_storage = [None] * self.capacity
            self.storage = new_storage
            self.size = 0

            for stored_node in old_storage:
                while stored_node is not None:
                    self.put(stored_node.key, stored_node.value)
                    stored_node = stored_node.next
        





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")
    ht.put("line_4", "Whatever")
    ht.put("line_1", "Tiny hash tables")
    ht.put("line_12", "node2 in one")
    ht.put("line_5", "Jane")
    ht.put("line_6", "Perry")
    ht.put("line_7", "Alice!")
    ht.put("line_8", "Carol")
    ht.put("line_9", "Peter")
    ht.put("line_10", "Taurus")
    ht.put("line_11", "Jane")
    ht.put("line_12", "Perry")
    ht.put("line_13", "Alice!")
    ht.put("line_14", "Carol")
    ht.put("line_15", "Peter")
    ht.put("line_16", "Taurus")
    print(f'{ht.capacity} {ht.size}')
    ht.delete("line_1")
    ht.delete("line_5")
    ht.delete("line_16")
    ht.delete("line_57")
    ht.delete("line_4")
    ht.delete("line_2")
    ht.delete("line_12")
    print(f'{ht.capacity} {ht.size}')
    ht.delete("line_6")
    ht.delete("line_7")
    ht.delete("line_8")
    ht.delete("line_9")
    print(f'{ht.capacity} {ht.size}')
    ht.delete("line_10")
    ht.delete("line_11")
    ht.delete("line_12")
    ht.delete("line_13")
    ht.delete("line_14")
    ht.delete("line_15")
    print(f'{ht.capacity} {ht.size}')


    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    print("")


