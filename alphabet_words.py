a = {
      "a": "apple",
      "b": "boy",
      "c": "cat",
      "d": "dog",
      "e": "elephant",
      "f": "frog",
      "g": "grapes",
      "h": "hut",
      "i": "ice cream",
      "j": "joker",
      "k": "kite",
      "l": "lamp",
      "m": "mango",
      "n": "nest",
      "o": "owl",
      "p": "parrot",
      "q": "quin",
      "r": "rat",
      "s": "sun",
      "t": "tiger",
      "u": "umbrella",
      "v": "vulture",
      "w": "watch",
      "x": "x-mass tree",
      "y": "yak",
      "z": "zebra",
}
b = input("enter the alphabet: ")
if b in a:
    print(a[b])
else:
    print("only alphabets are allowed")
