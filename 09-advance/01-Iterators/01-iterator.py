my_tuple = ("apple", "banana", "cherry")
my_it = iter(my_tuple)

print(next(my_it))
print(next(my_it))
print(next(my_it))

# looping through an iterator
for a in my_tuple:
    print('the output from loop ', a)

my_str = 'Banana'
my_it_str = iter(my_str)
print(next(my_it_str))
print(next(my_it_str))
print(next(my_it_str))
print(next(my_it_str))
print(next(my_it_str))
print(next(my_it_str))

for b in my_str:
    print('the output from loop', b)


class MyNumbers:
    def __iter__(self):
        self.c = 1
        return self

    def __next__(self):
        d = self.c
        self.c += 3
        return d


MyClass = MyNumbers()
my_it_cls = iter(MyClass)


print('from class & method ', next(my_it_cls))
print('from class & method ', next(my_it_cls))
print('from class & method ', next(my_it_cls))
print('from class & method ', next(my_it_cls))
print('from class & method ', next(my_it_cls))
print('from class & method ', next(my_it_cls))
