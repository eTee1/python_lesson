txt = """“Любіть Україну, як сонце любіть,

як вітер, і трави, і води...

В годину щасливу і в радості мить,

любіть у годину негоди.



Любіть Україну у сні й наяву,

вишневу свою Україну,

красу її, вічно живу і нову,

і мову її солов'їну.



Без неї — ніщо ми, як порох і дим,

розвіяний в полі вітрами...

Любіть Україну всім серцем своїм

і всіми своїми ділами.”"""

txt_r = txt.replace(",", "").replace(".", "").replace("'", "")\
    .replace("”", "").replace("“", "").replace("—", "").lower().split()
print(txt_r)  # #удалил знаки, всё в нижний регистр, создал список

dict_1 = {x: txt_r.count(x) for x in txt_r}  # #словарь для счета слов
print(dict_1)
print('Слово встречающееся больше всего: ', max(dict_1, key=dict_1.get))
print('Слово меньше чаще всего:', min(dict_1, key=dict_1.get))
