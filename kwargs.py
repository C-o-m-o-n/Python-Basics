## Key Word Args (KWArgs)

## Rewriting the sum() function
def addAll(*args):
    total = 0
    # sum(args)
    for arg in args: total += arg
    return total

## Add All Numbers
print("\nAdd all")
print(addAll(1,2,3,4,5,6))

## Create Dictionary
createDictionary(o=1,t=2,f=4)
def createDictionary(**kwargs):
    return kwargs
    #return {**happy}

print("\nCreate Dictionary")
print(createDictionary(
    neva='happy',
    taylor='edon',
    Something=3222,
    Tovra="Messor", Just='playing',
    bil='oak',
    rosmy='kuruvilla',
))

def f(*args, **kwargs):
    print(args)
    print(kwargs)

#f(1,2,3,key='value',foo='bar')
