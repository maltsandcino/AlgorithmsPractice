###Implement hash function
# def get_hash(key):
#     h = 0
#     for  char in key:
#         h += ord(char)
#     return h % 1000

# print(get_hash("This is my new value"))

##Create hashtable class
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

 ##Hash function   
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

###Setting and getting values, with these methods you can use the hashtable similarly to a dictionary
###I.E. you can index in via the key    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        
        found = False
        ###Key already exists. iterate through elements in that bucket. each element is an entry
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,val)
                found=True
                break
        ###no key xists
        if not found:
            self.arr[h].append((key, val))
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        # return print(self.arr[h])

##Delete method    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                del self.arr[h][index]

t = HashTable()

###These two keys have the same hash value, causing collision without proper handling
print(t.get_hash('march 15'))
print(t.get_hash('march 06'))


t['march 15'] = 130
t['march 06'] = 120
print(t['march 06'])
t['march 06'] = 160
t['march 16'] = 12
print(t['march 15'])
print(t['march 16'])
print(t['march 06'])
print(t.arr)
del t['march 06']
print(t.arr)
