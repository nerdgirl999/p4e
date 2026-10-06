text = "X-DSPAM-Confidence:    0.8475"
find_start = text.find('0')
final_value = float(text[find_start:])
print(final_value)