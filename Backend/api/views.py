from http.client import HTTPResponse
from sqlite3 import IntegrityError

from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DatiPersona
from .serializers import DatiPersonaSerializer
from codicefiscale import codicefiscale


@api_view(['GET', 'POST'])
def getPersone(request):
    '''
    GET = Restituisce tutte le persone con i relativi dati
    POST = controlla che i dati ricevuti dal form siano corretti , se corretti calcola il cf e aggiunge la persona al DB
    '''

    if request.method == 'GET':
        persone = DatiPersona.objects.all()
        serializer = DatiPersonaSerializer(persone, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        surname = request.data.get('surname')
        name = request.data.get('name')
        sex = request.data.get('sex')
        birthdate = request.data.get('birthdate')
        birthplace = request.data.get('birthplace')

        # CALCOLO CF CON I DATI DEL FORM
        try:
            cf = codicefiscale.encode(surname=surname, name=name, sex=sex,
                                      birthdate=birthdate, birthplace=birthplace)

        except ValueError:
            return JsonResponse({"errore_comune": "Località non valida"}, status=status.HTTP_400_BAD_REQUEST)

        # ESISTE UNA PERSONA NEL DB CON QUESTI DATI?
        esiste = DatiPersona.objects.filter(surname=surname, name=name, sex=sex,
                                            birthdate=birthdate, birthplace=birthplace)

        if esiste:

            # CERCA PERSONA CON QUEL CF SUL DB
            plogged = DatiPersona.objects.get(codice_fiscale=cf)

            return JsonResponse({"codice_fiscale": plogged.codice_fiscale})
        # CF NON TROVATO SUL DB
        else:

            try:
                pnew = DatiPersona(surname=surname, name=name, sex=sex,
                                   birthdate=birthdate, birthplace=birthplace, codice_fiscale=cf)
                pnew.save()

            except IntegrityError as e:
                avviso = 'valore già presente nel db'
                print(avviso)

            return JsonResponse({"codice_fiscale": pnew.codice_fiscale, "messaggio": "Nuovo CF aggiunto al db"})


@ api_view(['GET'])
def getPersona(request, pk):
    persona = DatiPersona.objects.get(id=pk)
    # SERIALIZZARE DATI PERSONA
    serializer = DatiPersonaSerializer(persona, many=False)
    return Response(serializer.data)
