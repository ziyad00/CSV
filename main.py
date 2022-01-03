from typing import Optional
import pandas as pd
from fastapi import FastAPI, File, UploadFile
import csv

app = FastAPI()


@app.post("/")
async def read_root(assignment_file: UploadFile = File(...)):
    csv_reader = pd.read_csv(assignment_file.file)

    csv = csv_reader.to_csv().split('\n')
    cars = []
    line_count = 0
    columns = csv
    #print(csv)

    for row in csv:
        if line_count != 0:
            cars.append(row)
        line_count+=1
    best_average = cars[0].split(',')
    for i in cars:
        i = i.split(',')
        

        if (len(i)>2):
            if float(i[3]) > float(best_average[3]):
               best_average = i
    print(best_average)
    return {"top_product": best_average[2], "best_average":best_average[3].split('\r')[0]}


