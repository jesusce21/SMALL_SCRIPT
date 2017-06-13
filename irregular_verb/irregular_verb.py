# -*- coding: utf-8 -*-

import random
import json

with open('verb.json') as json_data:
    irregular_verb = json.load(json_data)

struct = ["infinitive", "past_simple", "past_participle", "translation"]

def check_value(num_random, typ_value):
	val = raw_input("%s: " % typ_value)
	print(val)
	content = irregular_verb[num_random][typ_value].lower()
	l_content = content.split("/")
	if(len(l_content)<1):
		l_content=list(content)
	if(val.lower() in l_content):		
		print("\x1b[1A\x1b[32mCORRECT '%s'\x1b[0m" % (content)) 
		return 1
	else:
		print("\x1b[1A\x1b[31mERROR: \x1b[9m'%s'\x1b[0m\x1b[31m'%s'\x1b[0m" % (val, content))
		return 0


loop_number = int(input("Introduce el número de verbos: "))
count = 0

aciertos = 0

while(count < loop_number):
	num_random = random.randint(1, len(irregular_verb)-1)
	num_t_struct = random.randint(1, len(struct)-1)
	t_struct = struct[num_t_struct]
	print("The %s is: %s " % (t_struct, irregular_verb[num_random][t_struct]))
	for key in struct:
		if key != t_struct:
			aciertos+=check_value(num_random, key)
	count+=1

por_acierto=(aciertos/(loop_number*3.0))*100

if(por_acierto>80):
	color_acert = "\x1b[32m%s%%\x1b[0m" % por_acierto
elif (por_acierto>50):
	color_acert = "\x1b[33m%s%%\x1b[0m" % por_acierto
else:
	color_acert = "\x1b[31m%s%%\x1b[0m" % por_acierto

print("Has acertado el {0} de {1} verbos ({2} posibilidades)".format(color_acert, loop_number, loop_number*3))