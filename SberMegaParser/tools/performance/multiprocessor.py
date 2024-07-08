from multiprocessing import Process, Queue


class Multiprocessor:

    def __init__(self):
        self.queue = Queue()
        self.processes = []

    @staticmethod
    def _call_wrapper(func, queue, parser, urls):
        ret = func(parser, urls)
        queue.put(ret)

    def run(self, func, parser, urls):
        args_all = [func, self.queue, parser, urls]
        process = Process(target=self._call_wrapper, args=args_all)
        self.processes.append(process)
        process.start()

    def wait(self):
        results = []
        for process in self.processes:
            ret = self.queue.get()
            results.append(ret)
        for process in self.processes:
            process.join()
        return results

