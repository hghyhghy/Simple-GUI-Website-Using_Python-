from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  # def text_box_3_pressed_enter(self, **event_args):
  #   """This method is called when the user presses Enter in this text box"""
  #   pass

  # def check_box_1_change(self, **event_args):
  #   """This method is called when this checkbox is checked or unchecked"""
  #   pass

  # def link_1_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   pass

  # def link_4_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   pass

  # def link_3_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   pass

  # def check_box_2_change(self, **event_args):
  #   """This method is called when this checkbox is checked or unchecked"""
  #   pass

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name=self.text_box_1.text
    email=self.text_box_2.text
    city=self.drop_down_1.items
    gender=self.drop_down_2.items
    ui=self.check_box_3.checked
    ui=self.check_box_1.checked
    # account=self.check_box_2.checked

    anvil.server.call('login',Name=name,Email=email,City=city,Gender=gender,UiToken=ui)

    Notification("Your Response Has Been Recorded").show()
  # def text_box_2_pressed_enter(self, **event_args):
  #   """This method is called when the user presses Enter in this text box"""
  #   pass

  # def text_box_1_pressed_enter(self, **event_args):
  #   """This method is called when the user presses Enter in this text box"""
  #   pass

  # def outlined_button_2_click(self, **event_args):
  #   """This method is called when the button is clicked"""
  #   pass

  # def file_loader_1_change(self, file, **event_args):
  #   """This method is called when a new file is loaded into this FileLoader"""
  #   pass

  # def youtube_video_2_state_change(self, state, **event_args):
  #   """This method is called when the video changes state (eg PAUSED to PLAYING)"""
  #   pass

  # def youtube_video_1_state_change(self, state, **event_args):
  #   """This method is called when the video changes state (eg PAUSED to PLAYING)"""
  #   pass

  # def check_box_1_change(self, **event_args):
  #   """This method is called when this checkbox is checked or unchecked"""
  #   pass














