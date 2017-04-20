import threading


class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print("It's thread A")


class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print("It's thread B")


if __name__ == "__main__":
    t1 = A()
    t1.start()
    t2 = B()
    t2.start()