import sys
class Histogram:
    "This Class makes a histogram out of a red in file"
    def __init__(self,file_str):
        file = open(file_str,'r')
        file_list = file.read()
        file_list = file_list.split(' ')
        self.file_list = file_list
        # print(self.file_list)

    def listogram(self):
        listogram = [[word,self.file_list.count(word)] for word in self.file_list]
        return listogram

    def dictogram(self):
        dictogram ={}
        for word in self.file_list:
            if word in dictogram:
                dictogram[word] += 1
            else:
                dictogram[word] = 1
        return dictogram

    def tuplegram(self):
        tuplegram =[(word,self.file_list.count(word)) for word in self.file_list]
        return tuplegram

    def unique_words(self):
        dictogram_1 = self.dictogram()
        unique_words_list = []
        for key,value in dictogram_1.items():
            if value == 1:
                unique_words_list.append(key)
        return unique_words_list

    def frequency(self,word):
        dictogram_1 = self.dictogram()
        for key,value in dictogram_1.items():
            if key == word:
                return value
if __name__ == '__main__':
    test = Histogram('source.txt')
    example = test.tuplegram()
    dictogram1 = test.dictogram()

    print(test.frequency(sys.argv[1]))
