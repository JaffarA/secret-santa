# secret santa
secret santa selector program 🎅

## Objectives

a python program that will generate double blind secret santa matches based on a TXT file input

## fun

this program initially used a different algorithim for selection, simply using the random choice function of python to make selections of gift givers, but i found a problem with that, being that a person could be left out using that algorithim.

the past algorithim to the pool was:

```python
participant_list = ['A', 'B', 'C']
receiver_list = copy(participant_list)

for participant in participant_list:

    possible_receivers = receiver_list.remove(participant) 
    # remove the participant from the list so that our participant could not match with themselves

    match = choice(possible_receivers) 
    # select a random participant as our match using python's random.choice

    receiver_list.remove(match) 
    # remove that participant from the list as they've already found a secret santa 😉-🎅

```

take this example:

```python
>>> people_pool = ['A', 'B', 'C']
>>> people_pool
['A', 'B', 'C']
>>> receiver_pool = people_pool[::-1] # shallow copy
>>> receiver_pool
['A', 'B', 'C']
>>> for person in people_pool:
...     possible_receivers = receiver_pool.remove(person)
...     match = choice(possible_receivers)
...     receiver_pool.remove(match)

# runs

# 1
person  # A
possible_receivers  # ['A', 'B', 'C'] -> remove self from receiver list -> ['B', 'C']
match  # ['B', 'C'] -> 'B' is chosen 
receiver_pool  # ['A', 'B', 'C'] -> remove choice from receiver list -> ['A', 'C']

# 2
person  # B
possible_receivers  # ['A', 'C'] -> remove self from receiver list (we are not in it) -> ['A', 'C'] 
match  # ['A', 'C'] -> 'A' is chosen 
receiver_pool  # ['A', 'C'] -> remove choice from receiver list -> ['C']

# 3
person  # C
possible_receivers  # ['C'] -> we are the only possible receiver, since: A => B; B => A -> we remove ourself from the pool -> []
match  # [] -> the list is empty and we cannot make a match 
receiver_pool  # [] -> we have no match, and probably error out of range index
```

this algorithim worked (most of the time, depending on N (number of participants)) but i wanted something that would work 100% of the time with no bugs to have to think about. the new algorithim which i use instead is much simpler and doesnt have this problem. (see santa.py)

## Installation

Install Python if you dont already have it

[Python](https://www.python.org/downloads/)

Clone the git repo

```bash
git clone https://github.com/JaffarA/secret-santa.git
```

Install the requirements

```bash
pip install -r requirements.txt
```

## Usage

Modify the participants.txt file with all your participants separated with newlines

```csv
a
b
c
```

You can use the program with

```bash
python santa.py
```

Then you can check the 'THIS PROJECT/matches' dir for your match files


### NOTE: these files are just .txt files with the match's name, if you want to run a true anonymous secret santa, i recommend you dont open them 😊


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## FAQ

If any questions are ever asked, they will be answered here. 🙋

## License
[GPL-3](https://choosealicense.com/licenses/gpl-3.0/)
