# sample3.py
# report generator with hook methods

class Report:
    def generate(self):
        self.header()
        self.body()
        self.footer()
    def header(self):
        print('Report Header')
    def body(self):
        pass
    def footer(self):
        print('Report Footer')

class SalesReport(Report):
    def body(self):
        print('Sales data...')

if __name__ == '__main__':
    r = SalesReport()
    r.generate()
