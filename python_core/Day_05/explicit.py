# Explicit Type Conversion: Programmer manually converts data types using functions

# 1. String → Int
x = "20"
int(x)        # 20, type: int

# 2. String → Float
y = "15.5"
float(y)      # 15.5, type: float

# 3. Int → String
a = 100
str(a)        # '100', type: str

# 4. Float → Int
b = 12.9
int(b)        # 12, type: int (decimal lost)

# 5. Tuple → List
t = (1, 2, 3)
list(t)       # [1, 2, 3], type: list

# 6. Int → Boolean
c = 0
bool(c)       # False, type: bool
d = 5
bool(d)       # True, type: bool
