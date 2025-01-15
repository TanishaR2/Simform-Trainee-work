prog_lang = ["C", "C++", "Python", "Java"]
x = prog_lang[0]
y = prog_lang[2]
print(prog_lang)
print(f"{x} is oldestlanguage while {y} is advanced and quite easier!")


prog_lang[1] = 'R'
print(prog_lang)


prog_lang.append('C++')
print(prog_lang)


prog_lang.append('cobol')
print(prog_lang)


prog_lang.pop(-1)
print(prog_lang)


prog_lang.remove('C++')
print(prog_lang)

prog_lang.sort()
print("Sorted array: ", prog_lang)
