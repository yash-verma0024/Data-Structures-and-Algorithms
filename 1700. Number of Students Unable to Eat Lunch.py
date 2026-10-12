class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count = [students.count(0), students.count(1)]

        for sandwich in sandwiches:
            if count[sandwich] == 0:
                break
            count[sandwich] -= 1
        return sum(count)
