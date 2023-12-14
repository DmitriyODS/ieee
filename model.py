def multiplication(num1: str, num2: str) -> str:
    res = []

    if len(num1) > len(num2):
        num2, num1 = num1[::-1], num2[::-1]
    else:
        num1, num2 = num1[::-1], num2[::-1]

    buffer = 0
    for i in range(len(num2)):
        for j in range(len(num1)):
            if len(res) <= i + j:
                res.append(0)

            tmp = int(num1[j]) * int(num2[i])
            tmp += buffer + res[i + j]
            buffer = tmp // 10
            tmp %= 10
            res[i + j] = tmp

        while buffer > 0:
            res.append(buffer % 10)
            buffer //= 10

    return ''.join(map(str, res[::-1]))


class IEEEModel:
    def __init__(self, model=None):
        self.symbol = 0
        self.order = 0
        self.exp = 0

        if model is not None:
            self.symbol = model.symbol
            self.order = model.order
            self.exp = model.exp

    def calc(self):
        self.exp *= 2
        res = multiplication(str(self.order), str(self.order))
        fact_len = len(str(self.order)) * 2 - len(res)
        self.exp -= fact_len
        
        self.order = int(res)

    def clear(self):
        self.symbol = 0
        self.order = 0
        self.exp = 0

    def is_empty(self):
        return not (self.symbol or self.order or self.exp)

    def load_number(self, one: str, two: str, symbol: str):
        self.clear()

        if symbol == '-':
            self.symbol = 1

        two = two.rstrip('0')

        tmp_num = int(one)
        while tmp_num != 0:
            tmp_num //= 10
            self.exp += 1

        if int(one) == 0:
            for i in range(len(two)):
                if two[i] == '0':
                    self.exp -= 1
                else:
                    two = two[i:]
                    break

        self.order = int(one + two)

    def get_data(self):
        return str(self.symbol), str(self.exp), str(self.order)
