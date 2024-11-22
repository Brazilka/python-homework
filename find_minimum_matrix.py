import random
rows = int(input("Počet řádků: "))
columns = int(input("Počet sloupců: "))
#matice bude mít rows sublistů a columns bude její počet indexů v sublistu
matrix = [[random.randint(1,10) for x in range(columns)] for y in range(rows)]
print(matrix)

for i in range(rows):
    nejvyssi = max(matrix[i])
    #print(nejvyssi)
    column_index = matrix[i].index(nejvyssi)
    #print(column_index)
    lokace = [i,column_index] 
    column_values = [matrix[i][column_index] for i in range(rows)]
    #print(column_values)
    nejnizsi = min(column_values)
    #print(nejnizsi)
    if nejvyssi == nejnizsi:
        print(f"Sedlovej bod je {lokace} a má hodnotu {nejnizsi}")
    #else:
     #   print("Sedlovej bod nenalezenej")