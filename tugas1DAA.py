class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def knapsack_backtracking(items, capacity):
    n = len(items)
    max_profit = 0
    best_combination = []
    def backtrack(index, current_weight, current_profit, selected_items):
        nonlocal max_profit, best_combination
        if current_weight > capacity:
            return
        if current_profit > max_profit:
            max_profit = current_profit
            best_combination = list(selected_items)
        if index == n:
            return
        if current_weight + items[index].weight <= capacity:
            selected_items.append(items[index].name)
            backtrack(index + 1, 
                      current_weight + items[index].weight, 
                      current_profit + items[index].value, 
                      selected_items)
            selected_items.pop() 
        backtrack(index + 1, current_weight, current_profit, selected_items)
    backtrack(0, 0, 0, [])
    
    return max_profit, best_combination

if __name__ == "__main__":
    data_items = [
        Item("Genset Portable", 15, 40),
        Item("Kotak Obat", 3, 15),
        Item("Makanan Kaleng", 8, 10),
        Item("Selimut Tebal", 5, 8),
        Item("Tenda Darurat", 10, 25),
        Item("Alat Komunikasi", 2, 30),
        Item("Baterai Cadangan", 4, 12),
        Item("Filter Air", 6, 20),
        Item("Pakaian Kering", 7, 8),
        Item("Peralatan Medis Berat", 12, 35)
    ]
    
    kapasitas_gudang = 60

    print("=== PENYELESAIAN 0/1 KNAPSACK DENGAN BACKTRACKING ===")
    print(f"Kapasitas Maksimum: {kapasitas_gudang} kg")
    print(f"Total Item: {len(data_items)}\n")
    
    print("Daftar Barang:")
    print(f"{'Nama Barang':<25} {'Berat (kg)':<12} {'Profit (Juta)':<15}")
    print("-" * 52)
    for item in data_items:
        print(f"{item.name:<25} {item.weight:<12} {item.value:<15}")
    print("-" * 52)

    max_val, chosen_items = knapsack_backtracking(data_items, kapasitas_gudang)

    print("\n=== HASIL AKHIR ===")
    print(f"Total Profit Maksimum : {max_val} Juta")
    print("Barang yang dipilih   :")
    
    total_berat = 0
    for name in chosen_items:
        for item in data_items:
            if item.name == name:
                print(f"- {name} (Berat: {item.weight}, Profit: {item.value})")
                total_berat += item.weight
                break         
    print(f"\nTotal Berat Terpakai  : {total_berat} / {kapasitas_gudang} kg")