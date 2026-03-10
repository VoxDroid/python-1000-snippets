# sample2.py
import json
class Point:
    def __init__(self,x,y): self.x=x; self.y=y
p = Point(1,2)
print(json.dumps(p, default=lambda o: o.__dict__))

