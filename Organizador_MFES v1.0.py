from os import path, mkdir, listdir, rename

# Identify current route
rutaActual = path.dirname(path.abspath(__file__))

# Correct the path in windows
def formatearRuta(ruta):
    clean = ""
    for caracter in ruta:
        if caracter == '\\':
            clean = clean + '/'
        else:
            clean = clean + caracter
    return clean
folderParaOrganizar = formatearRuta(rutaActual) + "/"

# New paths to organize files
folderOrganizado = folderParaOrganizar + 'Archivos_Organizados'
folderOrganizado_images = folderParaOrganizar + 'Archivos_Organizados/IMAGENES'
folderOrganizado_audios = folderParaOrganizar + 'Archivos_Organizados/AUDIO'
folderOrganizado_videos = folderParaOrganizar + 'Archivos_Organizados/VIDEOS'
folderOrganizado_word = folderParaOrganizar + 'Archivos_Organizados/WORD'
folderOrganizado_excel = folderParaOrganizar + 'Archivos_Organizados/EXCEL'
folderOrganizado_powerPoint = folderParaOrganizar + 'Archivos_Organizados/POWER_POINT'
folderOrganizado_pdf = folderParaOrganizar + 'Archivos_Organizados/PDF'
folderOrganizado_rar = folderParaOrganizar + 'Archivos_Organizados/RAR'
folderOrganizado_exe = folderParaOrganizar + 'Archivos_Organizados/EXE'
folderOrganizado_apk = folderParaOrganizar + 'Archivos_Organizados/APK'
folderOrganizado_txt = folderParaOrganizar + 'Archivos_Organizados/TXT'
folderOrganizado_web = folderParaOrganizar + 'Archivos_Organizados/WEB'

# File extensions
extensionImagenes = ['.jpg','.jpeg','.png','.gif','.webp','.ico','.svg']
extensionAudio =  ['.mp3','.ogg','.wav','.flac']
extensionVideos = ['.mp4','.avi','.mkv','.flv','.mov']
extensionWord = ['.doc','.docx','.docm','.odt','.rtf']
extensionExcel = ['.xlsx','.xlsm','.xlsb','.xltx','.xls','.xltm','.csv','.tsv','.ods']
extensionPowerPoint = ['.pptx','.pptm','.ppt','.potx','.potm','.pot','.ppsx','.ppsm','.pps','.ppam','.ppa','.odp']
extensionPdf = ['.pdf','.epub']
extensionRar = ['.rar','.zip','.7z','.tar','.gzip','.bzip2']
extensionExe = ['.exe','.msi','.appx','.iso']
extensionApk = ['.apk','.apkx']
extensionTxt = ['.txt']
extensionWeb = ['.html','.css','.xml','.js','.php']

# Create folders to organize
def create_folders():
    if not path.exists(folderOrganizado):
        mkdir(folderOrganizado)
    if not path.exists(folderOrganizado_images):
        mkdir(folderOrganizado_images)
    if not path.exists(folderOrganizado_audios):
        mkdir(folderOrganizado_audios)
    if not path.exists(folderOrganizado_videos):
        mkdir(folderOrganizado_videos)
    if not path.exists(folderOrganizado_word):
        mkdir(folderOrganizado_word)
    if not path.exists(folderOrganizado_excel):
        mkdir(folderOrganizado_excel)
    if not path.exists(folderOrganizado_powerPoint):
        mkdir(folderOrganizado_powerPoint)
    if not path.exists(folderOrganizado_pdf):
        mkdir(folderOrganizado_pdf)
    if not path.exists(folderOrganizado_rar):
        mkdir(folderOrganizado_rar)
    if not path.exists(folderOrganizado_exe):
        mkdir(folderOrganizado_exe)
    if not path.exists(folderOrganizado_apk):
        mkdir(folderOrganizado_apk)
    if not path.exists(folderOrganizado_txt):
        mkdir(folderOrganizado_txt)
    if not path.exists(folderOrganizado_web):
        mkdir(folderOrganizado_web)

# It is repeated as long as the user does not choose the exit option
estado = True
while estado:
    print(''.center(52,'_'))
    print('|'+''.center(50,'#')+'|')
    print('|'+' ORGANIZADOR MFES v1.0.0 '.center(50,'#')+'|')
    print('|'+''.center(50,'#')+'|')
    print('|'+'1| Organizar Archivos'.ljust(50,' ')+'|')
    print('|'+'0| Salir'.ljust(50,' ')+'|')
    print(''.center(52,'¯'))
    option = input('>>> ')
    
    if option == '1':
        create_folders()

        # Loop through each file in the folder to sort
        for filename in listdir(folderParaOrganizar):
            print(filename)
            name, extension = path.splitext(folderParaOrganizar + filename)

            #IMG
            if extension in extensionImagenes:
                rename(folderParaOrganizar + filename, folderOrganizado_images + '/' + filename)
                
            #AUD
            if extension in extensionAudio:
                rename(folderParaOrganizar + filename, folderOrganizado_audios + '/' + filename)
                
            #MOV
            if extension in extensionVideos:
                rename(folderParaOrganizar + filename, folderOrganizado_videos + '/' + filename)
                
            #WORD
            if extension in extensionWord:
                rename(folderParaOrganizar + filename, folderOrganizado_word + '/' + filename)
                
            #EXCEL
            if extension in extensionExcel:
                rename(folderParaOrganizar + filename, folderOrganizado_excel + '/' + filename)
                
            #POWER POINT
            if extension in extensionPowerPoint:
                rename(folderParaOrganizar + filename, folderOrganizado_powerPoint + '/' + filename)
                
            #PDF
            if extension in extensionPdf:
                rename(folderParaOrganizar + filename, folderOrganizado_pdf + '/' + filename)
                
            #RAR
            if extension in extensionRar:
                rename(folderParaOrganizar + filename, folderOrganizado_rar + '/' + filename)
                
            #EXE
            if extension in extensionExe:
                rename(folderParaOrganizar + filename, folderOrganizado_exe + '/' + filename)
            #APK
            if extension in extensionApk:
                rename(folderParaOrganizar + filename, folderOrganizado_apk + '/' + filename)
                
            #TXT
            if extension in extensionTxt:
                rename(folderParaOrganizar + filename, folderOrganizado_txt + '/' + filename)
                
            #WEB
            if extension in extensionWeb:
                rename(folderParaOrganizar + filename, folderOrganizado_web + '/' + filename)
                
        print('\nArchivos organizados correctamente.')
    
    elif option == '0':
        # End of loop
        estado = False
    else:
        print('\nOpción Inválida. Intente de nuevo')