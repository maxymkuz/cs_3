from abc import ABC
import math


class TableFather:
    def __init__(self):
        self.collisions = 0

    def add(self, elem):
        raise NotImplementedError

    def find(self, elem):
        raise NotImplementedError


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class ChainedDivisionHash(TableFather, ABC):
    def __init__(self, size):
        super().__init__()
        self.size = 78787 % (3 * size)  # Optimal number
        self.T = [None] * self.size

    @staticmethod
    def hash(elem, m):
        return elem % m

    def add(self, elem):
        index = self.hash(elem, self.size)
        if self.T[index] is None:
            self.T[index] = Node(elem)
        else:
            node = self.T[index]
            self.collisions += 1
            while node.next is not None:
                self.collisions += 1
                node = node.next
            node.next = Node(elem)

    def find(self, elem):
        index = self.hash(elem, self.size)
        node = self.T[index]
        while node is not None:
            if node.val == elem:
                return elem
            node = node.next
        return False  # if we go through every element in cell


class ChainedMultiplicationHash(ChainedDivisionHash, ABC):
    def __init__(self, size):
        super().__init__(size)
        self.size = 2**(math.floor(math.log2(2*size)))
        # Optimal prime number that is power of 2
        self.T = [None] * self.size

    @staticmethod
    def hash(elem, m):
        a = (math.sqrt(5) - 1) / 2
        return math.floor(m * (elem * a % 1))


class OpenAddressLinear(TableFather, ABC):
    def __init__(self, size):
        super().__init__()
        self.size = 199999 % (3 * size)  # Optimal prime number
        self.T = [None] * self.size
        # print(len(self.T))

    def hash(self, elem, m):
        return ChainedDivisionHash.hash(elem, m)

    def skip(self, i, elem):
        return i

    def add(self, elem):
        hashed_idx = self.hash(elem, self.size)
        idx = hashed_idx
        i = 1
        while self.T[idx] is not None:
            self.collisions += 1
            idx = (hashed_idx + self.skip(i, elem)) % self.size
            i += 1
        self.T[idx] = elem

    def find(self, elem):
        hashed_idx = self.hash(elem, self.size)
        idx = hashed_idx
        i = 1
        while self.T[idx] != elem:
            # print(idx)
            if self.T[idx] is None:
                return False
            idx = (hashed_idx + self.skip(i, elem)) % self.size
            i += 1
        return elem


class OpenAddressQuadratic(OpenAddressLinear):
    def __init__(self, size):
        super().__init__(size)

    def skip(self, i, elem):
        return math.floor(0.5 * i + 0.5 * i**2)


class OpenAddressDouble(OpenAddressLinear):
    def __init__(self, size):
        super().__init__(size)

    def skip(self, i, elem):
        return i * (1 + (elem % (self.size - 1)))


class HashTable:

    hash_tables_map = {
        1: ChainedDivisionHash(1),
        2: ChainedMultiplicationHash(1),
        3: OpenAddressLinear(1),
        4: OpenAddressQuadratic(1),
        5: OpenAddressDouble(1)

    }

    def __init__(self, hash_type, values):
        self.hashTable = HashTable.hash_tables_map[hash_type].\
            __class__(len(values))
        self.values = values
        for x in values:
            self.hashTable.add(x)

    def get_collisions_amount(self):
        return self.hashTable.collisions

    def find_sum(self, S):
        for x in self.values:
            if self.hashTable.find(S - x) != False:
                return x, S - x
        return None


# if __name__ == '__main__':
#     table = HashTable(3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 51])
#     print(table.get_collisions_amount())
#     print(table.find_sum(50))
#     print(table.hashTable.find(51))
#     print(table.hashTable.T)
