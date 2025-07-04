import sys
from antlr4 import *
from CompiladorLexer import CompiladorLexer
from CompiladorParser import CompiladorParser
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time

    # Caminho para o JSON com a KEY
SERVICE_ACCOUNT_FILE = "token.json"  
SCOPES = ["https://www.googleapis.com/auth/calendar"]

CALENDAR_ID = "testecompiladores01@gmail.com"




event = {
            'summary': 'Entrega compiladores',
            'start': {
                'dateTime': '2025-07-08T08:50:00-03:00',
                'timeZone': 'America/Recife',
            },
            'end': {
                'dateTime': '2025-07-08T10:30:00-03:00',
                'timeZone': 'America/Recife',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }


def iniciar(prog, service, calendar_id):
    for c in prog.com():
        avalie(c, service, calendar_id)
        
def avalie(com, service, calendar_id):
            if com.CRIAR():
                try:
                    nome = com.children[2].getText()
                    data_inicio = com.children[3].getText().split('-')
                    data_inicio = f"{data_inicio[2]}-{data_inicio[1]}-{data_inicio[0]}"
                    hora_inicio = com.children[4].getText()
                    data_termino = com.children[5].getText().split('-')
                    data_termino = f"{data_termino[2]}-{data_termino[1]}-{data_termino[0]}"
                    hora_termino = com.children[6].getText()

                    event['summary'] = nome
                    event['start']['dateTime'] = f"{data_inicio}T{hora_inicio}:00-03:00"
                    event['end']['dateTime'] = f"{data_termino}T{hora_termino}:00-03:00"

                    created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
                    print(f"Event created: {created_event.get('htmlLink')}")
                except Exception as e:
                    print(f"Erro ao criar o evento: {e}")

            elif com.DELETAR():
                try:

                    if com.NOME():
                        nome = com.children[2].getText().strip('"')

                        events_result = service.events().list(
                            calendarId=calendar_id,
                            q=nome,
                            singleEvents=True,
                            orderBy='startTime',
                            timeMin=datetime.datetime.utcnow().isoformat() + 'Z'
                        ).execute()
                        events = events_result.get('items', [])

                        if not events:
                            print(f"Nenhum evento encontrado com o nome '{nome}' para deletar.")
                            return

                        print(f"Encontrados {len(events)} evento(s) com o nome '{nome}':")
                        for event_item in events:
                            print(f"  Deletando: '{event_item['summary']}' (ID: {event_item['id']}) em {event_item['start'].get('dateTime', event_item['start'].get('date'))}")
                            service.events().delete(calendarId=calendar_id, eventId=event_item['id']).execute()
                            print("--- Eventos deletado(s) com sucesso. ---")

                    
                    elif com.DATA():
                        data = com.children[2].getText().split('-')
                        dia = data[0]
                        mes = data[1]
                        ano = data[2]

                        data = f"{ano}-{mes}-{dia}"
                        print(f"Tentando deletar eventos no dia: {data}")

                        start_of_day = datetime.datetime.strptime(data, "%Y-%m-%d")
                        end_of_day = start_of_day + datetime.timedelta(days=1) - datetime.timedelta(microseconds=1)

                        events_result = service.events().list(
                            calendarId=calendar_id,
                            timeMin=start_of_day.isoformat() + 'Z',
                            timeMax=end_of_day.isoformat() + 'Z',
                            singleEvents=True,
                            orderBy='startTime'
                        ).execute()
                        events = events_result.get('items', [])

                        if not events:
                            print(f"Nenhum evento encontrado para deletar no dia {data}.")
                            return

                        print(f"Encontrados {len(events)} evento(s) no dia {data}:")
                        for event_item in events:
                            print(f"  Deletando: '{event_item['summary']}' (ID: {event_item['id']}) em {event_item['start'].get('dateTime', event_item['start'].get('date'))}")
                            service.events().delete(calendarId=calendar_id, eventId=event_item['id']).execute()
                            print("  Deletado com sucesso.")

                    else:
                        print("Formato de comando DELETAR inválido. Use 'deletar \"Nome do Evento\"' ou 'deletar DD-MM-AAAA'.")
                    print("----------------------------------------")

                except HttpError as err:
                    print(f"Erro na API do Google Calendar: {err}")
                    print(f"Detalhes do erro: {err.content.decode()}")
                except Exception as e:
                    print(f"Ocorreu um erro inesperado: {e}")
            
            elif com.REPETIR():
                for i in range(0,int(com.children[2].getText())):
                    print(i+1, "ª repetição do comando:")
                    for com in com.com():
                        avalie(com, service, calendar_id)
                        time.sleep(0.5)
                        
            elif com.CONSULTAR():
                try:
                    nome = com.children[2].getText().strip('"')
                    print(f"Consultando eventos com o nome: {nome}")

                    events_result = service.events().list(
                        calendarId=calendar_id,
                        q=nome,
                        singleEvents=True,
                        orderBy='startTime',
                        timeMin=datetime.datetime.utcnow().isoformat() + 'Z'
                    ).execute()
                    events = events_result.get('items', [])

                    if not events:
                        print(f"Nenhum evento encontrado com o nome '{nome}'.")
                        return

                    print(f"Encontrados {len(events)} evento(s) com o nome '{nome}':")
                    for event_item in events:
                        start = event_item['start'].get('dateTime', event_item['start'].get('date'))
                        end = event_item['end'].get('dateTime', event_item['end'].get('date'))
                        print(f"  Evento: '{event_item['summary']}' de {start} até {end} (ID: {event_item['id']})")

                except HttpError as err:
                    print(f"Erro na API do Google Calendar: {err}")
                    print(f"Detalhes do erro: {err.content.decode()}")
                except Exception as e:
                    print(f"Ocorreu um erro inesperado: {e}")
                
            
   
#Main
#input_stream = FileStream(sys.argv[1])
input_stream = FileStream(sys.argv[1], encoding='utf-8')  # Adicionando o encoding
lexer = CompiladorLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = CompiladorParser(stream)
tree = parser.prog()

if parser.getNumberOfSyntaxErrors() == 0:
    print("ok")
    print(tree.toStringTree(recog=parser))
    try:
        # Autenticando usando a conta de serviço (feito uma única vez)
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
            )
        # Conectar à API (feito uma única vez)
        service = build("calendar", "v3", credentials=credentials)

        # Inicia o processamento dos comandos na árvore
        iniciar(tree, service, CALENDAR_ID)

    except HttpError as err:
        print(f"Erro de autenticação ou conexão com a API: {err}")
        print(f"Detalhes do erro: {err.content.decode()}")
    except Exception as e:
        print(f"Ocorreu um erro fatal na inicialização: {e}")

else:
    print("erro sintático")

