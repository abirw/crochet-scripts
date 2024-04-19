import numpy as np
from PIL import Image
from os import walk
import random

f = []
for (dirpath, dirnames, filenames) in walk("./word-files"):
    f.extend(filenames)
    break

colours = [[1,56,17],[11,97,36],[4,120,37]]
print(f)

letter_files = {"a":"a.png", "b":"b.png", "c":"c.png", "d":"d.png", "e":"e.png", "f":"f.png", "g":"g.png", "h":"h.png", "i":"i.png", "j":"j.png", "k":"k.png", "l":"l.png", "m":"m.png", "n":"n.png", "o":"o.png", "p":"p.png", "q":"q.png", "r":"r.png", "s":"s.png", "t":"t.png", "u":"u.png", "v":"v.png", "w":"w.png", "x":"x.png", "y":"y.png", "z":"z.png", "?":"question-mark.png", "!":"exclamation-mark.png", ".":"full-stop.png", ",":"comma.png", "'":"apostrophe.png", chr(45):"dash.png", chr(8212):"dash.png", "(":"left-bracket.png", ")":"right-bracket.png"}

letter_images = {" ":[[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]}

for key, value in letter_files.items():
  im = Image.open(f"letter-images/{value}")
  pixels = list(im.getdata())
  new_pixels = []
  for i in range(0, len(pixels), 6):
    new_pixels.append(pixels[i:(i+6)])
  letter_images[key] = new_pixels


for filename in f:
  file = open(f'word-files/{filename}', 'r')

  text_to_translate = ""
  for line in file.readlines():
      text_to_translate = text_to_translate + line.strip().lower() + " "
  text_to_translate = text_to_translate.replace(chr(45), "-")
  print(filename)
  print(len(text_to_translate))
  black = [0,0,0]
  white = [255,255,255]
  img_list = []
  n = 45
  j = 0
  while j < len(text_to_translate) - 1:
    for i in range(10):
      l = j
      row = []
      for k in range(n):
        if l <= len(text_to_translate)-1:
          try:
            row_colours = letter_images[text_to_translate[l]][i]
            for x in row_colours:
              if x == 0:
                row.append(random.choice(colours))
              else:
                row.append(white)
          except:
            print(ord(text_to_translate[l]))
        else:
          for x in range(6):
            row.append(random.choice(colours))
        l+=1
      img_list.append(row)
    j+=n

  arr = np.array(img_list)
  im_out = Image.fromarray(arr.astype('uint8')).convert('RGB')
  im_out.save(f"images-out/{filename[:-4]}.png")

