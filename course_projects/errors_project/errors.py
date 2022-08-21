class RuntimeErrorWithCode(Exception):
  """
  Exception raised when a specific error code is needed. <This is a docstring>
  """
  def __init__(self, message, code):
    super().__init__(f"Ex{code}: {message}")
    self.code = code

raise RuntimeErrorWithCode("OUCH! An error happened.", 500)