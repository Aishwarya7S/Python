lang = {"c", "python", "java", "html", "css"}
lang.add("php")
print("After adding an item:", lang)

more_langs = {"sql", "ai"}
lang.update(more_langs)
print("After extending:", lang)

lang.discard("css")
print("After removing an item:", lang)

lang.remove("html")
print("After removing 'html':", lang)

removed_item = lang.pop()
print("After popping an item:", lang, "| Removed item:", removed_item)

python_exists = "python" in lang
print("Does 'python' exist in the set:", python_exists)

lang.clear()
print("After clearing the set:", lang)

copy_lang = {"java", "python", "sql"}
copy_set = copy_lang.copy()
print("Copied set:", copy_set)

a = {"java", "python"}
b = {"sql", "python", "c"}
print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference (a - b):", a.difference(b))
print("Symmetric difference:", a.symmetric_difference(b))
print("Is a subset of b:", a.issubset(b))
print("Is a superset of b:", a.issuperset(b))
print("Are a and b disjoint:", a.isdisjoint({"html", "css"}))
