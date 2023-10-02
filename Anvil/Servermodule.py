import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable

def login(Name,Email,City,Gender,UiToken):

 app_tables.unleashinnovation.add_row(Name=Name,Email=Email,City=City,Gender=Gender,UiToken=UiToken)

 # anvil.Email.send(to="sarkarsubham624@gmail.com", subject="Response from Unleashinnovation",text=f"Feedback from {Name}:City is {City} and Gender is {Gender}.Have An Account:{Account}")
