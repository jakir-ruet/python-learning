def pig_latin(text):
  say = []
  my_word = text.split()
  for i in my_word:
    i = i[1:] + i[0] + "ay"
    say.append(i)
  return " ".join(say)
print(pig_latin("python"))
print(pig_latin("django"))