text = """Потанцуем крабика.
		Я хочу до клабика, там танцуют крабика.
		А чо, пойдём до клабика, потанцуем крабика.
		Я хочу до клабика, там танцуют крабика.
		А чо, пойдём до клабика, потанцуем крабика.

		Все дойдём до клабика, потанцуем крабика.
		Все дойдём до клабика, потанцуем крабика.
		Все дойдём до клабика, потанцуем крабика.
		Все дойдём до клабика, потанцуем крабика."""

text = text.lower()
signs = [',', '.']

for sign in signs:
	if sign in text:
		text = text.replace(sign, ' ')
		
text = text.split()

fr = {}

for el in text:
	if el not in fr:
		fr[el] = 0
	fr[el] += 1	

key = list(fr.keys())
value = list(fr.values())
inv_fr = {k:v for k,v in zip(value, key)}

most_fr_word = max(inv_fr.keys())
most_fr_word = inv_fr[most_fr_word]
print(f'Наиболее часто встречающееся слово в тексте: "{most_fr_word}"')
