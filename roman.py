# Roman to Integer Program: specific instructions given by LeetCode
class Solution:
    """Initialize the Solution class with a conversion dictionary."""
    def __init__(self):
        self.convert_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def validate(self) -> str:
        """Validate the input Roman numeral.

        Returns:
            str: The valid Roman numeral entered by the user.
        """
        while True:
            try:
                roman = input("Enter Roman numeral: ")

                # Check string length
                if not 1 <= len(roman) <= 15:
                    raise ValueError("Invalid input: Number of characters must be between 1 and 15.")

                # Check for non-roman numerals
                for ch in roman:
                    if ch not in self.convert_nums:
                        raise ValueError("Invalid input: Roman numerals ONLY")

                # Check for invalid roman numeral combinations
                i = 0
                while i < len(roman):
                    curr = roman[i]
                    nxt = roman[i+1] if i + 1 < len(roman) else None
                    if curr == nxt:
                        count = 1
                        while i < len(roman)-1 and roman[i] == roman[i+1]:
                            count += 1
                            i += 1
                            if count > 3:
                                raise ValueError("Invalid input: Roman numeral combination does not exist.")
                    i += 1

                # Check Roman numeral length
                if not 1 <= self.roman_to_int(roman) <= 3999:
                    raise ValueError("Invalid input: Roman numerals sum must be between 1 and 3999.")

                break  # Str is valid
            except ValueError as e:
                print(str(e))
        return roman

    def roman_to_int(self, roman_nums: str) -> int:
        """Convert the Roman numeral to an integer.

        Args:
            roman_nums (str): The Roman numeral to convert.

        Returns:
            int: The converted integer value.
        """
        total = 0
        last = self.convert_nums[roman_nums[-1]]

        for index in range(len(roman_nums)-1):
            curr = self.convert_nums[roman_nums[index]]
            nxt = self.convert_nums[roman_nums[index+1]]
            if curr < nxt:
                total -= curr
            else:
                total += curr
        return total + last

    def explanation(self, r: str):
        """Provide an explanation of the Roman numeral conversion.

        Args:
            r (str): The Roman numeral.

        Returns:
            str: The explanation of the conversion.
        """
        out_list = []

        i = 0
        while i < len(r):
            curr = self.convert_nums[r[i]]
            nxt = self.convert_nums[r[i + 1]] if i < len(r)-1 else None

            if curr < nxt:
                out_list.append(f"{r[i]}{r[i + 1]} = {nxt - curr}")
                i += 2
            elif curr == nxt:
                j = 1
                dup = curr
                while i < len(r)-1 and r[i] == r[i + 1]:
                    j += 1
                    i += 1
                out_list.append(f"{r[i] * j} = {j * dup}")
                i += 1
            else:
                out_list.append(f"{r[i]} = {curr}")
                i += 1
        output = ", ".join(out_list) + "."

        return output


def main():
    """Main function"""
    sol = Solution()

    while True:
        roman = sol.validate()
        result = sol.roman_to_int(roman)

        print(f"Output: {result}")
        print(f"Explanation: {sol.explanation(roman)}")

        while True:
            again = input("Play again? [Y/N]: ")
            if again == 'N':
                print("Thanks for playing! Quitting...")
                return False
            elif again == 'Y':
                break
            else:
                print("I didn't understand that...")


if __name__ == '__main__':
    main()
