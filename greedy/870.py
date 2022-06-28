class Solution(object):
    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)
        assigned = {b: [] for b in B}
        remaining = []

        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        return [assigned[b].pop() if assigned[b] 
                else remaining.pop() for b in B]