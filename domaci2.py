# -*- coding: utf-8 -*-
recnik = {"love": {"sinonimi": ["adulation", "amour"], "antonimi":["dislike", "hate"]}, "sleep":{"sinonimi":["bedtime", "coma"], "antonimi":["awakeing", "wakefulness"]}, "sad":{"sinonimi":["bereaved", "bitter"], "antonimi":["cheerful", "glad"]}}


print(recnik["love"]["sinonimi"])
print(recnik["love"]["antonimi"])
print(recnik["sleep"]["sinonimi"])
print(recnik["sleep"]["antonimi"])
print(recnik["sad"]["sinonimi"])
print(recnik["sad"]["antonimi"])

print(recnik["love"]["antonimi"][0])
print(recnik["sad"]["sinonimi"][1])
print(recnik["sleep"]["antonimi"][0])


