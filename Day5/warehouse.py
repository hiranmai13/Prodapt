p=["Laptop","Mouse","Keyboard"]
print(p)

p.append("Monitor")
print(p)
new_p=["Tablet","Webcam"]
p.extend(new_p)

p.remove("Mouse")
print(p)

print("Shipped",p.pop())
print(p)

print(p.count("Laptop"))
print(p.index("Monitor"))

p.sort()
print(p)

p.reverse()
print(p)

back=p.copy()
print(back)
p.clear()
print(p)
