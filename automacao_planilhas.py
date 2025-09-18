import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Autenticação com Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Abrindo planilha
sheet = client.open("Base de Dados").sheet1

# Lendo dados
dados = sheet.get_all_records()
print("Dados atuais:", dados)

# Inserindo novo dado
sheet.append_row(["Cliente X", "Produto Y", 1200])
print("Novo registro adicionado!")
