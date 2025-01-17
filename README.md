# WildfireReports
Simple Django API to manage wildfire reports for follow up by emergency authorities. 


## Getting Started
Comes with a pre-populated SQLite db with some wildfires and a Django admin (username:admin, password:supersecret). Just clone the repository and run: 
```
docker-compose up --build 
```

To run unit tests:

1. Activate a python virtual environment
2. Install requirements

```
pip install -r config/requirements.txt
```

3. Run tests

```
python3 app/manage.py test  
```

TODO BUGBUG ERROR

Zero tests were run, see:

```
Found 0 test(s).
System check identified no issues (0 silenced).

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```

TODO BUGBUG ERROR


## Architecture
App is served by Django with Nginx as proxy, see Docker Compose


## Endpoints:
/API/WildfireReport/<str:id>/

GET:
- Accepts optional id paramenter
- Without the id parameter, returns all wildfire reports in JSON
- If an id is specified, returns the specific id or an error message in JSON eg. {"message": "Wildfire with id: 24 not found!"}

POST 
- Accepts optional id parameter but requires JSON in the body to define a new report or update an existing one
- Without the id parameter, accepts a report definition in JSON (see above)
- If an id is passed, updates existing report with report JSON sent in request

DELETE
- Requires the id parameter
- Deletes the report with the matching id
- If report with specified id is not found, returns an error in JSON eg. {"message": "Report with id: 25 not found!"}

Wildfire Report JSON Definition:
```json
{
    "town": "Burlington",
    "reported_by": "John Doe",
    "contact_number": "(555)-867-5309"
}
```
