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
