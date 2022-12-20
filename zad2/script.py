import matplotlib.colors as colors
import csv
import json
import os
import pandas as pd
import boto3

def lambda_handler(event, context):

    main_df = pd.DataFrame()

    for file in os.listdir(os.getcwd()):
        if file.endswith('.csv'):
            main_df = main_df.append(pd.read_csv(file))

    main_df.to_csv('colors.csv', index=False)

    df = pd.read_csv('colors.csv')
    colors_rgb = []
    hex_value = df['value'].tolist()
    
    for i in hex_value:
        new_i = colors.hex2color(i)
        rgb.append(new_i)

    df['rgb'] = colors_rgb 

    df.to_csv('colors.csv') 

    targetbucket = 'Bucket1'
    csvkey = 'colors.csv'
    jsonkey = 'color.json'

    s3 = boto3.resource('s3')
    csv_object = s3.Object(targetbucket, csvkey)
    csv_content = csv_object.get()['Body'].read().splitlines()
    s3_client = boto3.client('s3')
    l=[]

    for line in csv_content:
        x = json.dumps(line.decode('utf-8')).split(',')
        colorname = str(x[1])
        hex = str(x[2])
        rgb = str(x[3])
        y = '{ "Color name": ' + colorname + '"' + ',' + ' "Hex":' + '"' + hex + '"' + ',' + ' "RGB":' + '"' + rgb + '"' + '}'
        
        l.append(y)

    s3_client.put_object(
        Bucket=targetbucket,
        Body = str(l).replace("'",""),
        Key = jsonkey,
        ServerSideEncryption= 'AES256'
    )
