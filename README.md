# Advanced Programming CA2 - Python CRUD API
**Development of an issue and vulnerability (ticket) tracking system**  


*Alexandre Peres Oliveira da Silva - 20096284*  

This project is designed to be the backend portion of a ticketing issue/vulnerability tracking system to be used in software development and maintenance. 

## Usage
The project is designed to run in Docker containers, and was tested mostly using a Google Cloud Virtual Machine. 

**How to run**
- Fork and/or Clone from git repository
- Install Docker, if not yet installed
- Go to the project's folder (same folder as `Dockerfile` and `docker-compose.yml` files)
- Create a file named `.env`
  - Edit the  `.env` file, including the properties `PG_USER=username-of-your-choice` and `PG_PASSWORD=password-of-your-choice`
- Open command line terminal on the project's folder 
- Execute `docker compose up --build -d`
  - `docker compose` calls the `docker-compose.yml` file
  - `up` executes the action necessary to setup the project containers
  - `--build` rebuilds image, if an outdated version of the project still exists
  - `-d` detaches the containers, allowing for the program to run in background
- To stop execution, run `docker compose down`

## Structure
The project is composed of different modules and uses several tools and libraries: 

| Functionality | Technology |
|-------------- | ---------- |
| Containerization | Docker |
| Database | Postgres (container "db") |
| Programming Language | Python (container "app") |
| Database adapter / interface | psycopg 2 |
| ORM and queries | SQLAlchemy |
| API Framework | Flask |
| Testing API Entrypoints | Postman |



### Endpoints

The following endpoints observe normal/intended functionality and should be exposed to the normal frontend:

**Tickets**
- CREATE | POST: Creates new Ticket:
    
    - Title, ID of creating user, ID of priority level and ID of ticket type are mandatory
        
    - Description and Estimated time to completion are optional fields
        
    - History list and Assigned users are empty upon creation
        
    - Status is "new" upon creation
        
- READ | GET: Search all Tickets, with optional query parameters passed on URI:
    
    - Optional query parameters are:
        
        - Title
            
        - Created after date
            
        - Created before date
            
        - Created by user
            
        - Assigned to user
            
        - Priority level
            
        - Ticket type
            
        - Ticket status
            
- READ | GET: Get Ticket by exact ID
    
- UPDATE | PUSH: Edits the Ticket's basic intormation:
    
    - Fields possible to edit through this method are:
        
        - Title
            
        - Description
            
        - Priority level
            
    - Other fields should not be edited in this manner, and have either a dedicated method to do so or should not be edited at all
        
- UPDATE | PUSH: Assigns Ticket to an User:
    
    - A Ticket can be assigned to multiple users, this adds the new user to list of users assigned to work on the ticket

- UPDATE | PUSH: Un-Assigns a Ticket assigned to an User:
        
- UPDATE | PUSH: Change estimated time described on the Ticket
    
- UPDATE | PUSH: Change the Status of the ticket
    
    - Ideally, to keep a record, tickets should not be deleted from the database. To "delete" a ticket, its status must be changed to either "Resolved", if work on it was successfully complete and the ticket was closed, or "Removed", if the ticket is no longer being managed, but it did not generate a resolved issue

**User**
- CREATE | POST: Creates new User:
    
    - Display name, full name, e-mail and role are mandatory
        
    - GitHub link is optional
        
- READ | GET: Search all Users, with optional query parameters passed on URI:
    
    - Optional query parameters are:
        
        - Display name
            
        - E-mail
            
        - Role
            
- READ | GET: Get User by exact ID
    
- UPDATE | PUSH: Edits the User's intormation:
    
    - Fields possible to edit through this method are:
        
        - Display name
            
        - Full name
            
        - E-mail
            
        - GitHub link
            
        - Role
            
    - Other fields should not be edited in this manner, and have either a dedicated method to do so or should not be edited at all
        
- DELETE | DELETE: Removes user from system


**Event**
- CREATE | POST: Creates new Event of the "new history addition" type:
    
    - Ticket, creating user and event type are mandatory for any event, but, for this type, description is also necessary
        
    - There are many situations in which an event are created, for each event type, however, _new history type is the only user-facing way to create an event_. Other event-creating events are managed internally and hsould not be user-facing.
        
- READ | GET: Search all Events, with optional query parameters passed on URI:
    
    - Optional query parameters is the creating user
        
    - "Search by ticket" is superfluous as this is already stored on the ticket history field
        
- READ | GET: Get Event by exact ID
    

There are no update or delete methods available for events as they represent a single event happening, and they should not be altered or removed after creation


### Tables

**Ticket**
- ID (auto generated, not interactible)
    
- Title
    
- Created on (date of creation, not interactible)
    
- Description
    
- History: list of Events
    
- Created by: one User
    
- Assigned to: list of Users
    
- Priority: one Priority level option
    
- Ticket Type: one Ticket Type option
    
- Estimated Time
    
- Status: one Ticket Status option

**User**

- ID (auto generated, not interactible)
    
- Display name
    
- Full name
    
- Registered on (date of creation, not interactible)
    
- E-mail
    
- GitHub
    
- Role: one User Role option

**Event**
- ID (auto generated, not interactible)
    
- Created by: one User
    
- Ticket: one Ticket
    
- Created On (date of creation, not interactible)
    
- Event Type: one Event Type option
    
- Description (in normal functioning, it can be internally generated)

## Future development

- Frontend Design
- Frontend implementation in Javascript and Angular
- Database migrations with Alembic
- Authentication and authorization method

## References
- https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
- https://www.geeksforgeeks.org/python/python-build-a-rest-api-using-flask/
- https://dev.to/jasec7/building-apis-with-flask-what-they-are-and-what-theyre-used-for-1lm3
- https://medium.com/@dennisivy/flask-restful-crud-api-c13c7d82c6e5
- https://blog.postman.com/how-to-build-an-api-in-python/
- https://learning.postman.com/docs/getting-started/quick-start
- https://www.w3schools.com/html/html_basic.asp
- https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/
- https://docs.docker.com/compose/gettingstarted/
- https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13
- https://docs.docker.com/engine/install/ubuntu/
- https://stackoverflow.com/questions/19315567/returning-rendered-template-with-flask-restful-shows-html-in-browser
- https://www.geeksforgeeks.org/python/default-arguments-in-python/
- https://stackoverflow.com/questions/44405708/flask-doesnt-print-to-console
- https://flask.palletsprojects.com/en/stable/logging/
- https://circleci.com/blog/application-logging-with-flask/
- https://www.w3schools.com/python/ref_string_isnumeric.asp
- https://www.w3schools.com/Python/python_try_except.asp
- https://www.geeksforgeeks.org/python/python-try-except/
- https://www.geeksforgeeks.org/python/python-flask-redirect-and-errors/
- https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask
- https://medium.com/@ritika.atal.work/crud-mapping-to-http-verbs-354a3c0009f5
- https://medium.com/yellowant/rest-api-calls-made-easy-7e620e4d3e82
- https://github.com/flask-restful/flask-restful/issues/114
- https://tortoise.github.io/getting_started.html
- https://stackoverflow.com/questions/57092632/accessing-a-database-in-a-container
- https://stackoverflow.com/questions/44001225/connect-to-postgresql-container-from-another-container-docker
- https://github.com/RassieDotDev/FastAPI-Tortoise-ORM/blob/main/docker-compose.yaml
- https://blog.codewithtemi.com/production-ready-docker-setup-for-full-stack-apps-nextjs-fastapi-postgresql-with-tortoise-orm
- https://betterstack.com/community/guides/scaling-python/tortoiseorm-vs-sqlalchemy/
- https://stackoverflow.com/questions/55311465/what-url-can-docker-container-a-use-to-access-another-docker-container-b-same-d
- https://berkkaraal.com/blog/2024/09/19/setup-fastapi-project-with-async-sqlalchemy-2-alembic-postgresql-and-docker/
- https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a
- https://tortoise.github.io/databases.html
- https://forums.docker.com/t/how-to-reach-localhost-on-host-from-docker-container/113321
- https://docs.docker.com/compose/how-tos/networking/
- https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a
- https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#declaring-mapped-classes
- https://berkkaraal.com/blog/2024/09/19/setup-fastapi-project-with-async-sqlalchemy-2-alembic-postgresql-and-docker/
- https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a
- https://docs.sqlalchemy.org/en/21/core/connections.html
- https://flask-sqlalchemy.readthedocs.io/en/stable/models/
- https://medium.com/@programersign/sqlalchemy-data-model-creation-333937341671
- https://docs.sqlalchemy.org/en/21/orm/session_api.html
- https://docs.sqlalchemy.org/en/21/orm/queryguide/select.html
- https://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask
- https://stackoverflow.com/questions/23600578/python-sql-alchemy-how-to-jsonify-a-class-object-result-from-a-database-query
- https://dev.to/lovestaco/running-postgresql-in-docker-with-persistent-volume-4joe
- https://docs.docker.com/get-started/docker-concepts/running-containers/persisting-container-data/
- https://support.liveagent.com/public/article/3286/attachment/71xoqqspy89yhw74c79u6kqwt3k78qvx/view
- https://www.dnsstuff.com/wp-content/uploads/2024/11/web_help_desk-1.png
- https://zen-marketing-documentation.s3.amazonaws.com/docs/en/SLA_group_ticket.png
- https://docs.sqlalchemy.org/en/21/orm/declarative_tables.html
- https://stackoverflow.com/questions/75363733/sqlalchemy-2-0-orm-model-datetime-insertion
- https://stackoverflow.com/questions/76498857/what-is-the-difference-between-mapped-column-and-column-in-sqlalchemy
- https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#declarative-table-with-mapped-column
- https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
- https://docs.sqlalchemy.org/en/21/core/types.html
- https://stackoverflow.com/questions/26613459/sqlalchemy-how-to-map-single-column-of-one-to-one-relationship-using-declarative
- https://docs.sqlalchemy.org/en/21/orm/extensions/associationproxy.html
- https://docs.sqlalchemy.org/en/21/orm/relationship_api.html#sqlalchemy.orm.relationship
- https://soumendrak.medium.com/autoincrement-id-support-in-sqlalchemy-6a1383520ce3
- https://docs.sqlalchemy.org/en/21/orm/join_conditions.html#handling-multiple-join-paths
- https://docs.sqlalchemy.org/en/21/orm/self_referential.html
- https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#many-to-many
- https://codesignal.com/learn/courses/introduction-to-flask-basics/lessons/working-with-url-query-parameters
- https://www.geeksforgeeks.org/python/how-to-get-specific-columns-in-sqlalchemy-with-filter/
- https://stackoverflow.com/questions/10995172/check-if-list-of-keys-exist-in-dictionary
- https://docs.python.org/2/library/functions.html#all
- https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching
- https://stackoverflow.com/questions/41176006/how-to-do-a-sqlalchemy-query-using-a-string-variable-as-table-name
- https://stackoverflow.com/questions/8561470/sqlalchemy-filtering-by-relationship-attribute
- https://stackoverflow.com/questions/48601123/sqlalchemy-exc-invalidrequesterror-cant-attach-instance-another-instance-with
- https://stackoverflow.com/questions/73879213/instance-is-not-bound-to-a-session