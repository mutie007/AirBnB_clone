# AirBnB Clone - The Console

## Description
This is the first phase of the AirBnB clone project. We build a command-line
interpreter to manage AirBnB objects. This is the foundation for building a
full web application: the console, a website, a database, an API, and a
front-end.

The following classes are implemented:
- **BaseModel**: base class for all models
- **User**: user information
- **State**: state information
- **City**: city information
- **Place**: place information
- **Amenity**: amenity information
- **Review**: review information

## Command Interpreter
The command interpreter allows us to manage objects:
- Create a new object
- Retrieve an object from a file or database
- Update attributes of an object
- Destroy an object
- Do operations on objects (count, compute stats, etc.)

### How to Start
```bash
./console.py
```

### How to Use
The console works in interactive and non-interactive mode.

**Interactive mode:**
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF create destroy all show update quit

(hbnb) quit
$
```

**Non-interactive mode:**
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF create destroy all show update quit

(hbnb)
$
```

### Commands
| Command | Description |
|---------|-------------|
| `quit` | Exits the console |
| `EOF` | Exits the console (Ctrl+D) |
| `help <command>` | Shows help for a command |
| `create <class>` | Creates a new instance of class |
| `show <class> <id>` | Shows an instance by class and id |
| `destroy <class> <id>` | Deletes an instance by class and id |
| `all [class]` | Shows all instances, or all of a class |
| `update <class> <id> <attr> <value>` | Updates an attribute of an instance |

### Examples
```bash
$ ./console.py
(hbnb) create User
246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb) show User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
[User] (246c227a) {'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', ...}
(hbnb) all User
["[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {...}"]
(hbnb) update User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68 first_name "Betty"
(hbnb) destroy User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb) quit
$
```

## Authors
See [AUTHORS](./AUTHORS) file.
