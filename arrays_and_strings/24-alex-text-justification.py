class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []

        current_len = 0
        start = 0
        end = -1

        for i, word in enumerate(words):
            new_len = len(word) + current_len + (1 if current_len != 0 else 0)

            if new_len < maxWidth:
                current_len = new_len
                continue

            including_i = new_len == maxWidth
            end = i + (0 if including_i else -1)
            lines.append((start, end))
            start = end + 1
            current_len = 0 if including_i else len(word)

        if len(lines) == 0 or lines[-1][-1] != len(words) - 1:
            lines.append((start, len(words)-1))

        result = []

        for line_idx, line in enumerate(lines):
            n_words = line[1] + 1 - line[0]
            line_words = words[line[0]:line[1]+1]
            words_length = sum(len(word) for word in line_words)
            n_gaps = max(n_words - 1, 1)

            space_left = maxWidth - words_length
            min_spaces = space_left // n_gaps

            result_string = ""

            if line_idx == len(lines) - 1:
                result_string += " ".join(line_words) + " " * (space_left - n_words + 1)
            else:
                for i in range(n_words):
                    result_string += words[line[0]+i]
                    if i != n_words - 1 or n_words == 1:
                        result_string += " " * (min_spaces + (1 if i <= space_left % n_gaps - 1 else 0))

            result.append(result_string)

        return result

