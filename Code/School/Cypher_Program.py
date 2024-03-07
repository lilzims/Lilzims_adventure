import string

class Caesar:
    def __init__(self):
        self.upper_letters = list(string.ascii_uppercase)
        self.lower_letters = list(string.ascii_lowercase)

        self.encoded = ""
        self.decoded = ""

    def get_text(self):
        print("Enter the text to encode: ")
        self.text = input()

    def enc(self, shifter):
        self.encoded = ""  
        shift_distance = int(shifter)
        for letter in self.text:
            if letter in self.upper_letters:
                index = (self.upper_letters.index(letter) + shift_distance) % len(self.upper_letters)
                self.encoded += self.upper_letters[index]
            elif letter in self.lower_letters:
                index = (self.lower_letters.index(letter) + shift_distance) % len(self.lower_letters)
                self.encoded += self.lower_letters[index]
            else:
                self.encoded += letter

        return self.encoded

    def dec(self, shifter):
        self.decoded = ""  
        shift_distance = int(shifter)

        for letter in self.encoded:
            if letter in self.upper_letters:
                index = (self.upper_letters.index(letter) - shift_distance) % len(self.upper_letters)
                self.decoded += self.upper_letters[index]
            elif letter in self.lower_letters:
                index = (self.lower_letters.index(letter) - shift_distance) % len(self.lower_letters)
                self.decoded += self.lower_letters[index]
            else:
                self.decoded += letter
        return self.decoded

caesar_instance = Caesar()
done = False

while not done:
    caesar_instance.get_text()

    print("What number will you use for the shift (type 'exit' to end): ")
    shift_level = input()

    if shift_level.lower() == 'exit':
        done = True
    else:
        print("Encoded text: " + caesar_instance.enc(shift_level))
        print("Decoded text: " + caesar_instance.dec(shift_level))
