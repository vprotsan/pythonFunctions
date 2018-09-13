import string
import re

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        lowerAlph = string.ascii_lowercase
        upperAlph = string.ascii_uppercase
        self.shift_dict = {}
        if shift >= 0 and shift < 26:
            for start in list(range(26)):
                totNum = start + shift
                if totNum < 26:
                    # print(totNum)
                    self.shift_dict[lowerAlph[start]] = lowerAlph[totNum]
                    self.shift_dict[upperAlph[start]] = upperAlph[totNum]
                else:
                    newShiftNum = totNum % 26
                    # print("new shift num " + str(newShiftNum))
                    self.shift_dict[lowerAlph[start]] = lowerAlph[newShiftNum]
                    self.shift_dict[upperAlph[start]] = upperAlph[newShiftNum]
        return self.shift_dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        self.build_shift_dict(shift)
        newString = ''
        for i in self.message_text:
            if i not in self.shift_dict:
               newString += i
            else:
               newString += self.shift_dict[i]
        self.newString = newString
        return self.newString


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        # self.message_text
        # self.valid_words
        Message.__init__(self, text)
        # self.shift
        self.shift = shift
        # self.encrypting_dict
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        copyOfencrypting_dict = self.encrypting_dict.copy()
        return copyOfencrypting_dict
        # pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        copyOfmessage_text_encrypted = self.message_text_encrypted[:]
        return copyOfmessage_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        if shift >= 0 and shift < 26:
            self.shift = shift
            self.encrypting_dict = Message.build_shift_dict(self, shift)
            self.message_text_encrypted = Message.apply_shift(self, shift)



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        returnedValue = ()
        currMsgArr = re.findall(r"[\w']+|[.,!?;]", self.message_text)
        matchedWordsPreviousTotal = 0;bestMatch = 0
        for i in list(range(26)):
            decryptedString = []
            currDict = self.build_shift_dict(i)
            for word in currMsgArr:
                possibleWord = ''
                for letter in word:
                    if letter in currDict:
                        possibleWord += currDict[letter]
                    else:
                        possibleWord += letter
                decryptedString.append(possibleWord)
            matchedWordsTotal = 0;
            for eachWord in decryptedString:
                if eachWord in self.valid_words:
                    matchedWordsTotal += 1
                elif  eachWord == "," or eachWord == "?" or eachWord == "!":
                    matchedWordsTotal += 1
                if matchedWordsTotal > matchedWordsPreviousTotal:
                    matchedWordsPreviousTotal = matchedWordsTotal
                    bestMatch = i
        decryptedStringOutput = self.apply_shift(bestMatch)
        returnedValue += (bestMatch,decryptedStringOutput,)
        return returnedValue

def decrypt_story():
    currStory = get_story_string()
    ciphertext = CiphertextMessage(currStory)
    return ciphertext.decrypt_message()

####################################################################
#tests
####################################################################
# {'a': 'd', 'A': 'D', 'b': 'e', 'B': 'E', 'c': 'f', 'C': 'F', 'd': 'g', 'D': 'G', 'e': 'h', 'E': 'H', 'f': 'i', 'F': 'I', 'g': 'j', 'G': 'J', 'h': 'k', 'H': 'K', 'i': 'l', 'I': 'L', 'j': 'm', 'J': 'M', 'k': 'n', 'K': 'N', 'l': 'o', 'L': 'O', 'm': 'p', 'M': 'P', 'n': 'q', 'N': 'Q', 'o': 'r', 'O': 'R', 'p': 's', 'P': 'S', 'q': 't', 'Q': 'T', 'r': 'u', 'R': 'U', 's': 'v', 'S': 'V', 't': 'w', 'T': 'W', 'u': 'x', 'U': 'X', 'v': 'y', 'V': 'Y', 'w': 'z', 'W': 'Z', 'x': 'a', 'X': 'A', 'y': 'b', 'Y': 'B', 'z': 'c', 'Z': 'C'}

# print('_______________________________________________________')
# plaintext = PlaintextMessage('hello, mother sunshine', 2)
# print('Expected Output: jgnnq, oqvjgt uwpujkpg')
# print('Actual Output:', plaintext.get_message_text_encrypted())
# print('_______________________________________________________')
# ciphertext = CiphertextMessage('complain rule quick sample seat pride modesty time advance net account direction situation neighbor report')
# print('Actual Output:', ciphertext.decrypt_message())
# print('_______________________________________________________')
# ciphertext = CiphertextMessage('bargain great tight nation overflow sea grease invent mere desire low possessor ruin grateful upper fan orange best continue remark many vessel tune satisfactory hold parent gain speed other wear truth people offend confidential wire')
# print('Actual Output:', ciphertext.decrypt_message())
# print('_______________________________________________________')
# ciphertext = CiphertextMessage('bargain great tight nation overflow sea grease invent mere desire low possessor ruin grateful upper fan orange best continue remark many vessel tune satisfactory hold parent gain speed other wear truth people offend confidential wire')
# print('Actual Output:', ciphertext.decrypt_message())
