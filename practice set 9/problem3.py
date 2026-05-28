
def generate_table(n):
    table=""
    with open(f"tables/table_{n}.txt", "w") as f:
        for i in range(1,11):
            table+=f"{n} * {i} = {n*i}\n"
            f.write(table)

for i in range(2,21):
    generate_table(i)