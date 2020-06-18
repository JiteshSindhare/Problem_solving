class Solution:
    def count(self, A: List[int], B: List[int]):
        dictA = {A[0]: 1}
        dictB = {B[0]: 1}
        check = A[0]
        not_needed = True
        counts = {A[0]: 1, B[0]: 1}
        for i in range(1, len(A)):
            if A[i] in counts.keys():
                counts[A[i]] += 1
                if A[i] in dictA.keys():
                    dictA[A[i]] += 1
                else:
                    dictA[A[i]] = 1
            if check != A[i]:
                not_needed = False
            if B[i] in counts.keys():
                counts[B[i]] += 1
                if B[i] in dictB.keys():
                    dictB[B[i]] += 1
                else:
                    dictB[B[i]] = 1

        # print(counts,dictA,dictB)
        return (counts, dictA, dictB, not_needed)

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        possible = False
        pivot = 0
        primary = 0
        secondary = 0
        # check=A[0]
        # not_needed=True
        need = 0
        # for i in range(len(A)):
        #     if check!=A[i]:
        #         not_needed=False
        # if not_needed:
        #     return 0
        counts, dicA, dicB, not_needed = self.count(A, B)
        # print(counts,len(A))
        if not_needed:
            return 0
        for key, val in counts.items():
            if val >= len(A):
                pivot = key
                possible = True
        if not possible:
            return -1
        if pivot in dicA.keys() and pivot in dicB.keys():
            if dicA[pivot] > dicB[pivot]:
                primary = A
                secondary = B
                need = len(A) - dicA[pivot]
            else:
                primary = B
                secondary = A
                need = len(B) - dicB[pivot]
        elif pivot in dicA.keys() and pivot not in dicB.keys():
            primary = A
            secondary = B
            need = len(A) - dicA[pivot]
        elif pivot not in dicA.keys() and pivot in dicB.keys():
            primary = B
            secondary = A
            need = len(B) - dicB[pivot]
        result = 0
        print('primary is', primary)

        for i in range(len(primary)):
            if primary[i] == pivot:
                continue
            elif secondary[i] == pivot:
                result += 1
        return result if (result >= need and result != 0) else -1

