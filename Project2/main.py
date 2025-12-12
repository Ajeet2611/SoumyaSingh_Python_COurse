import datetime
import time
name = input("Swagat hai ,enter your name:")
presentHour = datetime.datetime.now().hour
if 5 <= presentHour <=11:
   print("Good morning ", name)
elif 11<=presentHour<=17:
      print("Good afternoon ",name)
elif 17<=presentHour<=20:
    print("Good envening ",name)
else:
    print("Good night ",name)

print("Namaste ! Welcome to Your ChatBot")
print("you can ask me basic Question, Type 'bye' to exit from the bot")

#chatbot Memory creation [dictionary of responses]
responses ={
    "hello": "Hi, welcome. How can I help you ?",
    "who are you": "Keep going . Every bug of your project makes you a better developer !",
    "happy":"Great to hear that",
    "functions kya hota hai":"Jakar chapter 7 padho Saumya singh ai /ml ccourse",
    "hi": "Namaskar! Bataye, kya madad chahiye?",
    "good morning": "Shubh prabhat! Aaj ka din aapka shandar ho.",
    "good evening": "Shubh sandhya! Aaj kya naya chal raha hai?",
    "how are you": "Main bilkul theek hoon, dhanyavaad. Aap kaise hain?",
    "how do you do": "Main achha hoon. Bataye, aapke liye kya kar sakta hoon?",
    "what's up": "Sab badhiya! Aap batao, kya chal raha hai?",
    "thank you": "Aapka swagat hai! Mujhe khushi hui madad karke.",
    "thanks": "Thank you! Aur kuch poochna hai?",
    "bye": "Alvida! Apna khayal rakhiyega. Fir milte hain!",
    "see you later": "Theek hai, fir baat hogi. Take care!",
    "who are you": "Main ek AI assistant hoon, jo aapki madad ke liye bana hoon.",
    "what is your name": "Mera koi naam nahi, par aap mujhe apna assistant maan sakte hain.",
    "where are you from": "Main cloud mein rehta hoon aur hamesha aapki seva ke liye tayyar hoon.",
    "functions kya hota hai": "Function code ka ek block hota hai jo ek specific task perform karta hai.",
    "happy": "Bahut accha laga sun kar! Kyun khush ho aaj?",
    "sad": "Ohh, mujhe afsos hua sun kar. Batao, main kaise help kar sakta hoon?",
    "i am bored": "Chalo kuch naya seekhte hain ya koi fun fact sunu?",
    "tell me a joke": "Ek programmer bola: 'Tum meri life ka semicolon ho,' kyunki tum har statement ko complete karti ho!",

    "order status": "Apna order number bataye, main status check kar deta hoon.",
    "where is my package": "Aapka package transit mein hai. Delivery date jaldi update hogi.",
    "change delivery address": "Order number aur naya address bataye, main update karwa deta hoon.",
    "return policy": "Return policy 30 days ki hai. Product original packing mein hona chahiye.",
    "how to get a refund": "Return request submit karein. Product milne ke baad 5-7 working days mein refund aa jayega.",
    "cancel order": "Kya aap sach mein order cancel karna chahte hain? Order number confirm karein.",
    "product price": "Kaunsa product? Naam bataye.",
    "is the item in stock": "Haan, item currently stock mein available hai.",
    "delivery time": "Normally delivery 3-5 working days mein ho jati hai.",
    "speak to an agent": "Sorry, main direct agent se connect nahi kara sakta, par aapko callback priority par milega.",
    "i have a complaint": "Mujhe afsos hai. Complaint detail mein bataye, main record kar deta hoon.",
    "how to reset password": "'Forgot Password' par click karein, aapko email aa jayega.",
    "bill payment issue": "Payment fail hua ya amount cut gaya lekin bill update nahi hua?",
    "nearest store location": "Aapka pin code bataye, main nearby store bata deta hoon.",
    "warranty period": "Is product par 1 year ki standard warranty hoti hai.",

    "system slow": "System slow chal raha hai? Kya recently koi heavy software install kiya ya tabs jyada khule hain?",
    "internet not working": "Kya router on hai? Ek baar restart kar ke dekhein.",
    "error code 404": "404 ka matlab hota hai page nahi mila. URL check karein.",
    "how to clear cache": "Browser settings → Privacy & Security → Clear cache.",
    "software update failed": "Ensure karein ki disk space aur stable internet ho.",
    "forgot username": "Aapka linked email ya phone number bataye.",
    "printer not connecting": "Printer USB se connected hai ya Wi-Fi se? Driver installed hai?",
    "my phone is frozen": "Power + Volume Down 10 seconds tak press karein, phone restart ho jayega.",
    "backup data": "Cloud storage ya external hard drive me backup lein.",
    "what is a VPN": "VPN aapke internet ko encrypt karke privacy badhata hai.",
    "what is api": "API ek interface hota hai jisse do software apps interact karte hain.",
    "what is html": "HTML ek markup language hai jo web pages banane ke liye use hoti hai.",
    "what is a bug": "Bug programming error hoti hai jisse program expected tarike se kaam nahi karta.",
    "how to install driver": "Driver manufacturer ki official website se download karke install karen.",
    "need a good antivirus": "Top antiviruses: Norton, Bitdefender, Kaspersky.",

    "set a reminder": "Kis cheez ka reminder chahiye aur kis time par?",
    "check my schedule": "Aaj aapki 4 PM team meeting aur 6 PM customer call hai.",
    "next meeting time": "Aapki next meeting kal 10:30 AM project planning ki hai.",
    "book an appointment": "Kis date aur kis purpose ke liye appointment chahiye?",
    "is the manager available": "Manager meeting mein hain. Kya koi message dena chahte hain?",
    "what is my deadline": "'Final report' ki deadline iss Friday 5 PM tak hai.",
    "where is the conference": "Conference Hall B (1st floor) mein hai.",
    "send a follow up email": "Kisko aur kis subject par follow-up email bhejna hai?",

    "suggest a good book": "'The Alchemist' ek bahut inspiring fiction book hai.",
    "what is the weather": "Aapka city name bataye, main weather bata deta hoon.",
    "latest news headlines": "Kaunse topic ki news chahiye?",
    "what is inflation": "Inflation ka matlab hai cheezon ki prices badhna aur paise ki value kam hona.",
    "tell me about mars": "Mars hamara 4th planet hai jise Red Planet bhi kehte hain.",
    "define AI": "AI wo technology hai jo machines ko human-like intelligence deti hai.",
    "how to save money": "Budget banaye, extra expenses kam karein, aur 10-20% saving karein.",
    "best place to travel": "Aapko mountains pasand hain, beach ya historical places?",
    "what is quantum computing": "Quantum computing quantum mechanics ka use karke complex problems solve karti hai.",
    "who is the CEO": "Kaunsi company ka CEO jana hai? Naam bataye.",

    "difference between compiler and interpreter": "Compiler pura code ek baar me convert karta hai, interpreter line-by-line execute karta hai.",
    "what is polymorphism": "Polymorphism ka matlab hai ek interface ka multiple forms me use hona.",
    "explain data structure": "Data structure data ko efficiently store aur manage karne ka tarika hai (Array, Stack, Queue, etc).",
    "what is normalization in dbms": "Normalization redundant data ko kam karta hai aur dependencies ko improve karta hai.",
    "what is recursion": "Recursion me function khud ko call karta hai jab tak base condition poori na ho.",
    "what is object oriented programming": "OOP class aur objects par based hota hai jisme data aur methods ek saath hote hain.",
    "what is stack and queue": "Stack LIFO hota hai, Queue FIFO hota hai.",
    "explain agile methodology": "Agile ek flexible software development approach hai jo feedback aur improvement par focus karti hai.",
    "what is git": "Git distributed version control system hai jo code changes track karta hai.",
    "what is cloud computing": "Cloud computing internet par servers, storage, database, networking provide karta hai.",
    "what is subnetting": "Subnetting ek bade network ko chhote manageable parts me divide karta hai.",
    "what is an operating system": "OS hardware aur software resources ko manage karta hai.",
    "difference between call by value and call by reference": "Call by value me copy jaati hai, call by reference me memory address jaata hai.",
    "what is constructor": "Constructor ek special method hota hai jo object create hote hi initialize karta hai.",
    "what is inheritance": "Inheritance me ek class doosri class ke properties aur methods ko inherit karti hai.",

    "how to start coding": "Ek easy language (Python/JS) choose karo, tutorials dekho, projects banao.",
    "which programming language is best": "Python beginners ke liye best hai, Java enterprise apps ke liye.",
    "how to make a good resume": "Resume short rakho (1-2 pages), skills, experience aur achievements clear rakho.",
    "what are soft skills": "Soft skills = communication, teamwork, problem-solving, time management.",
    "how to prepare for interview": "Company research karo, technical skills revise karo, HR questions practice karo.",
    "how to learn python fast": "Basics seekho, coding challenges karo, ek mini project banao.",
    "how to do project planning": "Goals set karo, tasks divide karo, deadline aur resources plan karo.",
    "how to debug code": "Print statements use karo ya debugger se step-by-step code chalao.",
    "what is version control": "Version control code changes track karta hai over time.",
    "can you explain big o notation": "Big O algorithm ki complexity aur performance measure karta hai."
}

#Method/Function to get response of ChatBot
def getResponseOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "I am not able to tell taht yet. mai jald hi ye sikh lunga"
#Take user input
while True:
    userInput = input("Please ask your Question: ")
    reply = getResponseOfBot(userInput)
    print("Bot Response :", reply)
    if "bye" in userInput.lower():
     break