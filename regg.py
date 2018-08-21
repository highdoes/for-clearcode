import re

with open("tekst.txt", "r") as myFile:
    data = myFile.read().replace('\n', '')

znalezione = re.findall(".ie.", data)
print(znalezione)


x = "rat cat qat wat"

regex = re.compile("[rc]at")

x = regex.sub("yyy", x)

print(x)

print("Ile kropek: ", len(re.findall(".\.", data)))



numer = "123 12345 123456 123456789"

print("Matches: ", len(re.findall("\d{6,9}", numer)))


mejle = 'qasdasd@sfddas.vc  asdadsa@daadsa  asdadas@gfsdfsdsfs.pl  fffwfw@fsfd'


print("Emails: ", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}\.[A-Za-z]{2,3}", mejle)))



