from itertools import product

def read_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Valoarea nu poate fi negativă. Încearcă din nou.")
            else:
                return value
        except ValueError:
            print("Input invalid. Te rog introdu un număr.")


def read_umg_list(prompt):
    while True:
        text = input(prompt).strip()
        try:
            values = list(map(float, text.split()))
            if not values:
                print("Trebuie să introduci cel puțin o utilitate marginală.")
            elif any(v < 0 for v in values):
                print("UMg-urile nu pot fi negative.")
            else:
                return values
        except ValueError:
            print("Lista trebuie să conțină doar numere separate prin spații.")


def optimal_choice(budget, groups):
    ranges = [range(len(g["umg"]) + 1) for g in groups]

    best_utility = -1
    best_combo = None

    for combo in product(*ranges):
        cost = sum(combo[i] * groups[i]["price"] for i in range(len(groups)))
        if cost <= budget:
            utility = sum(sum(groups[i]["umg"][:combo[i]]) for i in range(len(groups)))
            if utility > best_utility:
                best_utility = utility
                best_combo = combo

    result = {groups[i]["name"]: best_combo[i] for i in range(len(groups))}
    return result, best_utility


print("=== Program optimizare utilitate ===")

budget = read_float("Introduceți bugetul total: ")

groups = []
index = 1

while True:
    print(f"\n--- Grupa {index} ---")
    name = input("Introduceți numele grupei (ENTER pentru a termina): ").strip()

    if name == "":
        break

    price = read_float(f"Prețul unei doze pentru grupa {name}: ")

    umg_list = read_umg_list(
        f"Introduceți utilitățile marginale pentru grupa {name} separate prin spațiu (ex. 5 4 3 2 1 etc): "
    )

    groups.append({
        "name": name,
        "price": price,
        "umg": umg_list
    })

    index += 1


if not groups:
    print("\nNu a fost introdusă nicio grupă. Program încheiat.")
else:
    best_combo, max_utility = optimal_choice(budget, groups)

    print("\n===== REZULTAT OPTIM =====")
    print(f"Buget: {budget}\n")

    print("Cantitățile optime:")
    for name, qty in best_combo.items():
        print(f"  {name}: {qty} doze")

    print(f"\nUtilitatea totală maximă: {max_utility}")
    print("==========================")

input("\nApasă ENTER pentru a ieși...")