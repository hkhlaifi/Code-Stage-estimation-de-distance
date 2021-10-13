'''
Purpose: Generates csv file of annotations from .txts
'''
import pandas as pd
import os
from tqdm import tqdm
import argparse

argparser = argparse.ArgumentParser(description='Generate annotations csv file from .txts')
argparser.add_argument('-i', '--input',
                       help='path du fichier annotations en sortie de yolo')
argparser.add_argument('-o', '--output',
                       help='nom du fichier de sortie')

args = argparser.parse_args()

# parse arguments
INPUTDIR = args.input
FILENAME = args.output

df = pd.DataFrame(columns=['filename','xmin', 'ymin', 'xmax', 'ymax','zloc'])

print(df)

def assign_values(filename, idx, list_to_assign):
    df.at[idx, 'filename'] = filename
    print(idx)   
    df.at[idx, 'xmin'] = list_to_assign[1]
    df.at[idx, 'ymin'] = list_to_assign[2]
    df.at[idx, 'xmax'] = list_to_assign[3]
    df.at[idx, 'ymax'] = list_to_assign[4]
    df.at[idx, 'zloc'] = list_to_assign[5]

all_files = sorted(os.listdir(INPUTDIR))
pbar = tqdm(total=len(all_files), position=1)

count = 0
for idx, f in enumerate(all_files):
    pbar.update(1)
    file_object = open(INPUTDIR + f, 'r')
    print(file_object)
    file_content = [x.strip() for x in file_object.readlines()]

    for line in file_content:
        elements = line.split()
        if elements[0] == 'DontCare':
            continue

        assign_values(f, count, elements)
        count += 1

df.to_csv(FILENAME, index=False)
