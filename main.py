import stock_main
filename='5NZ88447'
source_path='/Users/abuhura/Desktop'
target_path='/Users/abuhura/Desktop'
format_ext='output'
stock_main.convert_pdf_to_csv(filename,source_path,target_path)
print(stock_main.all_purchase_stocks(target_path,filename))
print(stock_main.clean_csv(target_path,filename,format_ext))
stock_main.open_file(target_path,filename+format_ext)