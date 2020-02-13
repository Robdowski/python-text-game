# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, shorthand, description, inspect_message_items= '', inspect_message_looted='', items = [], n_to = '', s_to = '', e_to = '', w_to = ''):
        self.name = name
        self.shorthand = shorthand
        self.description = description
        self.inspect_message_items = inspect_message_items
        self.inspect_message_looted = inspect_message_looted
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
        f"You are in the {self.name} room. {self.description}"

    def inspect(self):
        if not self.items:
            print(self.inspect_message_looted)
        else:
            print(self.inspect_message_items)
            print("\n=== Items in room ===\n")
            [print(f"{item.name}\n") for item in self.items]

