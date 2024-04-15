from ast import List


def kidsWithCandies(candies, extraCandies):
        result = []
        for i in range(len(candies)):
            print(max(candies))
            if (candies[i] + extraCandies) >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return candies


print(kidsWithCandies([2,3,5,1,3], 3))