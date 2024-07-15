from itertools import permutations


s = "barfoothefoobarman"
words = ["bar", "foo"]

permutation = []

for i in permutations(words):
    print(i)
    permutation.append(''.join(i))

print(permutation)

s_permutation = []

index_position = []

for permu_s in permutation:
    index = s.find(permu_s)
    # if permu_s in s:
    if permu_s:
        s_permutation.append(permu_s)
        index_position.append(index)

print(s_permutation)
print(index_position)

