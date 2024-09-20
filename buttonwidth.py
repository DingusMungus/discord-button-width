# Converted from https://github.com/Luke265/discord-button-width
from typing import Dict, List, Tuple

Align = {
    'LEFT': 'start',
    'RIGHT': 'end',
    'CENTER': 'center',
}

# Define the CHAR_MAP dictionary
CHAR_MAP = {
	'0': 8.67,
	'1': 5,
	'2': 7.47,
	'3': 7.18,
	'4': 8.25,
	'5': 7.38,
	'6': 7.9,
	'7': 7.38,
	'8': 7.95,
	'9': 7.9,
	'a': 6.98,
	'b': 7.45,
	'c': 6.53,
	'd': 7.53,
	'e': 6.98,
	'f': 4.35,
	'g': 7.05,
	'h': 7.38,
	'i': 3.4,
	'j': 3.4,
	'k': 6.73,
	'l': 3.4,
	'm': 11.42,
	'n': 7.38,
	'o': 7.38,
	'p': 7.53,
	'q': 7.45,
	'r': 5.02,
	's': 6.18,
	't': 4.72,
	'u': 7.38,
	'v': 6.58,
	'w': 10.1,
	'x': 6.6,
	'y': 6.77,
	'z': 6.32,
	'ą': 6.98,
	'č': 6.53,
	'ę': 6.98,
	'ė': 6.98,
	'į': 3.4,
	'š': 6.18,
	'ų': 7.38,
	'ū': 7.38,
	'ž': 6.32,
	'A': 9.63,
	'B': 7.63,
	'C': 8.85,
	'D': 9.83,
	'E': 7.08,
	'F': 6.68,
	'G': 9.75,
	'H': 9.83,
	'I': 3.8,
	'J': 5.17,
	'K': 8.52,
	'L': 6.55,
	'M': 12.6,
	'N': 9.83,
	'O': 10.43,
	'P': 7.5,
	'Q': 10.43,
	'R': 7.98,
	'S': 7.17,
	'T': 8.4,
	'U': 9.65,
	'V': 9.47,
	'W': 14.23,
	'X': 8.9,
	'Y': 8.9,
	'Z': 8.33,
	'Ą': 9.63,
	'Č': 8.85,
	'Ę': 7.08,
	'Ė': 7.08,
	'Į': 3.8,
	'Š': 7.17,
	'Ų': 9.65,
	'Ū': 9.65,
	'Ž': 8.33,
    ' ': 3,
    '/': 7.5,
	'*': 5.6,
	'-': 4.95,
	',': 3.17,
	'.': 3.17,
	'_': 6.35,
	'?': 7.25,
	'!': 3.8,
	'#': 9.25,
	'@': 11.7,
	'$': 7.38,
	'%': 12.6,
	'^': 6.35,
	'&': 9.53,
	'=': 8.25,
	'<': 8,
	'>': 8,
	'\\': 7.5,
	'|': 3.72,
	'"': 5.72,
	"'": 3.17,
	';': 3.3,
	':': 3.3,
	'{': 6.67,
	'}': 6.67,
	'[': 5.72,
	']': 5.72,
	'(': 5.47,
	')': 5.47,
	'`': 6.35,
	'~': 5.72,
	' ': 3.8,
}

# Define the PAD_MAP list
PAD_MAP = [    
	('　', 14),
  	(' ', 4.65),
  	(' ', 3.5),
  	(' ', 1.87),
  	(' ', 1.05),
]

BR = "\u200b"


class DiscordButtonWidthUtil:
    def __init__(self):
        self.default_char_width = 7

    def get_string_width(self, string: str) -> float:
        return sum(CHAR_MAP.get(char, self.default_char_width) for char in string)

    def pad_string_to_width(self, string: str, width: float, align: str = Align['LEFT']) -> str:
        current_width = self.get_string_width(string)
        if current_width >= width:
            return string
        pad_width = width - current_width
        if align == Align['RIGHT']:
            return BR + self.pad(pad_width) + string + BR
        elif align == Align['CENTER']:
            pad = self.pad((width - current_width) / 2)
            return BR + pad + string + pad + BR
        return string + self.pad(pad_width) + BR

    def pad(self, width: float) -> str:
        result = ''
        remaining_width = width
        for char, char_width in PAD_MAP:
            if remaining_width < 0.5:
                break
            repeat = int(remaining_width // char_width)
            if repeat == 0:
                continue
            remaining_width -= char_width * repeat
            result = result.ljust(len(result) + repeat, char)
        return result

buttonwidth = DiscordButtonWidthUtil()
