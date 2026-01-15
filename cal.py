import sys

if len(sys.argv)>0:
    script_name=sys.argv[0]
    num1=sys.argv[1]
    num2=sys.argv[2]
else:
    script_name=sys.argv[0]
    num1=162
    num2=153

print("calculator")
print(f"addition:{num1+num2}\nsubtraction:{num1-num2}\nmultiplication:{num1*num2}\ndivision:{num1/num2}")