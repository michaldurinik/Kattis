import sys
a, b = sys.stdin.readline().strip().split()
a,b = int(a),int(b)

print(sorted([num + x for num in range(1,a+1) for x in range(1, b+1)]))
arr = []
for num in range(1, a+1):
	for i in range(1,b+1):
		arr.append(num+i)

counter_dict = {}
for num in arr:
	if num in counter_dict:
		counter_dict[num] += 1
	else:
		counter_dict[num] = 1

maxi = max(counter_dict.values())

for k,v in sorted(counter_dict.items(), key=lambda x:x[1], reverse=True):
	if v != maxi:
		break
	print(k)
