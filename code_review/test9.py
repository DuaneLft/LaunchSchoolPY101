
def twice(n):
  a = str(n)
  return n if len(a) % 2 == 0 and a[:len(a)//2] == a[len(a)//2:] else n*2
    
# These examples should all print True
print(twice(37) == 74)
print(twice(44) == 44)
print(twice(334433) == 668866)
print(twice(444) == 888)
print(twice(107) == 214)
print(twice(103103) == 103103)
print(twice(3333) == 3333)
print(twice(7676) == 7676)

