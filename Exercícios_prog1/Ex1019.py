seg = int(input())
hr = seg // 3600
hr_rest = seg % 3600
min = hr_rest // 60
segnds_rest = hr_rest % 60
print(f'{hr}:{min}:{segnds_rest}')
