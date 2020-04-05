from contextlib import contextmanager

class Job(object):
    def __init__(self, name):
        self.name = name
        self.target_url = "<none>"
        self.selector = "<none>"
        self.save_file = "<none>"
    
    def load(self, url):
        self.url = url

        return self
    
    def find(self, selector):
        self.selector = selector

        return self
    
    def save(self, save_file):
        self.save_file = save_file

        return self
    
    def complete(self):
        print(f"[START {self.name}]")
        print(f"TARGET_URL = {self.target_url}")
        print(f"SELECTOR = {self.selector}")
        print(f"SAVE_FILE = {self.save_file}")
        print(f"[END {self.name}]")

def main():
    job = Job("Job 1")
    job.load("<url>").find("<selector>").save("filename").complete()

    job2 = Job("Job 2")
    job2.load("<url>").find("<selector>").complete()

    job3 = Job("Job 3")
    job3.load("<url>").complete()


if __name__ == "__main__":
    main()