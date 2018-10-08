Folgende Aufrufe funktionieren (mit ihren Ergebnissen):

http://localhost:5000/appointments
[
    {
        "date_agreed": "",
        "date_offered": "dateVorschlag",
        "guest_id": "AndiID",
        "host_id": "SteffenID",
        "id": "3ab97853-a5ca-4dfd-af90-9f7c36018f91"
    },
    {
        "date_agreed": "",
        "date_offered": "dateVorschlag",
        "guest_id": "EstherID",
        "host_id": "UlrikeID",
        "id": "1b0c4b7a-ee3f-4326-8f66-7c5553e13af3"
    },
    {
        "date_agreed": "",
        "date_offered": "dateVorschlag",
        "guest_id": "AndiID",
        "host_id": "UlrikeID",
        "id": "4d473d1f-6a2b-4787-a39a-19d07848740a"
    }
]
http://localhost:5000/appointments/host?id=UlrikeID
[
    {
        "date_agreed": "",
        "date_offered": "dateVorschlag",
        "guest_id": "EstherID",
        "host_id": "UlrikeID",
        "id": "1b0c4b7a-ee3f-4326-8f66-7c5553e13af3"
    },
    {
        "date_agreed": "",
        "date_offered": "dateVorschlag",
        "guest_id": "AndiID",
        "host_id": "UlrikeID",
        "id": "4d473d1f-6a2b-4787-a39a-19d07848740a"
    }
]

http://localhost:5000/appointments/guest?id=AndiID
[
    {
        "date_agreed": "",
        "date_offered": "dateVorschlag",
        "guest_id": "AndiID",
        "host_id": "SteffenID",
        "id": "3ab97853-a5ca-4dfd-af90-9f7c36018f91"
    },
    {
        "date_agreed": "",
        "date_offered": "dateVorschlag",
        "guest_id": "AndiID",
        "host_id": "UlrikeID",
        "id": "4d473d1f-6a2b-4787-a39a-19d07848740a"
    }
]


Nun gibt es auch:
mit HTTP DELETE zum Löschen eines Appointments
http://localhost:5000/appointment?id=76f0d6f9-ab99-4198-8da3-5f82ccca670a

und HTTP POST zum Anlegen eines neuen Appointments
http://localhost:5000/appointment
Daten als JSON im Body
{
	"host_id" : "EstherID",
	"guest_id" : "UlrikeID",
	"date_offered" : "OPEN"
}