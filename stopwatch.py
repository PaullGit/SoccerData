import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            print("Stopwatch started.")

    def stop(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            self.is_running = False
            print(f"Stopwatch stopped. Elapsed time: {elapsed_time:.2f} seconds.")
            return elapsed_time
        else:
            print("Stopwatch is not running.")

    def reset(self):
        self.start_time = None
        self.is_running = False
        print("Stopwatch reset.")

