from collections import Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        preferences_count = Counter(students)

        for sandwich in sandwiches:
            if preferences_count[sandwich] > 0:
                preferences_count[sandwich] -= 1
            else:
                break
        
        return sum(preferences_count.values())