import re

# re.match()
string = "apythonhellomypythonhispythonourpythonend"
pattern = ".python"
res1 = re.match(pattern, string)
res2 = re.match(pattern, string).span()
print(res1)
print(res2)

# re.search()

# re.compile()
pat = re.compile(".python.")
res = pat.findall(string)
print(res)

# re.sub()
res1 = re.sub(pattern, "php", string)
res2 = re.sub(pattern, "php", string, 2)
print(res1)
print(res2)