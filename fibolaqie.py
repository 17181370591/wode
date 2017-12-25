class Fib():
    def __init__(s):
        s.a=0
        s.b=1
    def __next__(s):
        s.a,s.b=s.b,s.b+s.a
        return s.a
    def __iter__(s):
        return s
