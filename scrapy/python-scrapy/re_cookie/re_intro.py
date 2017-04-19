import re

# 1.Atom

# normal char
pattern1 = "yue"
string1 = "http://yum.iqianyue.com"
res1 = re.search(pattern1, string1)
print(res1)

# no-print char
pattern2 = "\n"
string2 = '''http://yum.iqianyue.com
            http://www.baidu.com'''
res2 = re.search(pattern2, string2)
print(res2)
string3 = '''http://yum.iqianyue.comhttp://www.baidu.com'''
res3 = re.search(pattern2, string3)
print(res3)

# common char
pattern4 = "\w\dpython\w"
string4 = "abcdedghiphp345python_py"
res4 = re.search(pattern4, string4)
print(res4)

# atom sheet
pattern11 = "\w\dpython[xyz]\w"
pattern21 = "\w\dpython[^xyz]\w"
pattern31 = "\w\dpython[xyz]\W"
string = "abcdfphp345python_py"
res11 = re.search(pattern11, string)
res21 = re.search(pattern21, string)
res31 = re.search(pattern31, string)
print(res11)
print(res21)
print(res31)


# 2.Meta char
pattern = ".python..."
res1 = re.search(pattern, string)
print(res1)

pattern1 = "^abd"
pattern2 = "^abc"
pattern3 = "py$"
pattern4 = "ay$"
res1 = re.search(pattern1, string)
res2 = re.search(pattern2, string)
res3 = re.search(pattern3, string)
res4 = re.search(pattern4, string)

pat1 = "py.*n"
pat2 = "cd{2}"
pat3 = "cd{3}"
pat4 = "cd{2,}"
res1 = re.search(pat1, string)
res2 = re.search(pat2, string)
res3 = re.search(pat3, string)
res4 = re.search(pat4, string)
print(res1)
print(res2)
print(res3)
print(res4)

pattern = "python|php"
res = re.search(pattern, string)
print(res)

pattern1 = "(cd){1,}"
pattern2 = "cd{1,}"
res1 = re.search(pattern1, string)
res2 = re.search(pattern2, string)
print(res1)
print(res2)


# 3.Pattern modify
pattern1 = "Python"
pattern2 = "Python"
res1 = re.search(pattern1, string)
res2 = re.search(pattern2, string, re.I)
print(res1)
print(res2)


# 4.Hunger and lazy
pattern1 = "p.*y"
pattern2 = "p.*?y"
res1 = re.search(pattern1, string)
res2 = re.search(pattern2, string)
print(res1)
print(res2)