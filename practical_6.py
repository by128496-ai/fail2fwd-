class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == original_index:
                print("Table is full!")
                return
        self.table[index] = key
        print(f"{key} inserted at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"{key} found at index {index}")
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        print(f"{key} not found")
        return False

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = None
                print(f"{key} deleted from index {index}")
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        print(f"{key} not found")
        return False

    def display(self):
        print("Hash Table:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

# Example usage
ht = HashTable(10)
ht.insert(23)
ht.insert(44)
ht.insert(33)
ht.display()
ht.search(44)
ht.delete(33)
ht.display()