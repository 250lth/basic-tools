import queue

a = queue.Queue()
a.put("Hello")
a.task_done()
print(a.get())

a.put("Python")
a.task_done()
a.put("php")
a.task_done()
a.put("Java")
a.task_done()

print(a.get())
print(a.get())
print(a.get())
