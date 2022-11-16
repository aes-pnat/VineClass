from os import listdir
from os.path import isfile, join, abspath
import random

def generate():
    mypath = abspath(__file__).split('DatasetGenerator.py')[0]
    healthy_path = f'{mypath}Grape\\Grape___healthy'
    blackrot_path = f'{mypath}Grape\\Grape___Black_rot'
    esca_path = f'{mypath}Grape\\Grape___Esca_(Black_Measles)'
    blight_path = f'{mypath}Grape\\Grape___Leaf_blight_(Isariopsis_Leaf_Spot)'

    healthy = [f'{healthy_path}\\{f}' for f in listdir(healthy_path) if f.lower().endswith(('.jpg', '.png', 'jpeg'))]
    blackrot = [f'{blackrot_path}\\{f}' for f in listdir(blackrot_path) if f.lower().endswith(('.jpg', '.png', 'jpeg'))]
    esca = [f'{esca_path}\\{f}' for f in listdir(esca_path) if f.lower().endswith(('.jpg', '.png', 'jpeg'))]
    blight = [f'{blight_path}\\{f}' for f in listdir(blight_path) if f.lower().endswith(('.jpg', '.png', 'jpeg'))]

    healthy_dict = {key:'0001' for key in healthy}
    blackrot_dict = {key:'0010' for key in blackrot}
    esca_dict = {key:'0100' for key in esca}
    blight_dict = {key:'1000' for key in blight}

    total_data = dict()
    total_data.update(healthy_dict)
    total_data.update(blackrot_dict)
    total_data.update(esca_dict)
    total_data.update(blight_dict)

    temp = list(zip(total_data.keys(), total_data.values()))
    random.shuffle(temp)
    res1, res2 = zip(*temp)
    res1, res2 = list(res1), list(res2)
    
    import pandas as pd  
        
    table = {'image': res1, 'output': res2}  
        
    df = pd.DataFrame(table) 
    df.to_csv('in_out.csv') 

if __name__ == '__main__':
    generate()



