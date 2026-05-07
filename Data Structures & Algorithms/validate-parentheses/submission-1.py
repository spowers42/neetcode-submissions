class Solution:
    def isValid(self, s: str) -> bool:
        characters = []

        for character in s:
            if self.is_opening(character):
                characters.append(character)
            else:
                if len(characters) == 0:
                    # Edge case, starting with closing character
                    return False
                pair = (characters.pop(), character)
                if not self.matches(pair):
                    return False

        if len(characters):
            # Edge case, more open than close characters
            return False
        return True

    @staticmethod
    def is_opening(character: str) -> bool:
        match character:
            case "(":
                return True
            case "[":
                return True
            case "{":
                return True
            case _:
                return False

    @staticmethod
    def matches(pair: (str, str)) -> bool:
        match pair:
            case ("(", ")"):
                return True
            case ("[", "]"):
                return True
            case ("{", "}"):
                return True
            case _:
                return False
