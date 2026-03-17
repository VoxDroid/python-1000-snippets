# sample2.py
# Template method with optional hooks for pre/post actions

class Task:
    def run(self):
        self.setup()
        self.execute()
        self.teardown()

    def setup(self):
        pass

    def execute(self):
        raise NotImplementedError

    def teardown(self):
        pass


class PrintTask(Task):
    def setup(self):
        print("starting")

    def execute(self):
        print("working")

    def teardown(self):
        print("done")


def main():
    task = PrintTask()
    task.run()


if __name__ == "__main__":
    main()
