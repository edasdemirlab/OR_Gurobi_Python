import gurobipy as gp

# list and tuples
l = [1, 2.0, 'abc'] 
t = (1, 2.0, 'abc') 
print(l[0]) 
print(t[1]) 
print(l[2])

# dictionaries
x = {} 
x['Pens', 'Denver', 'New York'] = 2 
x['Pens', 'Denver', 'New York']
values = {} 
values['zero'] = 0 
values['one'] = 1 
values['two'] = 2 

values

ders_kapasite = {} # boş bir dictionary tanımlar
ders_kapasite['EMU679'] = 11 #EMU679 anahtarına 11 atar.
ders_kapasite['EMU430'] = 73 #EMU430 anahtarına 11 atar.
ders_kapasite 

# Bu dictionary'i tek satırda da tanımlayabilirdik:
ders_kapasite = {'EMU679':11, 'EMU430':73}
ders_kapasite['EMU430']
ders_kapasite['EMU679']

# list comprehension ve Generator
[x*x for x in [1, 2, 3, 4, 5]] # [1, 4, 9, 16, 25]
sum(x*x for x in [1, 2, 3, 4, 5])

sum(x*x for x in range(1,6))
[(x,y) for x in range(4) for y in range(4) if x < y]
[(x,y) for x in range(4) for y in range(x+1, 4)]

# multidict
names, lower, upper = gp.multidict({ 'x': [0, 1], 'y': [1, 2], 'z': [0, 3]}) 
names
lower
upper

# tuplelist
l = gp.tuplelist([(1, 2), (1, 3), (2, 3), (2, 4)])
l.select(1, '*')
l.select('*', 3)
l.select('*', [2, 4])
l.select(1, 3)
l.select('*', '*')

# Tupledict
model = gp.Model("ornek") # creates gurobi model
l = list([(1, 2), (1, 3), (2, 3), (2, 4)]) # creates list l, each element is a tuple
d = model.addVars(l, name="d") # add list elements as variables 
# this will create variables d(1,2), d(1,3), d(2,3), and d(2,4)

model.update() # we need to update model before calling its elements
d.select(1, '*') # d(1,2),d(1,3)
d.sum(1, '*') # d(1,2) + d(1,3)
d.sum('*', 3) # d(1,3) + d(2,3)



