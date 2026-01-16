#from dataclasses import dataclass

## Magic Methods / Dunder Methods / Double Underscore
## Quad Underscore Methods
#@dataclass
class QQ():
    def __init__(self):
        self.name = "QuntumQuantified"
        self.matrix = [[1,2],[3,4]]

    def __matmul__(self, other):
        newQQ = QQ()
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
               print(col)
               newQQ.matrix[row][col] = \
                    self.matrix[row][col] * \
                    other.matrix[col][row]
        return newQQ

    def __getitem__(self, index=0):
        return self.matrix[index]

    def __len__(self):
        return 1000000

    def __post_init__(self):
        print('post inited')

    def __repr__(self):
        return f"QQ Name is: {self.name} {self.matrix}"

    def __add__(self, other):
        concatQQ = QQ()
        concatQQ.name = f"{self.name} {other.name}"
        return concatQQ
        

    #enumeration / yeild __iter__
    #@
    #def __@__(self, other):
    #    pass

    #def __enter__(self):
    #    print('__enter__')

    #def __exit__(self):
    #    print('__exit__')

    #def __del__(self):
    #    print('__del__')

    #def __new__(self):
    #   #print('__new__')
    #   #return self


myQQ = QQ()
myOtherQQ = QQ()

multedQQ = myQQ @ myQQ

print(multedQQ)
print(myQQ + myOtherQQ)
print(myQQ)
print(myQQ[1])


