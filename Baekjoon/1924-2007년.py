months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
m, d = map(int, input().split())
print(days[(sum(months[:m]) + d) % 7])
