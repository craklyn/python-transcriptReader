import duckling
import pandas

d = duckling.Duckling()
d.load()
print(d.parse("tomorrow"))
print(d.parse("daniel@fartbox.com"))
print(d.parse("daniel at fartbox dot com"))
print(d.parse("daniel that fartbox dot com"))
print(d.parse("daniel at fartbox dot org"))
print(d.parse("daniel at fartbox dot info"))
print(d.parse("daniel at fartbox dot gov"))
print(d.parse("1208 weeks"))
print(d.parse("7208 weeks"))
print(d.parse("circle 7208 weeks all circle a house or the e. r."))
print(d.parse('eighty pound cat'))


callData = pandas.read_csv('Data/callData.csv')
callData['callerWords'].str.contains("gmail")
callData['callerWords'].str.contains("gmail")[22]


gmailMentions = callData['callerWords'][callData['callerWords'].str.contains("gmail")].str.find("gmail")
#list(map((lambda x: x.find("gmail")), callData$callerWords['callerWords')))[1]

d.parse(callData['callerWords'][1155])

emailFound = 0
for ind, val in gmailMentions.iteritems():
  print(ind)
  # callData['callerWords'][ind]
  #print(d.parse(callData['callerWords'][ind]))
  entryFound = False
  for entry in d.parse(callData['callerWords'][ind]):
    if 'dim' in entry and entry['dim'] == 'email':
      #print(entry)
      entryFound = True
  if entryFound == False:
    print("No email address found")
  else: 
    emailFound += 1

print("Number of calls with emails found: " + str(emailFound))

# 5673
  
#for ind, val in temp.iteritems():
#  print(ind)
#  # callData['callerWords'][ind]
#  print(d.parse(callData['callerWords'][ind]))
#  
#d.parse(callData['callerWords'][384][140:160])


