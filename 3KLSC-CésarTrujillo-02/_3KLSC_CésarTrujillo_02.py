NUM = 8
nums = [0] * NUM
total = 0

for i in range(NUM):
    nums[i] = int(input(f"Por favor, Introduza el numero en la posicion {i + 1}: "))
    total += nums[i]

print("El total de la suma es: ", total)
