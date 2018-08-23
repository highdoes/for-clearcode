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

koty = "cat cats cat's"

regex3 = re.compile("[cat]+['s]*")

matches = re.findall(regex3, koty)

for x in matches:
    print(x)

strin = "<name>keymap</name><name>default</name>"

regex4 = re.compile("<name>.*</name>")  # greedy
regex5 = re.compile("<name>(.*?)</name>")  # lazy
matches2 = re.findall(regex4, strin)
for x in matches2:
    print(x)
matches3 = re.findall(regex5, strin)
for x in matches3:
    print(x)

strin2 = "asdasd asdasd asdasd /"

regex6 = re.compile(r"^.*[^/]")
matches4 = re.findall(regex6, strin2)
print(matches4)
historia = {}
adres = ["https://www.youtube.com/watch?v=a7nuYAk2xK8&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=16",
         "youtube.com/watch?v=a7nuYAk2xK8&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=16",
         "https://youtube.com/watch?v=a7nuYAk2xK8&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=16",
         "https://docs.python.org/3.7/library/re.html"]
for link in adres:
    if "www" in link and 'http' in link:
        regex5 = re.compile(r"www.(.*?)/")
    if 'http' in link:
        regex5 = re.compile(r"://(.*?)/")
    else:
        regex5 = re.compile("(.*?)/")
    matches5 = re.findall(regex5, link)
    for x in matches5:
        if "www" in x:
            x = x.strip("www.")
        if x in historia.keys():
            historia[x] += 1
        else:
            historia[x] = 1
for k,v in historia.items():
    print(k,v)