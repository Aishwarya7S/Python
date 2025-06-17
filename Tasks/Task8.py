# Set
set1 = {1,2,3,5}
set2 = {7,3,9,10}
print("Intersection:" , set1.intersection(set2))
print("Union:", set1.union(set2))
print("Difference:", set1.difference(set2))
print("Symmetric difference:", set1.symmetric_difference(set2))

seta = {'sam', 'sd', 'ani', 'rishi'}
seta.discard('rishi')
setb = {'jas', 'silver', 'meow'}
seta.update(setb)
seta.remove('meow')
print(seta)

