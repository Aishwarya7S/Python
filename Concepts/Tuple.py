veg1 = ("carrot", "cauliflower", "tomato", "onion")

veg1 = veg1 + ("cabbage",)
print("After adding an item:", veg1)

veg2 = ("radish", "potato")
veg1 = veg1 + veg2
print("After concatenation:", veg1)

index_of_cauliflower = veg1.index("cauliflower")
print("Index of 'cauliflower':", index_of_cauliflower)

veg1 = veg1 + ("tomato",)
tomato_count = veg1.count("tomato")
print("Count of 'tomato':", tomato_count)

print("the legth: ", len(veg1))

nums = (1,2,3,4,5)
print("The sum is :", sum(nums))
print("The max num is :" , max(nums))
print("The min num is :" , min(nums))
