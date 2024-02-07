import os
import shutil



#mini project that cleans my desktop
#As u can see this code is very messy because i tried my best

# for i in EXCEL_ls:
#     print(i)
#     excel_files.extend([file for file in files_on_desktop if file.endswith(f".{i}")])


# for i in TXT_ls:
#     print(i)
#     txt_files.extend([file for file in files_on_desktop if file.endswith(f".{i}")])

# for i in zdj_ls:
#     print(i)
#     zdj_files.extend([file for file in files_on_desktop if file.endswith(f".{i}")])

def move_file(extention,nazwa_pliku):
    
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    files_on_desktop = os.listdir(desktop_path)
    print(files_on_desktop)
    lista = []
    for i in extention:
        print(i)
        lista.extend(file for file in files_on_desktop if file.endswith(f".{i}"))
    decyzja = input(f"{lista} Czy przenieść pliki do folderu {nazwa_pliku}: T lub N?: ")
    # nazwa_pliku = input(f"do jakiego pliku chcesz przenieść?").lower

    if decyzja == "T":
        for file in lista:
            src_path = os.path.join(desktop_path,file)
            dst_path = os.path.join(desktop_path,nazwa_pliku, file)  
            shutil.move(src_path, dst_path)

excel_files= ['xlsx', 'xls',"XLSX","xlsb","xlsm",".csv"]
pdf_files = ["pdf","PDF"]
txt_files = ["txt","docx"]
apki_files = ['deb']
zdj_files = ["jpg", "png", "gif", "bmp","jpeg"]


move_file(txt_files,"txt_files")


