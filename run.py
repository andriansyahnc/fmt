from fmt import Repository as RManager

a = RManager()
a.Register("name", "M Andriansyah Nurcahya", 1)
a.Register("name", "NC", 1)
a.Register("gender", "Male", 1)
a.Register("status", "Married", 1)

print(a.Retrieve("name"))
print(a.Retrieve("gender"))
print(a.GetType("name"))
print(a.Deregister("status"))
print(a.GetType("status"))