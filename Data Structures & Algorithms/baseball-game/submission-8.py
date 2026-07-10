class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum_of_scores = 0
        for operation in operations:
            if operation == "+":
                last_score = record[-1]
                second_last_score = record[-2]
                added_score = last_score + second_last_score
                sum_of_scores += added_score
                record.append(added_score)
            elif operation == "D":
                previous_score = record[-1]
                doubled_score = previous_score * 2
                sum_of_scores += doubled_score
                record.append(doubled_score)
            elif operation == "C":
                deleted_score = record.pop()
                sum_of_scores -= deleted_score
            else:
                score = int(operation)
                sum_of_scores += score
                record.append(score)

        return sum_of_scores
        