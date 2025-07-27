n = int(input())
temp_sum, bar_sum, bar_count = 0, 0, 0
for i in range(n):
    tmp_temp, tmp_bar = map(float, input().split())
    if tmp_temp < 80 and tmp_temp > -70:
        bar_sum += tmp_bar
        bar_count += 1
    temp_sum += tmp_temp
print(f'{(temp_sum / n):.4f}', f'{(bar_sum / bar_count):.4f}')
