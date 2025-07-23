import sys

print(f"All arguments passed: {sys.argv}")
print(sys.argv[0])
print(sys.argv[1])

print("-" * 50)

# usage: python sys_args.py ghana togo usa banana
args = ['sys_args.py', 'Ghana', 'Togo',
        'banana', 'USA', 'Daniel', '99', 'Dallas']

print(args[0])
print(args[7])

print("-" * 50)


def addition(number1, number2):
    return number1 + number2


print(addition(59, 30))


print(len(sys.argv))
