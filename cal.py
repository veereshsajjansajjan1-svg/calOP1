import sys

if len(sys.argv) > 2:
    script_name = sys.argv[0]
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
else:
    script_name = sys.argv[0]
    num1 = 162
    num2 = 153

print("calculator")

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print(f"addition: {sum}")
print(f"subtraction: {sub}")
print(f"multiplication: {mul}")
print(f"division: {div}")
