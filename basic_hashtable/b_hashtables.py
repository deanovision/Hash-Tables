

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max_len):
    hash_value = 5381
    # string_array = string.split()
    for c in string:
        print(c)
        hash_value = (hash_value * 33) + ord(c)
        print(hash_value, max_len)
    return hash_value % max_len


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    key_hash = hash(key, hash_table.capacity)
    new_pair = Pair(key, value)
    if hash_table.storage[key_hash]:
        print("hash already exists")
    else:
        hash_table.storage[key_hash] = new_pair

    # def insert(self, key, value):
    #     key_hash = _djb2x_hash(key)
    #     bucket_index = key_hash % self.capacity

    #     new_node = _Node(key, value)
    #     existing_node = self.bucket_array[bucket_index]

    #     if existing_node:
    #         last_node = None
    #         while existing_node:
    #             if existing_node.key == key:
    #                 # found existing key, replace value
    #                 existing_node.value = value
    #                 return
    #             last_node = existing_node
    #             existing_node = existing_node.next_node
    #         # if we get this far, we didn't find an existing key
    #         # so just append the new node to the end of the bucket
    #         last_node.next_node = new_node
    #     else:
    #         self.bucket_array[bucket_index] = new_node

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
    hash_key = hash(key, hash_table.capacity)
    hash_table.storage[hash_key] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hash_key = hash(key, hash_table.capacity)
    if hash_table.storage[hash_key] is None:
        return None
    else:
        return hash_table.storage[hash_key]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
