import subprocess
import pandas as pd
import os
from pathlib import Path

def getData(dest: str, user: bool = False, file: str = None, start: str = None, end: str = None, keywords: str = None) -> None:

    if user:
        f = pd.read_csv(file)
        usr_ids = f['author.id'].to_list()
        usrnames = f['author.username'].to_list()
        print(len(usrnames), len(usr_ids))
        # twarc2 following 1383732403559014406 R.jsonl

        for i in range(len(usr_ids)):
            print("Scrapping ", usr_ids[i],  str(usrnames[i]))
            my_file = Path(dest +  str(usrnames[i]) + ".jsonl")
            if my_file.exists():
                print(str(usrnames[i]) + " exists, skipping")
                continue
            else:
                s = "from:" + str(usr_ids[i])
                fname = dest +  str(usrnames[i]) + ".jsonl"
                subprocess.run(["twarc2", "search", "--archive", "--start-time", start, "--end-time", end, s, fname,])

    else:
        #default to keyword search
        s = keywords
        fname = dest +  keywords + ".jsonl"
        subprocess.run(["twarc2", "search", "--archive", "--start-time", start, "--end-time", end, s, fname,])

    
def main():
    getData(dest= "/Users/sheyrilagarwal/Desktop", user = False, file = None, start = None, end = None, keywords = "#Metoo")



if __name__ == "__main__":
    main()