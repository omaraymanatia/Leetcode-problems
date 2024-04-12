import random
class RandomizedSet:
    def __init__(self):
        self.se=set()

    def insert(self, val: int) -> bool:
        if val in self.se:
            return 0
        else:
            self.se.add(val)
            return 1

    def remove(self, val: int) -> bool:
        if val not in self.se:
            return 0
        else:
            self.se.remove(val)
            return 1

    def getRandom(self) -> int:
        random_element = random.choice(list(self.se))
        return random_element


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()