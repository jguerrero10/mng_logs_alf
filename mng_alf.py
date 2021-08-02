from datetime import datetime, timedelta
from os import remove, path

date = datetime.now()
print(f"{date} Se ejecuta el programa")
archivo = "localhost_access_log"
logs_alf_path = "/opt/alfresco-community/tomcat/logs"

for i in range(1,3):    
    dia = (date + timedelta(days=-i)).strftime('%Y-%m-%d')
    file = f"{logs_alf_path}{archivo}{dia}.txt"
    if path.exists(file):
        remove(file)
        print(f"{date} Se borra el archivo {file}")
    else:        
        print(f"{date} No found File {file}")




