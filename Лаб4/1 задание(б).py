f = open('27-123b.txt')
n, k, v = map(int, f.readline().split())
a = [0] * k

k_del, ost  = k // 2, k % 2

for i in range(n):
    kilometer_num, kolvo = map(int, f.readline().split())
    a[kilometer_num % k] = kolvo // v + (kolvo % v > 0)

min_sum = 10**25
s = 0

for i in range(1, k):
    s += a[i] * (2*k_del + ost - abs(2*(i-k_del) - ost)) // 2

d = a[0] + sum(a[k_del + 2:k]) - sum(a[1:k_del + 1])

for i in range(1, k):
    s += d
    d += 2 * a[i] - a[(k_del + i) % k] - a[(k_del + i + ost) % k]
    min_sum = min(min_sum, s)
print(min_sum)