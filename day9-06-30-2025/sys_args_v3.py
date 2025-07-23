import sys
# import argparse
# import click

if len(sys.argv) != 2:
    print("Usage: python sys_args_v3.py <filename.txt>")
else:
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        print(f.read())
    print("File processed successfully!")

print("-" * 50)
filename = input("Enter your file name: ")
with open(filename, 'r') as f:
    print(f.read())
    print("File processed successfully!")
