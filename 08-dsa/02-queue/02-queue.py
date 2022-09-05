from typing import Union


class Queue:
  def __init__(self, k, *e) -> None:
    self.queue = [None] * k
    self.k = k
    self.front = -1
    self.rear = k
    self.len = 0

    for els in e:
      self.enqueue(els)

  # Add an element
  def enqueue(self, item) -> None:
    # print(self.len, self.k)
    if self.len <= self.k:
      self.queue.append(item)
      self.len += 1
      self.rear += 1
    else:
      print(f"Queue is full, maximum limit is {self.k}")

  # Remove an element
  def dequeue(self) -> Union[None, any]:
    if self.len < 1:
      return None
    else:
      self.rear -= 1
      self.len -= 1
      return self.queue.pop(0)

  # Display  the queue
  def display(self) -> None:
    print(self.queue)

  def size(self) -> int:
    return self.len

  def isFull(self) -> bool:
    pass


q = Queue(6, 1, 2, 3, 4, 5, 6, )

q.enqueue(8)
print(q.len)
