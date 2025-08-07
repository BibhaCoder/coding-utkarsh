chars = "abcdefghijklmnopqrstuvwxyz0123456789"
s, e = input().lower().split("-")

start = chars.index(s)
end = chars.index(e)

if start <= end:
    for i in range(start, end + 1):
        print(chars[i])
