# Write a program to read through the mbox-short.txt and figure out who has sent the greatest
# number of mail messages. The program looks for 'From ' lines and takes the second word of those
# lines as the person who sent the mail. The program creates a Python dictionary that maps the
# sender's mail address to a count of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a maximum loop to find
# the most prolific committer.

# handle = open(r"..\..\text_files\mbox-short.txt")

name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

senders = dict()
max_sender = None
sender_count = None


for line in handle:
    if line.startswith("From "):
        sender = line.split()
        senders[sender[1]] = senders.get(sender[1], 0) + 1

for email, count in senders.items():
    if sender_count == None or sender_count < count:
        max_sender = email
        sender_count = count


print(max_sender, sender_count)