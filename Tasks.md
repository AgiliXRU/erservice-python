# 

## Task #1: add &lt;Condition> from XML to JSON

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

to: http://localhost:8000/inboundPatients

```JSON
[
    {
        "transportId": 1,
        "name": "John Doe",
        "priority": "YELLOW"
    }
]
```

## Techniques 

## § Pass Null

### Steps
1. define change point
2. try to create test (with dependency)
3. extract method
4. pass null as dependency
5. make green test
6. add assertion for condition
7. make test green (write production code)

## § Expose static method

### Steps
1. make previously extracted method static
2. fix tests if needed

## Task #2: Add residents

to http://localhost:8000/physiciansOnDuty

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
add role=RESIDENT
```JSON
{
  ...
  "role": "RESIDENT",
  ...
}
```
## Techniques
## § Parametrize Constructor

### Steps
1. find change point // cmd+shift+t
1. try to write characterization test for method
1. parametrize a constructor StaffAssignmentManager() // cmd+alt+p
1. write test doubles
1. make test green
1. add check for resident
1. make test green again

## Task #3 Process Yellow Priority 

Now we have this 
```JSON
POST http://localhost:4567/simulateNewTransport
Content-Type: application/json

{
  "name": "Sandra Plum",
  "priority": "RED",
  "condition": "stroke"
}
```

we want to send a message with priority=Yellow and condition=heart arrhythmia
```JSON
POST http://localhost:4567/simulateNewTransport
Content-Type: application/json

{
  "name": "Doroty Olive",
  "priority": "YELLOW",
  "condition": "heart arrhythmia"
}
``` 
// Endpoint to scan and send a message http://localhost:8000/scanForCritical

## Techniques
## § Subclass & Override method

### Steps

1. Find change point // AlertScanner.scan()
1. Write test // test_scan_for_red_priority_patients
    1. Create double for ```InboundPatientController``` and make it pass patients
    1. Subclass ```AlertScanner``` and override ```alert_for_new_critical_patient()```
    1. make it pass
1. Add test for priority=Yellow, condition=heart arrhythmia
1. Change ```scan()``` 


## Task #4 Send a message with acknowledge for red priority patients only

## Technique
## § Wrap method

### Steps
1. find change point // alert_for_new_critical_patient
1. extract method
1. modify tests from [Task #3](#task3) - override new method   
1. modify assertions is tests
1. implement new logic

## § Wrap class
### Steps
1. move extracted method to a new class
1. use test double for a new class in tests

## Task #5: Do not count inbound if non-critical condition

Non-critical mean contains "ambulatory" or "non-emergency"  

## Technique
## § Sprout method

### Steps

1. find change point
1. create new method in same class
1. write test
1. implement logic


## Task #6: Add to message current divergence situation when any message send

eg:
```text
Situation report: 
Inbound patients requiring beds: 1 Red, 2 Yellow, 3 Green.
```

## Technique
## § Sprout class

1. find change point
1. create new class with a method, pass all needed variables
1. write test
1. implement logic

