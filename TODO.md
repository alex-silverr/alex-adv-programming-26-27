# TODO
## Structure:
- [ ] CRUD API on Python container
- [x] Persistent Postgres database on container
- [x] Postman
- [ ] OPTIONAL: Javascript/Angular/some other sort of frontend thing if I have time

## Step-by-Step
- [x] Understand and set up Postman
- [x] Dockerize flask 
- [x] Create the most barebones API possible, execute on Docker
- [x] Test interaction of barebones API and Postman for testing
- [x] Make a simple database container
- [x] Connect backend and database containter
- [x] Test saving barebones backend stuff to database
- [x] Set up database persistence
- [x] Make db user and password safe
- [x] Design ticket objects
- [x] Create persistent tables
- [x] Create basic CRUD API for Ticket, Event and User
- [x] Create basic READ API for option tables
- [ ] Create extra entrypoints for Ticket, Event and User
- [ ] Organize and separate files for better visibility
- [ ] OPTIONAL: create frontend
	- Angular?????
	- Honestly I don't know. TODO: look into that when I get to it

# Database

## Endpoints
### Ticket
- [x] CREATE: Create new
- [x] READ: Read all
- [x] READ: Search by filter
- [x] READ: Get by ID
- [x] UPDATE: Edit info (Title, Description, Priority)
- [ ] UPDATE: Add history item
- [ ] UPDATE: Assign to user
- [x] UPDATE: Change estimated time
- [x] UPDATE: Change status ("DELETE": Removed status)

### Event
- [ ] CREATE: Create new history item
- [ ] CREATE: Create from editing info (Title, Description, Priority)
- [ ] CREATE: Create from adding subtask
- [ ] CREATE: Create from adding to group task
- [ ] CREATE: Create from assign to user
- [ ] CREATE: Create from change estimated time
- [ ] CREATE: Create from change status
- [ ] READ: Read all
- [ ] READ: Search by user
- [ ] READ: Get by ID

### User
- [x] CREATE: Create new
- [x] READ: Read all
- [x] READ: Search by filter
- [x] READ: Get by ID
- [x] UPDATE: Edit info (Display name, Full name, E-mail, GitHub, Role)
- [ ] DELETE: Delete user by ID

### Priority Level
- [x] READ: Read all
- [x] READ: Get by ID

### Ticket Type
- [x] READ: Read all
- [x] READ: Get by ID

### Ticket Status
- [x] READ: Read all
- [x] READ: Get by ID

### Event Type
- [x] READ: Read all
- [x] READ: Get by ID

### Edited Field
- [x] READ: Read all
- [x] READ: Get by ID

### User Role
- [x] READ: Read all
- [x] READ: Get by ID

## Design
### Ticket
- ID (auto generated)
- Title
- Created on (date)
- Description
- History -- *Event, list of*
- Created by -- *User, one*
- Assigned to -- *User, list of*
- Priority -- *Priority Level, one*
- Ticket Type -- *Ticket Type, one*
- Estimated time
- Status -- *Ticket Status, one*

### Event
- ID (auto generated)
- Actor -- *User, one*
- Ticket -- *Ticket, one*
- Date of (date)
- Event Type -- *Event Type, one*
- Description (if type is "New history item")
- Edited field (if type is not "New history item") -- *Edited Field, one*

### Priority Level
- ID (auto generated)
- Description:
	- Urgent 
	- High priority
	- Medium priority
	- Low priority
	- Background task

### Ticket Type
- ID (auto generated)
- Description:
	- Error - A problem that breaks functionality
	- Issue - A problem that hampers, but do not break, software use
	- Vulnerability - An issue invisible to software use, but potential point of exploit
	- Feature - A new feature to be developed. 
	- Requirements - A new change to be developed that will affect the system beyond a single feature.

### Ticket Status
- ID (auto generated)
- Description:
	- New
	- Approved
	- Assigned
	- In Progress
	- On Hold
	- Resolved
	- Removed

### Event Type
- ID (auto generated)
- Description:
	- Change details (Title, Description, Priority)
	- Assign person to ticket
	- Change estimated time
	- Change Status
	- New history item

### Edited Field
- ID (auto generated)
- Description:
	- Title
	- Description
	- Priority
	- Assigned to
	- Estimated time
	- Status

### User
- ID (auto generated)
- Display name
- Full name
- Registered on (date)
- E-mail
- GitHub
- Role -- *User Role, one*

### User Role
- ID (auto generated)
- Description:
	- Developer
	- Analyst
	- Manager
	- Designer
	- Owner
	- QA
	- Tester