import tabula
import csv

def convert_pdf_to_csv(filename,source_path,target_path):
    source_file=source_path + '/' + filename +'.pdf'
    target_file=target_path + '/' + filename +'.csv'
    res=tabula.convert_into(source_file, target_file, output_format="csv", pages='all')
    return None

def all_purchase_stocks(target_path,filename):
    target_file=target_path + '/' + filename +'.csv'
    allstk=set()
    with open(target_file,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row[0].split(" "))>=2:
                if row[0].split(" ")[1]=='B' and row[5]!='':
                    allstk.add(row[5])
                elif row[0].split(" ")[1]=='S' and row[5]!='':
                    allstk.add(row[5])
    return allstk

def clean_csv(target_path,filename,format_ext):
    target_file_unformat=target_path + '/' + filename +'.csv'
    target_file_format=target_path + '/' + filename + format_ext + '.csv'
    lst=[]
    stock_list=all_purchase_stocks(target_path,filename)
    with open(target_file_unformat,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[5] in stock_list:
                lst.append([row[5],row[0].split(" ")[2],row[0].split(" ")[1],row[2],row[6]])
            if row[2] in stock_list:
                lst.append([row[2],row[0].split(" ")[2],row[0].split(" ")[1],row[1].split(" ")[1],row[6]])
    with open(target_file_format, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(lst)
    return None

def open_file(target_path,filename):
    target_file_format=target_path + '/' + filename + '.csv'
    with open(target_file_format,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    return None
