установиь python3
установить pip, если не установлен
склонировать репозиторий
положить в папку code/ файл creds.json

установить зависимости
pip.exe install google-api-python-client
pip.exe install oauth2client

скрипт принимает на вход .csv файлы, которые экспортирует CFX
в файле должны быть размечены названия образцов
скрипт проходится построчно, записывает ct каждого каналадля каждого образца
на выходи выдает строку в котороЙ
sample,a1FAM,a1HEX,a2FAM,a2HEX,...,...b1FAM,b1HEX,...

.csv файлы складывать в CFX_files/
оттуда они переносятся в архив
если в архиве уже есть файл с таким именем, то скрипт его пропустит

для запуска открыть powershell в папке code/
ввести
python.exe .\main.py


скрипт работает только с файлами .csv экспортированными из CFX, кроме них в дирректории ничего быть не должно
при экспорте файлов с CFX используются опции по умолчанию
для работы скрипта необходим интернет
