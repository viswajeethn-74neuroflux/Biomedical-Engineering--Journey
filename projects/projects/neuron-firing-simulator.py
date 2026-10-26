threshold = 10

signal1 = int(input("Enter the first signal: "))
signal2 = int(input("Enter the second signal: "))

total = signal1 + signal2

print("Total signal:", total)

if total >= threshold:
    print("Neuron fired!")
elif total >= 5:
    print("Signal reaching threshold")
else:
    print("Low signal")
thsi code i should put
