from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        permutationLength = len(nums)
        sortedList = nums[:]
        sortedList = sorted(sortedList)
        for i in range(permutationLength):
            sortedList[i] = [sortedList[i], i]
        sortedList2 = sortedList[:]
        treeOrder = [[0, 0]] * permutationLength
        for i in range(permutationLength):
            treeOrder[i] = [sortedList.index([nums[0], i]), i]
            sortedList.pop(sortedList.index([nums[0], i]))
            nums.pop(0)

        backwardsIndex = 0
        carry = 0
        while True:
            if backwardsIndex > permutationLength - 1 and carry == 1:
                treeOrder = [0] * permutationLength
                break
            if backwardsIndex == 0 or carry == 1:
                if (
                    treeOrder[permutationLength - backwardsIndex - 1] + 1
                    > backwardsIndex
                ):
                    carry = 1
                    treeOrder[permutationLength - backwardsIndex - 1] = 0
                else:
                    carry = 0
                    treeOrder[permutationLength - backwardsIndex - 1] += 1

            elif carry == 0:
                break

            backwardsIndex += 1

        for i in range(permutationLength):
            nums.append(sortedList2[treeOrder[0]])
            sortedList2.pop(treeOrder[0])
            treeOrder.pop(0)
        return


sol = Solution()
sol.nextPermutation([1, 5, 1])
