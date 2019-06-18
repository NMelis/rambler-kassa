## install
Simply run:
```
pip install rambler-kassa
```

or download the project via git clone and run the following:
```
pip install -r requirements.txt
```

## usages
Create instance
```python
from rambler_kassa.rambler_kassa import *

city_id = 1 # Identifier of the city where the films will be searching in the cinema

kassa = RamblerKassa('<api_key>', city_id)

```

### Get movies
```python
for item in kassa.get_movies(98847):
    print(item)
# -> Movie OriginalName='Take That: Greatest Hits Live' Genre=['Музыкальный'] Country=['Великобритания'] ViewCountDaily=0 AgeRestriction='16' Thumbnail='https://kassa.rambler.ru/s/StaticContent/P/Aimg/1905/23/190523100556922.jpg?1…' Cast=[] Description='29 июня Невафильм Emotion выпустит в кинотеатрах страны концерт «Take That: G…' Director='' CreatorName=None CreatorObjectID=None Year='2019' Duration='150 мин.' HorizonalThumbnail='https://kassa.rambler.ru/s/StaticContent/P/Aimg/1905/23/190523100557089.jpg' IsNonStop=False SubCreationIDs=[] Rating='7.00' Trailers=None Frames=None ReleaseDate=datetime.date(2019, 6, 29) KinoplanID=13477 ObjectID=98725 ClassType='Movie' Name='Take That: Greatest Hits Live' AfishaClassID=16 AfishaObjectID=257101
# -> Movie OriginalName='' Genre=['Документальный', ' Музыкальный'] Country=['Великобритания'] ViewCountDaily=1 AgeRestriction='16' Thumbnail='https://kassa.rambler.ru/s/StaticContent/P/Aimg/1906/14/190614141030583.jpg?1…' Cast=[] Description='«The Cure – Anniversary 1978-2018 Live in Hyde Park London», снятый режиссеро…' Director='Тим Поуп' CreatorName=None CreatorObjectID=None Year='2019' Duration='137 мин.' HorizonalThumbnail='https://kassa.rambler.ru/s/StaticContent/P/Aimg/1906/18/190618155201329.jpg' IsNonStop=False SubCreationIDs=[] Rating='7.00' Trailers=None Frames=None ReleaseDate=datetime.date(2019, 7, 11) KinoplanID=13605 ObjectID=98847 ClassType='Movie' Name='The Cure – Anniversary 1978-2018 Live in Hyde Park London' AfishaClassID=16 AfishaObjectID=25721
# -> ...

```

### Get movie by id
```python
movie = kassa.get_movie(98847)
print(movie)
# -> Movie OriginalName='' Genre=['Документальный', ' Музыкальный'] Country=['Великобритания'] ViewCountDaily=1 AgeRestriction='16' Thumbnail='https://kassa.rambler.ru/s/StaticContent/P/Aimg/1906/14/190614141030583.jpg?1…' Cast=[] Description='«The Cure – Anniversary 1978-2018 Live in Hyde Park London», снятый режиссеро…' Director='Тим Поуп' CreatorName=None CreatorObjectID=None Year='2019' Duration='137 мин.' HorizonalThumbnail='https://kassa.rambler.ru/s/StaticContent/P/Aimg/1906/18/190618155201329.jpg' IsNonStop=False SubCreationIDs=[] Rating='7.00' Trailers=None Frames=None ReleaseDate=datetime.date(2019, 7, 11) KinoplanID=13605 ObjectID=98847 ClassType='Movie' Name='The Cure – Anniversary 1978-2018 Live in Hyde Park London' AfishaClassID=16 AfishaObjectID=257212

```

### Get schedules of movies
```python
schedule = kassa.get_movies_schedules()
print(schedule[0])
# -> Schedule SessionID=46215468 CityID=2565 CreationClassType='Movie' CreationObjectID=97646 PlaceClassType='Place' PlaceObjectID=14232 DateTime=datetime.datetime(2019, 6, 20, 0, 0) Format='3D' IsSaleAvailable=True IsReservationAvailable=False IsWithoutSeats=False MinPrice='190' MaxPrice='190' HallID='9:13' HallName='Зал № 1' FeeType='Percent' FeeValue='0,0'

```

### Get schedule movie by id
```python
schedule = kassa.get_movie_schedules(98847)
print(schedule[0])
# -> Schedule SessionID=46425075 CityID=2565 CreationClassType='Movie' CreationObjectID=98847 PlaceClassType='Place' PlaceObjectID=5385 DateTime=datetime.datetime(2019, 7, 11, 19, 30) Format='' IsSaleAvailable=True IsReservationAvailable=False IsWithoutSeats=False MinPrice='500' MaxPrice='500' HallID='302:292' HallName='03' FeeType='Percent' FeeValue='0,0'

```