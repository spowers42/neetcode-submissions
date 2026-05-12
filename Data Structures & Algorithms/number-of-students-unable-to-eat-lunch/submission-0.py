from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = deque(students)
        sammies_stack = deque(sandwiches)

        while sammies_stack and sammies_stack[0] in student_queue:
            student = student_queue.popleft()
            if student == sammies_stack[0]:
                sammies_stack.popleft()
            else:
                student_queue.append(student)

        return len(sammies_stack)
