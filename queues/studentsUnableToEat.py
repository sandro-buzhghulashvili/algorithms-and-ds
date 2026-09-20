
## Input: students = [1,1,0,0], sandwiches = [0,1,0,1]

from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students_queue = deque(students)
        sandwiches_queue = deque(sandwiches)

        operation = 0

        while students_queue and sandwiches_queue:
            if students_queue[0] == sandwiches_queue[0]:
                students_queue.popleft()
                sandwiches_queue.popleft()
                operation = 0
            else:
                s = students_queue.popleft()
                students_queue.append(s)
                operation += 1

                if operation == len(students_queue):
                    break
        
        return len(students_queue)