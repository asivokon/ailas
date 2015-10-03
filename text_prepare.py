#!/usr/bin/env python3.5

import re
from pymystem3.mystem import Mystem



analizer = Mystem()
text = " \
Як умру, то поховайте \
Мене на могилі \
Серед степу широкого \
На Вкраїні милій, \
Щоб лани широкополі, \
І Дніпро, і кручі \
Було видно, було чути, \
Як реве ревучий. \
Як понесе з України \
У синєє море \
Кров ворожу... отойді я \
І лани і гори — \
Все покину, і полину \
До самого Бога \
Молитися... а до того \
Я не знаю Бога. \
Поховайте та вставайте, \
Кайдани порвіте \
І вражою злою кров’ю \
Волю окропіте. \
І мене в сем’ї великій, \
В сем’ї вольній, новій, \
Не забудьте пом’янути \
Незлим тихим словом. \
"

def text_prepare(text):
    text = text.lower()
    pattern = r"[а-яА-ЯґҐЇїіІєЄ'’]+"
    pattern_exp = re.compile(pattern, re.MULTILINE & re.LOCALE)
    return pattern_exp.findall(text)

print(text_prepare(text))
