import requests

TOKEN = '7724702440:AAEspL7SQhV_crexoooMHzeePaq5Y1sZH_I'  # Substitua pelo token do seu bot
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url)
data = response.json()

# O chat ID estará disponível no JSON, veja nos itens a seguir
print(data)
