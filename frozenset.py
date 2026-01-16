# Normal set (mutable)
s = set(["a", "b", "c"])
print("Normal Set is Mutable:", s)
s.add("d")
print("Normal Set:", s)

# Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen Set is Immutable:", fs)
s.add("h")
print("Frozen Set:", fs)

