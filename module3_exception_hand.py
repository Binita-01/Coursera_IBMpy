try: 
  getfile = open ("myfile","r")
  getfile.write("My file for exception handling.")
except IOError: 
  print("Unable to open or read the data in the field")
else: 
  print("Didn't handle by try and except. ")

# zerodivision error
# value error
# filenot found error
# index error
# key error
# type error
# 
