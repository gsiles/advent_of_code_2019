import requests
import os

def get_puzzle_input(day, session_id):
    url = f"https://adventofcode.com/2019/day/{day}/input"
    headers = {"cookie" : f"session={session_id}"}
    r = requests.get(url, headers=headers)

    if not os.path.exists(f"./day{day}"):
        os.mkdir(f"./day{day}")

    try:
        file = open(f"./day{day}/puzzle_input.txt","xt")
        file.write(r.text)
        file.close()
    except FileExistsError:
        print("There is already a puzzle input for this day. Do you wish to overwrite it? Y/N:")
        answer = input()
        if answer=="Y" or answer=="y":
            try:
                file = open(f"./day{day}/puzzle_input.txt","wt")
                file.write(r.text)
                file.close()
            except:
                raise
