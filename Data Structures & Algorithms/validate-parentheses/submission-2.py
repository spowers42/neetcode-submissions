class Solution:
    def isValid(self, s: str) -> bool:
        CLOSE_TO_OPEN = {')': '(', ']':'[', '}':'{'}
        characters = []

        for character in s:
            if character in CLOSE_TO_OPEN.values():
                characters.append(character)
            else:
                if characters and characters[-1] == CLOSE_TO_OPEN[character]:
                    characters.pop()
                else:
                    return False

        if len(characters):
            # Edge case, more open than close characters
            return False
        return True
