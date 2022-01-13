import dill

with open("dilled_function.dill", "rb") as file:
    tested_dilled_function = dill.load(file)

print(tested_dilled_function("test"))

