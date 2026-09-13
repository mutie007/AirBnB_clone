#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return
        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show an instance based on class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        print(objs[key])

    def do_destroy(self, arg):
        """Destroy an instance based on class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        del objs[key]
        storage.save()

    def do_all(self, arg):
        """Print all instances or all instances of a class.
        Usage: all [class name]
        """
        objs = storage.all()
        if arg and arg not in classes:
            print("** class doesn't exist **")
            return
        result = []
        for key, obj in objs.items():
            if not arg or type(obj).__name__ == arg:
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Update an instance based on class name and id.
        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objs[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        try:
            attr_value = int(attr_value)
        except ValueError:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
