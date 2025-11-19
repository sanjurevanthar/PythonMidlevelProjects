#open the file and read its content and the store into story variable

with open("story.txt","r") as f:
    story = f.read()

#Interating throughout the story and fetching the <word> into a set
start_index = -1
words = set()

target_start = "<"
target_end = ">"

for i,char in enumerate(story):

    #check if the the char equals the target_start
    if char == target_start:
        start_index = i
    if char == target_end and start_index != -1:
        words.add(story[start_index:i+1])
        #reassign the start_index
        start_index = -1

#print(words) #{'<adjective1>', '<place2>', '<character>', '<adverb>', '<emotion>', '<place>', '<animal>', '<weather_condition>', '<emotion2>', '<object>', '<terrain>'}

answer_map = {}

#now we iterate through the set and we get an equivalent word replacement for the values from the set
#use map to map them

for vals in words:
    ans = input("Enter the word for :" + str(vals) + ": ")
    answer_map[vals] = ans

#print(answer_map)

#Now replace the <words> with actual words which we stored in the map
for val in words:
    #use replace function
    story = story.replace(val, answer_map[val])

print(story)