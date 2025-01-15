import module1 as m1

import platform

m1.greet()
m1.greet("")
m1.greet("Charlie")

print("You are working on ", platform.system())
print(dir(platform))