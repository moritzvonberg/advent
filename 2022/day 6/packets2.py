import aocd


signal = aocd.get_data(day=6, year=2022).rstrip()

answer = None
for i in range(len(signal) - 14):
    if len(set(signal[i:i+14])) == 14:
        answer = i + 14
        break    

for i in range(answer-15, answer+3):
    print(f"{i}: {signal[i]}")


aocd.submit(answer=answer, part='b', day=6, year=2022)