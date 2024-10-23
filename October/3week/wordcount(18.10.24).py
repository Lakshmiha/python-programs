text=input("Enter a sentence:")
words=text.lower().split()
word_count={}
for i in words:
    word_count[i]=word_count.get(i,0)+1
print("Count=",word_count)
