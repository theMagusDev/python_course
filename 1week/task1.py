"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/count-and-say/description/
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        currentStr = "1"
        resultingStr = ""

        leftPtr, rightPtr = 0, 0
        counter = 0
        for i in range(1, n):
            leftPtr, rightPtr = 0, 0
            counter = 0
            resultingStr = ""
            while leftPtr <= len(currentStr) - 1:
                while rightPtr <= len(currentStr) - 1 and currentStr[leftPtr] == currentStr[rightPtr]:
                    counter += 1
                    rightPtr += 1
                resultingStr += str(counter) + currentStr[leftPtr]
                leftPtr = rightPtr
                counter = 0
            currentStr = resultingStr
        return currentStr
