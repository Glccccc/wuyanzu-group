class SIUnit:
    """Представление значений в удобочитаемом виде с корректировкой приставок СИ."""
    __prefixes = {0: '', 3: 'k', 6: 'M', 9: 'G', 12: 'T', 15: 'P', 18: 'E', 21: 'Z', 24: 'Y',
                  -3: 'm', -6: 'μ', -9: 'n', -12: 'p', -15: 'f', -18: 'a', -21: 'z', -24: 'y'}
    __exponents = {v: k for k, v in __prefixes.items()}
    
    def __init__(self, number, unit='', *, start_exp=0, digits=None):
        self.number = number
        self.__unit = unit
        self.__start_exp = start_exp
        # 遍历所有可能的SI前缀，找到合适的可读表示
        for k in range(-24, 25, 3):
            r_number = number / 10**k
            if 0 < r_number < 1000:
                self.readable = r_number if digits is None else round(r_number, digits)
                self.readable_unit = f"{self.__class__.__prefixes[k+start_exp]}{unit}"
                break
    
    def __str__(self):
        if self.__unit:
            return f"{self.readable} {self.readable_unit}"
        else:
            exp = self.__class__.__exponents[self.readable_unit]
            return f"{self.readable:.1f}\u00b710^{exp}"
    
    def target(self, target_exp):
        # 转换为目标指数的数值和单位
        t_number = self.number * 10**(target_exp+self.__start_exp)
        t_unit = f"{self.__class__.__prefixes[target_exp]}{self.__unit}"
        return f"{t_number} {t_unit}"


if __name__ == '__main__':
    # 示例：自动格式化不同数量级的数值
    v1 = SIUnit(123734345)
    print(v1)

    v2 = SIUnit(2364, 'eV', start_exp=3, digits=1)
    print(v2)

    v3 = SIUnit(0.00003215)
    print(v3)

    v4 = SIUnit(0.000000000358, 's')
    print(v4)

# 使用方法：
# 1. 创建SIUnit对象，例如：SIUnit(1500, 'm')
# 2. 打印对象即可获得带SI前缀的可读字符串
# 3. 可调用target方法转换为指定指数的单位
# 适用场景：科学计算、物理量展示、单位换算等。

