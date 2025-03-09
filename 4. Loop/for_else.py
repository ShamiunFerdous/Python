# For loop can have an optional else block as well.
# It executes only if the loop is not terminated by a break statement.
# If the loop finishes normally → The else block runs.
# If the loop is interrupted by break → The else block is skipped.

# Example 1: else block is executed
for i in range(1,4):
    print(i)

else:
    print("Loop finished normally")

# Output:
# 1
# 2
# 3
# Loop finished normally
    


# Example 2: else block is skipped
for i in range(1, 4):
    print(i)
    if i == 2:
        break
else:
    print("Loop finished normally")

# Output:
# 1
# 2
