from itertools import permutations


s = "barfoothefoobarman"
words = ["bar", "foo"]
permutation = []
for i in permutations(words):
    permutation.append(''.join(i))
s_permutation = []
index_position = []
for perm in permutation:
    index = s.find(perm)
    if perm:
        s_permutation.append(perm)
        index_position.append(index)
print(index_position)

