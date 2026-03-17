# sample3.py
# Factory method used as an alternative constructor for a class

class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    def from_url(cls, url):
        scheme, rest = url.split("://", 1)
        host, port = rest.split(":")
        return cls(host, int(port))

    def __str__(self):
        return f"Connection({self.host}:{self.port})"


def main():
    conn = Connection.from_url("http://localhost:8080")
    print(conn)


if __name__ == "__main__":
    main()
