# Implicit Type Conversion: Python automatically converts data types when needed

# 1. Int + Float
a = 10        # int
b = 2.5       # float
a + b         # 12.5, type: float

# 2. Int + Complex
x = 5         # int
y = 3 + 2j    # complex
x + y         # (8+2j), type: complex

# 3. Float + Complex
p = 4.5       # float
q = 2 + 3j    # complex
p + q         # (6.5+3j), type: complex

# 4. Boolean + Int
flag = True
flag + 5      # 6, type: int

# Note: Strings are NOT implicitly converted
s = "10"
# s + 5      # Error