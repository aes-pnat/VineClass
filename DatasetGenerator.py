from os import listdir
from os.path import isfile, join, abspath
import random

import shutil
import pandas as pd 
import os



def generate():
    mypath = abspath(__file__).split('DatasetGenerator.py')[0]
    healthy_path = f'{mypath}dataset\\Grape\\Grape___healthy'
    blackrot_path = f'{mypath}dataset\\Grape\\Grape___Black_rot'
    esca_path = f'{mypath}dataset\\Grape\\Grape___Esca_(Black_Measles)'
    blight_path = f'{mypath}dataset\\Grape\\Grape___Leaf_blight_(Isariopsis_Leaf_Spot)'

    healthy = [f'{healthy_path}\\{f}' for f in listdir(healthy_path) if f.lower().endswith(('.jpg', '.png', 'jpeg'))]
    blackrot = [f'{blackrot_path}\\{f}' for f in listdir(blackrot_path) if f.lower().endswith(('.jpg', '.png', 'jpeg'))]
    esca = [f'{esca_path}\\{f}' for f in listdir(esca_path) if f.lower().endswith(('.jpg', '.png', 'jpeg'))]
    blight = [f'{blight_path}\\{f}' for f in listdir(blight_path) if f.lower().endswith(('.jpg', '.png', 'jpeg'))]

    healthy_dict = {key:'healthy' for key in healthy}
    blackrot_dict = {key:'blackrot' for key in blackrot}
    esca_dict = {key:'esca' for key in esca}
    blight_dict = {key:'blight' for key in blight}

    total_data = dict()
    total_data.update(healthy_dict)
    total_data.update(blackrot_dict)
    total_data.update(esca_dict)
    total_data.update(blight_dict)

    temp = list(zip(total_data.keys(), total_data.values()))
    random.shuffle(temp)
    res1, res2 = zip(*temp)
    res1, res2 = list(res1), list(res2)
    table = {'image': res1, 'output': res2}  
        
    df = pd.DataFrame(table) 
    df.to_csv('in_out.csv') 

def train_splitter(train_perc, validate_perc=0):
    # Splits the generated CSV into train, validation and test
    # as defined by the ratio tuple
    
    if(train_perc <= 0 and train_perc >= 1 and validate_perc <= 0 and validate_perc >= 1):
        raise Exception("Invalid percentages input")

    mypath = abspath(__file__).split('DatasetGenerator.py')[0]
    data = pd.read_csv('in_out.csv').values.tolist()
    
    if not os.path.isdir("cooked_dataset"):
        os.makedirs("cooked_dataset")
        os.makedirs("cooked_dataset\\train")
        os.makedirs("cooked_dataset\\val")
        os.makedirs("cooked_dataset\\test")

        for w in ['healthy','blackrot','esca','blight']:
            os.makedirs(f'cooked_dataset\\train\\{w}')
            os.makedirs(f'cooked_dataset\\val\\{w}')
            os.makedirs(f'cooked_dataset\\test\\{w}')

    else:
        shutil.rmtree("cooked_dataset", ignore_errors=True)

        os.makedirs("cooked_dataset")
        os.makedirs("cooked_dataset\\train")
        os.makedirs("cooked_dataset\\val")
        os.makedirs("cooked_dataset\\test")

        for w in ['healthy','blackrot','esca','blight']:
            os.makedirs(f'cooked_dataset\\train\\{w}')
            os.makedirs(f'cooked_dataset\\val\\{w}')
            os.makedirs(f'cooked_dataset\\test\\{w}')
    #shutil.copyfile(src, dst)

    s = len(data)
    test_perc = 1 - train_perc - validate_perc
    print(data[10])
    for f in data:
        if(f[0] < train_perc*s):
            #train
            shutil.copy(f[1], f'{mypath}cooked_dataset\\train\\{f[2]}')
        elif(f[0] < train_perc*s + validate_perc*s):
            #validate
            shutil.copy(f[1], f'{mypath}cooked_dataset\\val\\{f[2]}')
        else:
            #test
            shutil.copy(f[1], f'{mypath}cooked_dataset\\test\\{f[2]}')





