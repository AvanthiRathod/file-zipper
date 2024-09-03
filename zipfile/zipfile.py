import zipfile

print('Zip Started...')

zip_files-zipfile.ZipFile('FileZip.zip','w')

zip_files.write('Filel.txt',compress_type-zipfile.ZIP_DEFLATED)

zip_files.write('File2.txt',compress_type=zipfile.ZIP_DEFLATED) zip_files.close()

print('Zip Completed...')

print('Unzip Started...')

unzip_files-zipfile.ZipFile('FileZip.zip','r')

unzip_files.extractall('Files')

print('Unzip completed..')

unzip_files.extract("Filel.cxn")