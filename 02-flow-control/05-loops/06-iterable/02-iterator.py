class MyIterator:
    # Constructor
    def __init__(self, limit):
        self.Limit = limit

    # Creates iterator object, Called when iteration is initialized
    def __iter__(self):
        self.a = 10
        return self

    # we should replace next with __next__
    def __next__(self):
        # Store current value ofx
        a = self.a

        # Stop iteration if limit is reached
        if a > self.Limit:
            raise StopIteration

        # Else increment and return old value
        self.a = a + 1
        return a


# Prints numbers from 10 to 20
for i in MyIterator(20):
    print(i)

# # Prints nothing
# for i in MyIterator(10):
#     print(i)
