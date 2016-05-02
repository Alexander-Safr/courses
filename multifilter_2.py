class multifilter:
    
    def judge_half(pos, neg):
        return pos >= neg
    
    def judge_any(pos, neg):
        return pos > 0

    def judge_all(pos, neg):
        return neg == 0
        
    def count_res(self, a):
        res = [f(a) for f in self.funcs]
        return res.count(True), res.count(False)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable  # iterable - исходная последовательность
        self.funcs = funcs        # funcs - допускающие функции
        self.judge = judge        # judge - решающая функция
       
    def __iter__(self):
        for i in self.iterable:
            pos, neg = self.count_res(i)
            if self.judge(pos, neg):
                yield i
