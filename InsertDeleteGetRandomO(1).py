

class RandomizedSet:

    def __init__(self):
        self.arr=[]
        self.dic={}

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.arr.append(val)
            self.dic[val]=len(self.arr)-1
            return True
        else:
            return False
        # print(self.arr,val)

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        else:
            indx=self.dic[val]
            self.arr[:]=self.arr[:indx]+self.arr[indx+1:]
            for i in self.dic:
                if self.dic[i]>indx:
                    self.dic[i]-=1
            # print(self.arr)
            del self.dic[val]
            return True

    def getRandom(self) -> int:
        n=len(self.arr)
        tmp=int(random.random()*n)
        return self.arr[tmp]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
