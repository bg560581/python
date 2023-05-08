def hello():
    print('hello Bennett!')
def pack(name, middle, last):
    return [name, middle, last]
def eat_lunch(list):
    if len(list)==0:
        print('My lunchbox is empty')
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"first i eat {list[0]}")
            else:
                print(f"next I eat {list[i]}")


hello()
print(pack('ben','will','gal'))
eat_lunch([])
eat_lunch(['sammy'])
eat_lunch(['x','y','z','zz','yy','xx'])
