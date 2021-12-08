def load_MiniC_file(file: str) -> str:
  miniCFile = open(file, "r")
  try:
    return miniCFile.read()
  except:
    raise Exception("Something went wrong reading the file.")