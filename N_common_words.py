import sys
#
# def read_and_split(text_data):
#     with open (text_data,"r") as file:
#         text=file.read()
#         words=text.split()
#         words_count={}#מילון
#         for word in words:
#             word=word.lower()
#             if word in words_count:
#                 words_count[word]+=1
#             else:
#                 words_count[word]=1
    
def sort_words_by_frequency(words_count,n):
        #מיון מהגדול לקטן
        sorted_words=sorted(words_count.items(),key=lambda word:word[1],reverse=True)#בעזרת פונקצית למדה ממיינים את המילון בסדר יורד
        sorted_words=sorted_words[:n]#עושים סלייסינג לרשימה
        sorted_dict=dict(sorted_words)#מחזירים את הרשימה למילון
        return sorted_dict#מחזירים את המילון הממויין
    


       
#הפונקציה מקבלת קובץ ומחזירה מילון עם המילים והכמות שהם מופיעים
#כל מפתח הוא מילה והערך זה כמות הפעמים שהוא מופיע
def read_file_content_to_dictionary(file_path):
    with open(file_path) as file:#פותח את הקובץ לקריאה
        d = {}  #הגדרת מילון
        for line in file:#לולאה שרצה על כל שורה בקובץ
            splited = line.split()# הפונקציה מחלקת את השורה למילים לפי רווחים   
            for word in splited:# לולאה שעוברת מילה מילה מתוך המילים המפורקות בשורה של קובץ          
                if word in d:#בודק אם המילה נמצאת במילון
                    d[word] += 1#אם המילה נמצאת כבר במילון מוסיפים לכמות שהיא נמצאת פלוס 1
                else:
                    d[word] = 1 # אחרת אם התנאי שגוי והמילה עוד לא נמצאה במילון מכניסים את המילה עם ערך 1
        return d#מחזיר את המילון
    


if __name__ == "__main__":  # בודק אם הקובץ הזה מורץ ישירות (ולא מיובא כמודול מקובץ אחר)
    if len(sys.argv) > 1:  # בודק אם המשתמש הכניס ארגומנט מהשורה 
        n = int(sys.argv[1])  # לוקח את הארגומנט הראשון (אחרי שם הקובץ) והופך אותו למספר שלם
    else:
        raise Exception("Please enter N as sys argument")  # אם לא הוזן ארגומנט, זורק שגיאה עם הודעה


    file_path = "C://Users//yonir//OneDrive//Desktop//vs.code.pyYR//read_file.txt"
    #קריאה לפונקציות
    d = read_file_content_to_dictionary(file_path)
    d = sort_words_by_frequency(d, n)
    for key, value in d.items():
        print("Word: " + key + " Appears " + str(value) + " times")
