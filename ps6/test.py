import string

def build_shift_dict(shift):
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
      lowerShifted = {}
      upperShifted = {}
      if shift >= 0 and shift < 26:
          for l in list(lowerAlph):
              lowerShifted[l] = lowerAlph[l + shift]
              upperShifted[l] = upperAlph[l + shift]
              print(lowerShifted[l])
              print(upperShifted[l])
      return lowerShifted, upperShifted


build_shift_dict(3)
