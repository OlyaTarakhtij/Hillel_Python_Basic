class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

        # переконєумось, чи входить в допустимі межі
        if self.current < self.min_value:
            self.current = self.min_value
        if self.current > self.max_value:
            self.current = self.max_value

    def set_current(self, start):
        # встанолюємо поточне значення, але фіксує в межах min/max
        if start < self.min_value:
            self.current = self.min_value
        elif start > self.max_value:
            self.current = self.max_value
        else:
            self.current = start

    def set_max(self, max_max):
        # встановлюємо новий максимум; якщо поточний > ніж новий максимум — "завузити" current
        self.max_value = max_max
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, min_min):
        # встанолюємо новий мінімум; якщо поточний < новий мінімум — підняти current
        self.min_value = min_min
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self):
        # збільшуємо на 1; при досягненні (або пребільшені) max — виключення
        if self.current >= self.max_value:
            raise ValueError("Досягнутий максимум")
        self.current += 1

    def step_down(self):
        # зменшуємо на 1; при досягненні (або нижче) min — виключення
        if self.current <= self.min_value:
            raise ValueError("Досягнутий мінімум")
        self.current -= 1

    def get_current(self):
        return self.current
