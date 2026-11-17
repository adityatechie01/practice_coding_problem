Question:

You need to write a Python program that performs the following steps:

1. Take input numbers separated by commas (e.g. 1,2,3,4,5,6).
2. Split the string into a list of strings.
3. Convert the list of strings into a list of integers.
4. Print the original string list, the integer list, and the product of the first and last elements.

Input Format:
A single line containing integers separated by commas (,).

Output Format:
Print the following, each on a new line:
- The original list of string values.
- The list after converting all elements to integers.
- The product of the first and last integers in the list.

Code:

a = input()

b = a.split(",")
print(b)

c = list(map(int, b))
print(c)

print(c[0] * c[-1])
