# in string using '', "", '''(multiline)''' """(multiline)"""
# it is case sensetive
# indexing is applicable in the string
# it is immutable, we can add/remove a character but not change.
a = "I am Jakir"
print(a)
print(len(a))
print(a[3])
print(a[-3])
print(a[2:6])
print(a[:6])  # slicing from start
print(a[4:])  # slicing from end

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)
# text check (case sensetive)
print("lorem" in b)
print("Lorem" in b)

c = "Banana"
for s in c:
    print(s)
