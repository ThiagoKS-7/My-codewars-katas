from string import ascii_lowercase


def alphabet_position(text):
    res=" " .join(map(str,[str(ascii_lowercase.index(i.lower())+1)
      for i in text if i.lower() in
      ascii_lowercase]))
    return res.rstrip()
