from bs4 import BeautifulSoup
import requests


class MorseCodeConverter:
    def __init__(self):

        response = requests.get("https://encyclopedia2.thefreedictionary.com/List+of+Morse+Code").text
        soup = BeautifulSoup(response, 'html.parser')
        pretty_table = soup.select(".prettytable")

        word_list = [word.text for word in pretty_table[0].find_all("td")]
        alphabet = word_list[::2]
        alphabet_code = word_list[1::2]

        number_list = [word.text for word in pretty_table[1].find_all("td")]
        number = number_list[::2]
        number_code = number_list[1::2]
        number[-1] = ","
        number[-2] = "."

        alphabet.extend(number)
        alphabet_code.extend(number_code)
        alphabet_code = [code.replace(" ", "") for code in alphabet_code]

        response = requests.get("https://morsedecoder.com/").text
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.select(".table")[-1].find_all("tr")

        string = ""
        for table in table:
            string += table.text.replace(".", "").replace("-", "")

        list1 = [string for string in string][1::]

        table = soup.select(".table")[-1].find_all("tr")
        string = ""
        for table in table:
            string += table.text

        for char in list1:
            string = string.replace(char, " ").replace(".", "·").replace("-", "–")
        list2 = string.split(" ")[1::]

        alphabet.extend(list1)
        alphabet_code.extend(list2)

        self.dict_to_code = {key: value for (key, value) in zip(alphabet, alphabet_code)}
        self.dict_to_text = {key: value for (key, value) in zip(alphabet_code, alphabet)}

        self.previous = None

    def string_to_code(self, string: str, to_real_char: bool = False) -> str:

        """Takes a string a returns it as a morse code.

        Args:
            string (str): Takes a text

            to_real_char (bool): Default is False. If True, returns the morse code as dash(-) and period(.).

        Return:
            string (str): Returns a morse code as a string
        """

        code = ""
        for char in string.upper():
            try:
                code += self.dict_to_code[char]
            except KeyError:
                code += char
            finally:
                code += " "

        if to_real_char:
            code = code.replace("·", ".").replace("–", "-")

        code = code[:-1:]

        self.previous = code

        return code

    def code_to_string(self, code: str) -> str:

        """Takes a morse code a returns it as a text.

            Args:
                code (str): Required: Takes a code

            Return:
                text (str): Returns the code that's converted back into a text
        """
        if self.previous:
            if code.lower() == "pre":
                code = self.previous

        code = code.replace(".", "·").replace("-", "–")
        code = code.split(" ")

        text = ""
        for char in code:
            try:
                text += self.dict_to_text[char]
            except KeyError:
                if char == "":
                    text += " "
                else:
                    text += char

        text = text.replace("   ", " ").replace("  ", " ")
        return text
