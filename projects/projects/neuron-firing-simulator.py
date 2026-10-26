threshold = int(input("Enter the threshold: "))
number_of_signals = int(input("How many signals? "))

signals = []

for i in range(number_of_signals):
    signal = int(input("Enter signal strength: "))
    signals.append(signal)

total = sum(signals)

print("Signals:", signals)
print("Total signal:", total)

if total >= threshold:
    print("Neuron fired!")
elif total >= threshold / 2:
    print("Signal reaching threshold")
else:
    print("Low signal")
