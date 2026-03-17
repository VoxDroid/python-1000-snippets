# sample3.py
# Template method with customized steps and shared logic

class ReportGenerator:
    def generate(self):
        self.header()
        self.body()
        self.footer()

    def header(self):
        print("=== Report ===")

    def body(self):
        raise NotImplementedError

    def footer(self):
        print("=== End ===")


class SalesReport(ReportGenerator):
    def body(self):
        print("Sales data goes here")


def main():
    report = SalesReport()
    report.generate()


if __name__ == "__main__":
    main()
