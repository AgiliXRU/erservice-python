# Общий алгоритм

1. Найти точку изменения
2. Разорвать зависимость
3. Написать тест
4. Написать тест на новое поведение
5. Написать необходимый код

# Техники

## §1 Передача нулевого значения (Pass Null)

### Задача: Передавать &lt;Condition> из XML в JSON

from: http://127.0.0.1:4567/inbound

```xml
<Inbound>
	<Patient>
		<TransportId>1</TransportId>
		<Name>John Doe</Name>
		<Condition>heart arrhythmia</Condition>
		<Priority>YELLOW</Priority>
		<Birthdate></Birthdate>
	</Patient>
</Inbound>
```

http://localhost:8000/inboundPatients

```JSON
[
    {
        "transportId": 1,
        "name": "John Doe",
        "priority": "YELLOW"
    }
]
```
---

## § 1a Выставить статический метод (Expose static method)
### Задача: та же, вывести condition

--- 

## §2 Унаследовать и переопределить (Subclass & Override method)

### Задача #2: Добавить отсылку уведомления для пациентов с priority=YELLOW и condition=heart arrhythmia 

Мы хотим отправлять сообщения по прибывающим пациентам с "желтым" приоритетом и состоянием "heart arrhythmia"

```JSON
POST http://localhost:4567/simulateNewTransport
Content-Type: application/json

{
  "name": "Doroty Olive",
  "priority": "YELLOW",
  "condition": "heart arrhythmia"
}
```
---
## §3 Метод-обёртка (Wrap method)

### Задача: мы хотим отправлять сообщения с подтверждением только по пациентам с "красным приоритетом"

---

## §4 Метод-росток (Sprout method)
## Task #4: Не учитывать в подсчёте загруженности больницы пациентов не подлежащих госпитализации

condition = ambulatory   

---

## §5 Добавление параметра в конструктор (Parametrize Constructor)
### Задача: добавить в вывод врачей на дежурстве помимо докторов еще и резидентов  

http://localhost:8000/physiciansOnDuty

```JSON
[
    {
        "staffId": 1,
        "name": "Leonard McCoy",
        "role": "DOCTOR"
    },
    {
        "staffId": 2,
        "name": "Beverly Crusher",
        "role": "DOCTOR"
    },
    {
        "staffId": 3,
        "name": "Benjamin Pierce",
        "role": "DOCTOR"
    },
    {
        "staffId": 4,
        "name": "John Zoidberg",
        "role": "DOCTOR"
    }
]
```
Добавить роль = RESIDENT
```JSON
{
  ...
  "role": "RESIDENT",
  ...
}
```


