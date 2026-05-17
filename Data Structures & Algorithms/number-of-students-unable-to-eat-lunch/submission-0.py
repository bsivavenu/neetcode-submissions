class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count the number of students preferring 0 (circular) and 1 (square)
        # index 0 stores count of 0s, index 1 stores count of 1s
        counts = [students.count(0), students.count(1)]
        
        for sandwich in sandwiches:
            # If no student left wants this type of sandwich, the line stalls
            if counts[sandwich] == 0:
                break
            # Otherwise, a student takes it
            counts[sandwich] -= 1
            
        # The remaining students unable to eat is the sum of left-over counts
        return sum(counts)