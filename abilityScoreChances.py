def roll():
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                for d4 in range(1, 7):
                    current_roll = [d1, d2, d3, d4]
                    current_roll.sort()
                    total = current_roll[1]+current_roll[2]+current_roll[3]
                    try:
                        results[total] += 1
                    except IndexError:
                        print("index:", str(total))


results = [0] * 19
roll()
count = 0
for i in range(3, 19):
    count += results[i]
print("total combinations:", str(count))
for i in range(3, 19):
    print(str(i), "-", str(results[i]), "-", str(results[i]/count*100)+"%")
input()
# console output:
# total combinations: 1296
# 3 - 1 - 0.07716049382716049%
# 4 - 4 - 0.30864197530864196%
# 5 - 10 - 0.7716049382716049%
# 6 - 21 - 1.6203703703703702%
# 7 - 38 - 2.9320987654320985%
# 8 - 62 - 4.78395061728395%
# 9 - 91 - 7.021604938271605%
# 10 - 122 - 9.41358024691358%
# 11 - 148 - 11.419753086419753%
# 12 - 167 - 12.885802469135802%
# 13 - 172 - 13.271604938271606%
# 14 - 160 - 12.345679012345679%
# 15 - 131 - 10.108024691358025%
# 16 - 94 - 7.253086419753087%
# 17 - 54 - 4.166666666666666%
# 18 - 21 - 1.6203703703703702%

