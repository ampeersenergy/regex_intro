import regex as re
from random import randint


def show_regex_search_result(regular_expression : str, test_text : str) -> None:
    """
    Prints a given string in jupyter, and colors the found strings from the regular expressions
    in test_text green and underlines it with a green text.

    Args:
        regular_expression: Regular expression to test against
        test_text: test text to be printed
    """

    if regular_expression.strip() == "":
        print(test_text)
        return

    test_text = re.sub(regular_expression, lambda match: f"\033[92m\033[4m{match.group(0)}\033[0m", test_text)
    print(test_text)


def show_regex_search_result_group_highlighting(regular_expression : str, test_text : str) -> None:
    """
    Prints a given string in jupyter, and colors the found groups from the regular expressions
    in test_text green and underlines it with a green text.

    Args:
        regular_expression: Regular expression to test against
        test_text: test text to be printed
    """

    if regular_expression.strip() == "":
        print(test_text)
        return

    # generate colors for all groups
    colors = []
    for i in range(0, 10):
        colors.append(f"\033[38;5;{randint(0, 255)}m")

    def color_regex_group_result(match):
        """
        Colors the full match with green, and the groups with the associated colors from the colors list.
        Args:
            match: The match object from the regular expression

        Returns: The colored string

        """
        result = match.group(0)

        string_offset = 0
        for i in range(1, len(match.groups()) + 1):
            start_index = match.start(i) - match.start(0) + string_offset
            end_index = match.end(i) - match.start(0) + string_offset

            result = result[:start_index] + colors[i] + match.group(i) + "\033[0m" + result[end_index:]

            string_offset += len(colors[i]) + 4

        return result

    test_text = re.sub(regular_expression, color_regex_group_result, test_text)

    for ind, color in enumerate(colors[1:re.compile(regular_expression).groups + 1]):
        pattern = re.findall(r"\(.+?\)",regular_expression)[ind]
        test_text += f"\n\033[0m{color}Group {ind+1}: {pattern}\033[0m"

    print(test_text)


def show_regex_substitution_highlighting(regular_expression : str, substitution : str, test_text : str) -> None:
    """
    Performs a substitution operation using regex, and then prints the original and modified strings, where
    the differences between original and modified strings are highlighted in red in the modified string.
    Args:
        regular_expression: Regular expression to search on
        substitution: Substitution string
        test_text: Text where operation is performed on
    """

    if regular_expression.strip() == "":
        print(test_text)
        return


    def get_difference_string(original : str, modified : str) -> list[str]:
        """
        Returns a string where the differences between original and modified strings are highlighted in red.
        Args:
            original: Original string
            modified: Modified string

        Returns: The difference string
        """

        string1 = original.split()
        string2 = modified.split()

        str_diff = set(string1).symmetric_difference(set(string2))

        return list(str_diff)

    regex = re.compile(regular_expression)
    modified_string = regex.sub(substitution, test_text)

    differences = get_difference_string(test_text, modified_string)

    print(" ".join([i for i in re.split(r"\s+", test_text)]))
    print("\033[91m" + " ".join([("^" if i in differences else " ")*len(i) for i in re.split(r"\s+", test_text)]) + "\033[0m")
    print(modified_string)
    print("\033[91m" + " ".join([("^" if i in differences else " ")*len(i) for i in re.split(r"\s+", modified_string)]) + "\033[0m")

