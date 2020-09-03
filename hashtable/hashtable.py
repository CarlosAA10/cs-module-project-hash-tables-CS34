class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.list = [None] * self.capacity
        # taking load factor into account, we must create a counter for it
        # this value will be increased when an item is added to this entire array
        self.ocp_space = 0
        # using the ocp_space / by self.capacity we measure the load factor
        # self.load_factor = self.ocp_space / self.capacity
        # if load factor is above .7, time to increase capacity
        # if load factor is below .2 then time to decrease capacity
        
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return  self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return (self.ocp_space / self.capacity)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


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
        # Your code here
        # we hashed an index
        index = self.hash_index(key)
        # we replaced values and continued on
        # self.list[index] = value

        # to handle this with a linked list will be to make the nodes
        # be in a position, and connect them all with next pointers
        # we will use the HashTableEntry class for this

        # if it is, we will make the value be a hash table entry
        # we will check and see if it is empty (None)
        if self.list[index] is None:
            # self.list[index] = HashTableEntry(key, value)
            # we will always add 1 to the ocp_space value when we add something
            self.list[index] = HashTableEntry(key, value)
            self.ocp_space += 1
        else:
            # if there is a node here, we must traverse through the linked list if it is more
            # than one node connected here
            cur = self.list[index]
            while cur.next is not None:
                # if the key of cur is the same as the key provided, it is an override
                if cur.key == key:
                    # we will make the value of this current key equal to the new 
                    # value we want to be overwritten, we might want to return the old value
                    # as a confirmation for the user
                    old_value = cur.value
                    cur.value = value
                    # we will print a message to the user
                    print(f"the new value: {cur.value}")
                    print(f"You have successfully updated {old_value} to {cur.value}")
                # we will traverse through , so making cur = cur.next
                cur = cur.next
            # when we exit the while loop we have successfully made it to the end
            # we will now take the cur which has changed to the last one
            # and add the .next to be this new hashtable entry
            # don't forget to increase self.ocp space
            if cur.key == key:
                old_value = cur.value
                cur.value = value
                print(f"the new value: {cur.value}")
                print(f"You have successfully updated {old_value} to {cur.value}")
            else:
                cur.next = HashTableEntry(key, value)
                self.ocp_space += 1
        




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # must hash the index first to find it's position
        index = self.hash_index(key)
        cur = self.list[index]
        # if there is nothingin that spot, means that something is not there
        # we will return a message saying it does not exist 
        if cur is None:
            print(f"Key does not exist")
        else:
            
            while cur is not None:

                if cur.key == key:
                    old_value = cur.value
                    cur.value = None
                    self.ocp_space -= 1
                    print(f"You have deleted {old_value}")
                cur = cur.next

            return f"Key was not found"

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        cur = self.list[index]
        if cur is None:
            return None
        else:
            # how to access the item we want based off key
            while cur is not None:

                # if we find the key, delete the value associated with it
                # or you can delete any mentioning of that node 
                if cur.key == key:
                    # return the value 
                    return cur.value
                # how we traverse through linked list
                cur = cur.next
            # we are at none, meaning we weren't able to find the key in the linked list
            return cur


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # when resizing, we want to create a new array, make it be twice the amount of 
        # elements currently in capacity
        if self.get_load_factor() > .7:
            # creates new array
            new_arr = [None] * new_capacity
            
            # now we want to rehash every item in our current list
            # we will run a for loop to rehash each item on there, 
            # and if there are nodes in each .next pointer in that position
            # we want to traverse through the linked list and rehash each key there is
            # and then do a put operation on each node
            # our current hash index function does not have the proper capacity set up. 
            # we would need to change it to be double the size now and then call our hash index function
            self.capacity = new_capacity

            for item in self.list:

                # we want to hash the item we are at, then check for next pointers
                # and then hash those items as well
                index = self.hash_index(item.key)
                # we have hashed the current node's key we are in
                new_arr[index] = HashTableEntry(item.key, item.value)
                # this handles rehashing every node that is in the linked list 
                # if there is a linked list on that position
                if item.next and item.next is not None:

                    cur = item.next

                    while cur is not None:
                        # we want to rehash every node's key that we are on
                        # and call that variable new_index
                        # the new index will then refer to a position in 
                        # new_arr and we will make that be equal to a new 
                        # hash table entry with that node's current key and value 
                        # passed into it
                        new_index = self.hash_index(cur.key)

                        new_arr[new_index] = HashTableEntry(cur.key, cur.value)
                        #traverse through linked list 
                        cur = cur.next
                    # we have exited the while loop, have gone through the entire linked list
                # all linked list nodes are accounted for and hashed into the new_arr
                # now outside of the for loop, we want to make sure our self.list is now 
                # the new_arr that we have with all the rehashed values
            self.list = new_arr
            

# ht = HashTable(1)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")



    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")
