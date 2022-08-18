#1 Importing the CSV module
import streamlit as st
import csv
from numpy import tile

file_name= st.text_input(label="Enter the name of csv(without csv):")
#2 Opening or creating the file
col_names=st.text_input(label="Enter col names(Seperated by commas):",help="Sperated column names with commas(',')")
col_lst=col_names.split(",")

#Creating a csv file with coulmn names 
with open(file_name+".csv", 'w', newline="") as file:
    myFile = csv.writer(file)
    myFile.writerow(col_lst)

    #5 Getting the number of rows to add   
    noOfEducationLevels = st.number_input("Enter numbers of rows you will enter.")

#6 Using for loop to write user input to the file   
    for i in range(int(noOfEducationLevels)):
        row =[]
        col_cnt=1
        for j in range(len(col_lst)):
            v=st.text_input(f"Enter the value for Row:- `{i}`, for column:- `{col_lst[j]}`")
            col_cnt+=1
            row.append(v)    
        myFile.writerow(row)
        st.success("File saved on local directory.")