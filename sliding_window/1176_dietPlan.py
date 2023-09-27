class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        points = 0

        T = 0
        for i in range(0,k):
            T += calories[i]
        
        if k == len(calories):
            if T < lower:
                return -1
            elif T > upper:
                return 1

        for j in range(0,len(calories) - k):
            if T < lower:
                points -= 1
            elif T > upper:
                points += 1
            T = T - calories[j] + calories[k + j]

        if T < lower:
            points -= 1
        elif T > upper:
            points += 1

        return points