seq = [1, True, 0, False, 1, 1, 2, 3]

# for number, item in enumerate(seq):
# print(number, item)


print(list(map(str, seq)))
new_seq = []
for i in seq:
    new_seq.append(str(i))
print(new_seq)
a = None

if a == True:
    print('aaaa')
else:
    print('bbb')

print('aaa') if a else print('bbb')
