A = True
B = True
C = True
z = not(not(A) and B) or C
print("______________")
print("|A|B|C|      |")
print("|V|V|V|", z, "|")
A = False
B = True
C = True
z = not(not(A) and B) or C
print("|F|V|V|", z, "|")
A = True
B = False
C = True
z = not(not(A) and B) or C
print("|V|F|V|", z, "|")
A = True
B = True
C = False
z = not(not(A) and B) or C
print("|V|V|F|", z, "|")
A = False
B = False
C = True
z = not(not(A) and B) or C
print("|F|F|V|", z, "|")
A = False
B = True
C = False
z = not(not(A) and B) or C
print("|F|V|F|", z, "|")
A = True
B = False
C = False
z = not(not(A) and B) or C
print("|V|F|F|", z, "|")
A = False
B = False
C = False
z = not(not(A) and B) or C
print("|F|F|F|", z, "|")
print("______________")
