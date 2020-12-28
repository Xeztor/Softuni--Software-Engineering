var_type = input()
data = input()

if var_type == "int":
    def mutate_data(var):
        return int(var) * 2

    print(mutate_data(data))
elif var_type == "real":
    def mutate_data(var):
        return f"{float(var) * 1.5:.2f}"

    print(mutate_data(data))
elif var_type == "string":
    def mutate_data(var):
        return f"${var}$"

    print(mutate_data(data))
