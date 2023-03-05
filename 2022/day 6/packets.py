import aocd

signal = aocd.get_data(day=6, year=2022).rstrip()

answer = None
for i in range(len(signal) - 4):
    if len(set(signal[i:i+4])) == 4:
        answer = i + 4
        break    

for i in range(answer-5, answer+3):
    print(f"{i}: {signal[i]}")

print(answer)
aocd.submit(answer=answer, part='a', day=6, year=2022)