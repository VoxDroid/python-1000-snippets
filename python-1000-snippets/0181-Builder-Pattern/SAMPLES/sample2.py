# sample2.py
# SQL query builder with fluent interface

class QueryBuilder:
    def __init__(self):
        self._select = '*'
        self._table = ''
        self._where = ''
    def select(self, columns):
        self._select = columns
        return self
    def from_table(self, table):
        self._table = table
        return self
    def where(self, clause):
        self._where = clause
        return self
    def build(self):
        q = f"SELECT {self._select} FROM {self._table}"
        if self._where:
            q += f" WHERE {self._where}"
        return q

if __name__ == '__main__':
    q = QueryBuilder().select('id,name').from_table('users').where('id=1').build()
    print(q)    
