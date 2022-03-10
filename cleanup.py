import csv
import re


def cleanup(input_row):


    item_type = input_row[18]
    for i in input_row:
        i =  re.sub(r'<a.*?>|</a> ', '', i)
        i  = re.sub(r'<\/LI><LI>', '\.', i)
        i  = re.sub(r'<.*?>', '', i)
    return_str = ""

    return_str += "The product Name is " +  input_row[1] + ".\n"
    return_str += "The product category  is" +  input_row[2] + ".\n"
    return_str +=  "The price is  " +   input_row[3] + ".\n"
    return_str += "The average customer rating is " +  input_row[4] + ".\n"
    for item in input_row[5].split(','):
       item =  re.sub(r'<a.*?>|</a> ', '', item)
       item = re.sub(r'<\/LI><LI>', '\.', item)
       item = re.sub(r'<.*?>', '', item)
       return_str += item + ".\n"
       
    return_str += "The color is " +  input_row[6] + ".\n"
    return_str += "The color group is " +  input_row[7] + ".\n"

    return_str += "The size is " +  input_row[8] + ".\n"
    return_str += "The gender is " +  input_row[9] + ".\n"
    return_str += "The item type is " +  input_row[11] + ".\n"
    for item in input_row[12].split(','):
       item =  re.sub(r'<a.*?>|</a> ', '', item)
       item = re.sub(r'<\/LI><LI>', '\.', item)
       item = re.sub(r'<.*?>', '', item)
       return_str += "It has " + item + ".\n"
    return_str += "The category is " +  input_row[13] + ".\n"
    return_str += "The condition is " +  input_row[14] + ".\n"
    for item in input_row[15].split(','):
       item =  re.sub(r'<a.*?>|</a> ', '', item)
       item = re.sub(r'<\/LI><LI>', '\.', item)
       item = re.sub(r'<.*?>', '', item)
       return_str += "It is " + item + ".\n"
    return_str += "The item is designed for " +  input_row[16] + ".\n"
    return_str += "The item type is  " +  input_row[18] + ".\n"
    return_str += "The item type is  " +  input_row[19] + ".\n"
    return_str += "The fit is  " +  input_row[20] + ".\n"
    input_row[20]  = re.sub(r'<\/LI><LI>', '.\n', input_row[20])
    input_row[20]  = re.sub(r'<.*?>', '', input_row[20])
    for item in input_row[21].split('.'):
       item  = re.sub(r'<\/LI><LI>', '.\n', item)
       item  = re.sub(r'<.*?>', '', item)
       return_str += "It is " + item + ".\n"
    return return_str



