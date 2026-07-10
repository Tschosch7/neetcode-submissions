class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == "+":
                last_score = record[-1]
                second_last_score = record[-2]
                record.append(last_score + second_last_score)
            elif operation == "D":
                previous_score = record[-1]
                record.append(previous_score * 2)
            elif operation == "C":
                record.pop()
            else:
                record.append(int(operation))
        
        sum_of_scores = 0
        while record:
            sum_of_scores += record.pop()
        return sum_of_scores
        