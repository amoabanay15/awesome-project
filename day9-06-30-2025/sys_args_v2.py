import sys


def addition(num1, num2):
    """function to add two numbers"""
    return num1 + num2


if len(sys.argv) != 4:
    print("Usage: python sys_args_v2.py num1 num2")
    print("Usage: python sys_args_v2.py 99 34")
    print("Usage: python sys_args_v2.py 99 34 AAPL")
else:
    print(sys.argv)
    apple_stock = int(sys.argv[1])
    tesla_stock = int(sys.argv[2])
    stock_name = sys.argv[3]
    #  total = apple_stock + tesla_stock
    total = addition(apple_stock, tesla_stock)
    # total = addition(num1=apple_stock, num2=tesla_stock)

    print(f"Sum is: {total}")
    print(f"Stock name is: {stock_name}")
