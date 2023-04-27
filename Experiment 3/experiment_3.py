import pandas as pd

# reading csv file
print("CSV FILE")
df = pd.read_csv("Iris.csv")
print(df.head())

# reading json file 
print("JSON FILE")
df1 = pd.read_json("iris.json")
print(df1.head())

# reading excel file
print("EXCEL FILE")
df2 = pd.read_excel("historical_data.xlsx")
print(df2.head())

# reading text file
print("TEXT FILE")
f = open("file.txt")
print(f.read())

# reading image file
import cv2
img = cv2.imread("image.jpg")
img2 = cv2.resize(img, (400,250))
cv2.imshow("eye", img2)
cv2.waitKey(0)

# reading zip file 
print("ZIP FILE")
from zipfile import ZipFile
file = "image.zip"
with ZipFile(file, 'r') as zip:
    zip.printdir()
    zip.extractall

# reading HTML file
print("HTML FILE")
from bs4 import BeautifulSoup
html_file = open("clock.php")
index = html_file.read()
print(index)


