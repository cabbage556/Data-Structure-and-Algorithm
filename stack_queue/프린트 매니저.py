from 큐 import MyQueue
from collections import deque


class PrintManager:
    def __init__(self):
        # self.queue = MyQueue()  # 리스트 기반 큐
        self.queue = deque()  # 이중 연결 리스트 기반 큐

    def queue_print_job(self, document):
        # self.queue.enqueue(document)
        self.queue.append(document)

    def run(self):
        # while not self.queue.is_empty():
        #     print(self.queue.dequeue())
        while self.queue:
            print(self.queue.popleft())  # O(1): 이중 연결 리스트 기반


printManager = PrintManager()
printManager.queue_print_job("First Document")
printManager.queue_print_job("Second Document")
printManager.queue_print_job("Third Document")
printManager.queue_print_job("Fourth Document")
printManager.run()
