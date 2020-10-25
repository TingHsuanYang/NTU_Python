from urllib.request import urlopen
import bs4


def dreye_dict(word):
  html = urlopen("http://yun.dreye.com/dict_new/dict.php?w=%s" % word).read().decode("utf-8")
  bs = bs4.BeautifulSoup(html, "html.parser")

  usualExps = bs.select(".sg.block")[0]

  # delete all .exp node
  [e.extract() for e in usualExps.select(".exp")]

  return usualExps.getText().strip()


word=input('word:')
print(dreye_dict(word))

'''
print(dreye_dict("understand"))
Output:
vt.[W]
理解；懂；熟諳[+wh-]
認識到；了解[+wh-][+（that）]
據聞，獲悉[+（that）][O2]
認為；推斷[+（that）]
將……理解為[+（that）][O2]
將……看作不言自明；省略[H]
vi.[W]
理解；懂得
熟悉[（+about）]
'''
