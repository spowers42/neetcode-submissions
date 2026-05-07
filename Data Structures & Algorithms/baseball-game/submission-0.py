class Solution:
    def calPoints(self, operations: List[str]) -> int:
        self.scores = []

        for operation in operations:
            self.process_operation(operation)

        return sum(self.scores)

    def process_operation(self, operation) -> None:
        match operation:
            case "+":
                self.scores.append(self.scores[-1] + self.scores[-2])
            case "D":
                self.scores.append(2 * self.scores[-1])
            case "C":
                self.scores.pop()
            case _:
                # This should only be valid integer values
                self.scores.append(int(operation))
