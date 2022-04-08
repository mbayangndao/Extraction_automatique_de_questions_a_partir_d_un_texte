import extraction_questions
text1=open("texte1.txt","r+",encoding="utf_8")
text2=text1.read()
print("temps",extraction_questions.extraction_questions(text2))