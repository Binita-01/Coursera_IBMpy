# a recap on string manipulation inside object:

class TextAnalzer(object):
    
    def __init__ (self, text):
        formatted_txt = text.replace([".","!",",","?"],"")
        formatted_txt = formatted_txt.lower()
        self.fmttext = formatted_txt
         
        
    def freqAll(self): 
        fortext = self.fmttext.split(" ")
        
        
        # Create dictionary
        freqmap = {}
        for word in set(fortext):
            # using set to remove duplicates
            freqmap[word] = fortext.count(word)
        return freqmap
           
    def freqOf(self,word):
        freqmap = self.freqAll()
        # for key,val in freqmap:
        #     if word == key:
        #         return val
        #     else: 
        #         return 0
        if word in freqmap:
            return freqmap[word]
        else:
            return 0


# OPEN FUNCTION IN PYTHON TO OPEN AND READ FILES
# file1 = open("filepath","r") : this gives file object
# r for reading
# file1.mod
# file1.close()

# using with to open file will automatically close the file too

with open("file.txt","r") as file1:
    file_stuff = file1.read()
    print(file_stuff)

print(file1.closed)
# can't read outside the indent
print(file_stuff)
# but can print the file stuff outside the indent

file_stuff = ["line1\n","line2\n"]

file_stff = file1.readline() 
# this will read the first line
file_stuff = file1.readline()
# this will read the second line

file_stff = file1.readline(4)
# reads the first 4 characters. 
file_stuff = file1.readline(5)
# reads the 5 character after the first four cause we read that before. 


# SUMMARY FROM THE CHEAT SHEET
# read() reads the entire file
# read.line() reads the first line and keeps track of where it ended
# file.seek(10) goes to the 11th byte [0 based index]
# 

                
        

