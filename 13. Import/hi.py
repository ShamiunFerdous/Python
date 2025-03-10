''' Importing in Python allows you to use 
code from other modules (Python files) without rewriting it.'''

import math
import my_module as mm

print(math.sqrt(16))  # Output: 4.0
mm.greet()
print(f"My name is {mm.name}")

