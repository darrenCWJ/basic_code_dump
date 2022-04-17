"""
Set practice

sets are no key word dictionary
"""

Set1 = {1,3,5,7,9}
Set2 = {2,4,6,8,10}
Set3 = {1,2,3,7,8,9}

u = Set1.union(Set2)
u # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

i = Set1.intersection(Set3)
i # {1, 3, 7, 9}

diff = Set1.difference(Set3)
diff # {5}

sdiff = Set1.symmetric_difference(Set3)
sdiff #{2, 5, 8}

Set1.update(Set2)
Set1 # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Set1 = {1,3,5,7,9}
Set1.intersection_update(Set3)
Set1 # {1, 3, 7, 9} because 5 is intersected with in set3

Set1 = {1,3,5,7,9}
Set1.difference_update(Set3)
Set1 #{5}

Set1 = {1,3,5,7,9}
Set1.symmetric_difference_update(Set3)
Set1 #  {2, 5, 8}

Set1 = {1,2,3,4,5,6,7,8,9}
Set2 = {4,5,6,7}
Set1.issubset(Set2) #False
Set1.issuperset(Set2) #True

Set3 = {10,11,12}
Set4 = {9,10,11}
Set3.isdisjoint(Set1) #True
Set4.isdisjoint(Set1) #False, 9 is in Set1


Set1.add(10)
Set1 #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}




