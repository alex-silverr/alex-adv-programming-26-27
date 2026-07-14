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
- [x] Create extra entrypoints for Ticket, Event and User
- [x] Fix things left on TODO like list relationships
- [x] Separate option functions in connection and endpoint
- [ ] Test every endpoint
- [x] Create checks for options
- [x] Organize and separate files for better visibility
- [x] Remove test remnants
- [ ] Write better README documentation
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
- [x] UPDATE: Add history item
- [x] UPDATE: Assign to user
- [ ] UPDTATE: remove assigned user
- [x] UPDATE: Change estimated time
- [x] UPDATE: Change status ("DELETE": Removed status)

### Event
- [x] CREATE: Create new history item
- [x] CREATE: Create from editing info (Title, Description, Priority)
- [x] CREATE: Create from assign to user
- [x] CREATE: Create from change estimated time
- [x] CREATE: Create from change status
- [x] READ: Read all
- [x] READ: Search by user
- [x] READ: Get by ID

### User
- [x] CREATE: Create new
- [x] READ: Read all
- [x] READ: Search by filter
- [x] READ: Get by ID
- [x] UPDATE: Edit info (Display name, Full name, E-mail, GitHub, Role)
- [x] DELETE: Delete user by ID

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

## Testing Checklist
- [x] Ticket - create new ticket
- [ ] Ticket - search tickets
  - [x] Ticket - search all
  - [x] Ticket - search by title
  - [x] Ticket - search by user that created it
  - [ ] Ticket - search by assigned to
  - [x] Ticket - search by priority
  - [x] Ticket - search by ticket type
  - [x] Ticket - search by status
- [x] Ticket - get specific ticket
- [x] Ticket - edit ticket's basic information
- [ ] Ticket - assign ticket to user
- [ ] Ticket - change estimated time
- [ ] Ticket - change ticket status
- [ ] Ticket - CRUD update
- [ ] Ticket - CRUD delete
- [x] User - create new user
- [ ] User - search users
  - [ ] User - search all
  - [ ] User - search by display name
  - [ ] User - search by email
  - [ ] User - search by role
- [ ] User - get specific user
- [ ] User - update user information 
- [ ] User - remove user
- [x] Event - make new "history item" event
- [ ] Event - search events
  - [x] Events - search all
  - [ ] Events - search by title
  - [ ] Events - search by created by
  - [ ] Events - search by priority
  - [ ] Events - search by ticket type
  - [ ] Events - search by status
- [ ] Event - get specific event
- [ ] Event - CRUD update
- [ ] Event - CRUD delete
- [ ] Options - get list
- [ ] Options - get instance
- [ ] Options - create
- [ ] Options - delete