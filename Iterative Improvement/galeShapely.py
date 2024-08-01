def galeShapely(sPref, aPref):
    n = len(sPref)
    freeSchol = list(range(n))
    sPart = [-1] * n 
    aPart = [-1] * n  
    next_proposal = [0] * n  
    while freeSchol:
        scholar = freeSchol.pop(0)
        advisor = sPref[scholar][next_proposal[scholar]]
        next_proposal[scholar] += 1
        if aPart[advisor] == -1:
            aPart[advisor] = scholar
            sPart[scholar] = advisor
        else:
            current_partner = aPart[advisor]
            if aPref[advisor].index(scholar) < aPref[advisor].index(current_partner):
                aPart[advisor] = scholar
                sPart[scholar] = advisor
                freeSchol.append(current_partner)
                sPart[current_partner] = -1
            else:
                freeSchol.append(scholar)
    return sPart

sP = [
    [1, 0, 2],
    [0, 1, 2],
    [0, 1, 2]
]
aP = [
    [1, 0, 2],
    [0, 2, 1],
    [2, 1, 0]
]
expMatch = [1, 0, 2]
result = galeShapely(sP, aP)
print(f"\nTest Case Result: {result}")
matching = galeShapely(sP, aP)
print("\nScholar to Advisor matching:")
for scholar, advisor in enumerate(matching):
    print(f"Scholar {scholar} -> Advisor {advisor}")
assert result == expMatch


