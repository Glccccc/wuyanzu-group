def orth_triangle(*, cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0) -> float | None:
    
    """Возвращает длину третьей стороны прямоугольного треугольника по двум переданным сторонам или None, если вычисление невозможно"""
    
    if cathetus1 and cathetus2 and hypotenuse:
        return None
        
    if cathetus1 and cathetus2:
        return round(((cathetus1 ** 2 + cathetus2 ** 2) ** 0.5), 2)
        
    if cathetus1 and hypotenuse and cathetus1 < hypotenuse:
        return round(((hypotenuse ** 2 - cathetus1 ** 2) ** 0.5), 2)
        
    if cathetus2 and hypotenuse and cathetus2 < hypotenuse:
        return round(((hypotenuse ** 2 - cathetus2 ** 2) ** 0.5), 2)
        
        
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> orth_triangle(cathetus1=18, cathetus2=23)
# 29.21
# >>> print(orth_triangle(cathetus1=18, cathetus2=23, hypotenuse=29.21))
# None
# >>> orth_triangle(cathetus1=18, hypotenuse=29.21)
# 23.0
# >>> orth_triangle(cathetus2=18, hypotenuse=29.21)
# 23.0
# >>> print(orth_triangle(cathetus1=18, hypotenuse=9.21))
# None
# >>> print(orth_triangle(cathetus2=18, hypotenuse=9.21))
# None