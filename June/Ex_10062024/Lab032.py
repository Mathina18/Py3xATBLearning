# Ternary Operator
anis_marks = 90
mathina_marks = 97

#   x > y -> do something - print("Anis")
# y > x -> do something else -> print("Mathina")
print("Anis is winner" if anis_marks > mathina_marks else "Mathina is winner")


if anis_marks > mathina_marks:
    print("Anis is the winner")
else:
    print("Mathina is the winner")