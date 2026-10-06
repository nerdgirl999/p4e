# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
spam_value = None
total_value = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        find_start = line.find('0')
        string_value = line[find_start:].rstrip()
        float_value = float(string_value)
        total_value = total_value + float_value
        count += 1
        continue
print("Average spam confidence:", total_value/count)