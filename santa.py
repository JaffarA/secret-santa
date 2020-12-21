from random import choice
from numpy.random import shuffle
from os.path import isdir
from os import mkdir
from shutil import rmtree


match_dir = 'matches'
rmtree(match_dir)
if not isdir(match_dir):
    mkdir(match_dir)

# participant file
f = open('participants.txt', 'r')

# participant list
participants = [i.strip('\n') for i in f.readlines()]

# shuffling
shuffle(participants)

# matches dict
matches = {}

# matching algorithim
size = len(participants)  # size = size of participants list
for i in range(0, size):
    if i == size - 1:  # if we are at the end of the participant list
        matches[participants[i]] = participants[0]  # match is first entry
    else:  # otherwise 
        matches[participants[i]] = participants[i + 1]  # match is next entry

# for double-blind matching (no-one knows who is matched with who)
# write to txt file for each match
for m in matches:
    with open(f"{match_dir}\{m}.txt", 'w') as f:
        f.write(matches[m])
