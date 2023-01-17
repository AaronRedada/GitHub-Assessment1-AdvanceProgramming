file_name = open("sentences.txt", "rt")
data = file_name.read()
name = data.count("Hello my name is Amster Sani")

print('Number of sentences in the text file :', name)