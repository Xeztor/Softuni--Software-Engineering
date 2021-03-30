from copy import deepcopy

class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        '''
        Reversed copy of the dictionary,
        so that we can use popitem() for iterator.
        '''
        self._dict = deepcopy(dictionary)
        self.dict_iterator = dict([self._dict.popitem() for _ in range(len(self._dict))])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.dict_iterator:
            raise StopIteration

        return self.dict_iterator.popitem()


# mydict = {1:'one', 2:'two', 3:'three'}
#
# di = dictionary_iter(mydict)
# print(di.dict_iterator)

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

