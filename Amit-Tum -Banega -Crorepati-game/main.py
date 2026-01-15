a="Welcome to Tum Banega Crorepati!"
print(a.center(100))
b=input("Enter your name: ")
print(f"Hello, {b}! Let's play Tum Banega Crorepati!")
print("Here are the rules of the game:")
print("1. You will be asked a series of multiple-choice questions.")
print("2. Each correct answer will earn you money and take you closer to the grand prize of 1 crore!")
print("3. You can use lifelines if you get stuck on a question.")
print("4. Answer carefully and think before you respond.")
print("Let's get started! Good luck!")
q = [
    [ "1.International Literacy Day is observed on?", "Sep 8", "Nov 28", "May 2", "Sep 22", "Sep 8"],
    [ "2.The language of Lakshadweep, a Union Territory of India?", "Tamil", "Hindi", "Malayalam", "Telugu", "Malayalam"],
    [ "3.In which group of places the Kumbha Mela is held every twelve years.?", "Ujjain / Puri / Prayag / Haridwar", "Prayag / Haridwar / Ujjain / Nasik", "Rameshwaram / Puri / Badrinath / Dwarika", "Chittakoot / Ujjain / Prayag / Haridwar", "Prayag / Haridwar / Ujjain / Nasik"],
    ["4.Bahubali festival is related to?", "Hinduism", "Buddhism", "Jainism", "Sikhism", "Jainism"],
    ["5. Which day is observed as the World Standards Day?", "Oct 14", "Nov 15", "Dec 10", "Sep 20", "Oct 14"],
    ["6. Which of the following was the theme of the World Red Cross and Red Crescent Day?", 'Dignity for all - focus on women', 'Dignity for all - focus on Children', 'Focus on health for all', 'Nourishment for all-focus on children', 'Dignity for all - focus on Children'],
    ["7. September 27 is celebrated every year as?", "World Tourism Day", "World Heart Day", "World Maritime Day", "World Rabies Day", "World Tourism Day"],
    ["8. Who is the author of 'Manas Ka-Hans' ?", "Kishorilal Goyal", "Amrit Lal Nagar", "Rabindranath Tagore", "Mahatma Gandhi", "Amrit Lal Nagar"],
    ["9. The death anniversary of which of the following leaders is observed as Martyrs Day?", "Jawaharlal Nehru", "Sardar Patel", "Bhagat Singh", "Mahatma Gandhi", "Mahatma Gandhi"],
    ["10. Who is the author of the epic Meghdoot?", "Kalidas", "Vyasa", "Valmiki", "Bhasa", "Kalidas"],
    ["11. 'Good Friday' is observed to commemorate the event of?", "The crucifixion of Jesus Christ", "The resurrection of Jesus Christ", "The birth of Jesus Christ", "The ascension of Jesus Christ", "The crucifixion of Jesus Christ"],
    ["12. Who is the author of the book 'Amrit Ki Ore'?", "Ramdhari Singh Dinkar", "Harivansh Rai Bachchan", "Suryakant Tripathi Nirala", "Narendra Mohan", "Narendra Mohan"],
    ["13. The headquarters of the International Red Cross Society is located at?", "Geneva", "New York", "The Hague", "Paris", "Geneva"],
    ["14. Who is known as the 'Father of the Indian Constitution'?", "B.R. Ambedkar", "Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "B.R. Ambedkar"],
    ["15. The Indian National Congress session held in December 1920 at which of the following places adopted the Non-Cooperation Movement?", "Nagpur", "Calcutta", "Madras", "Delhi", "Nagpur"],
    ["15. Pongal is a popular festival of which state?", "Tamil Nadu", "Kerala", "Andhra Pradesh", "Karnataka", "Tamil Nadu"],
    ["16. Who among the following was not a recipient of the Bharat Ratna award?", "Satyajit Ray", "Mother Teresa", "Lata Mangeshkar", "A.P.J. Abdul Kalam", "Lata Mangeshkar"],
    ["17. The headquarters of the World Health Organization (WHO) is located at?", "Geneva", "New York", "London", "Paris", "Geneva"],
    ["18. Who is the author of the book 'Gitanjali'?", "Rabindranath Tagore", "Kazi Nazrul Islam", "Sarojini Naidu", "Bankim Chandra Chatterjee", "Rabindranath Tagore"],
    ["19. The famous 'Khajuraho Temples' are located in which state of India?", "Madhya Pradesh", "Uttar Pradesh", "Rajasthan", "Gujarat", "Madhya Pradesh"],
    ["20. Who is known as the 'Missile Man' of India?", "Dr. A.P.J. Abdul Kalam", "Dr. B.R. Ambedkar", "Dr. S. Radhakrishnan", "Dr. C.V. Raman", "Dr. A.P.J. Abdul Kalam"]
]
levels = [1000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 20000000, 40000000, 80000000, 150000000, 300000000, 500000000, 1000000000]
money = 0
for i in range(len(q)):
    question = q[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"{question[0]}")  # Question text is now at index 1
    print(f"1.{question[1]}                                2.{question[2]}")
    print(f"3.{question[3]}                                4.{question[4]}")
    answer = int(input("Enter your answer (1-4) or 0 to quit: "))
    if answer==0:
        money=levels[i-1]
        print(f"finally you are going home with Rs.{money}")
        print ("congratulations")
        print("Thank you for playing Kaun Banega Crorepati!")
        break
    elif answer==1:
        if question[1]==question[5]:
            money=levels[i]    
            print(f"Correct answer! You have won Rs.{money}")
        else:
            print("Wrong answer. Game over!")
            print("You are going home with Rs.3000")
            print("Thank you for playing Kaun Banega Crorepati!")
            break    
    elif answer==2:
        if question[2]==question[5]:
            money=levels[i]    
            print(f"Correct answer! You have won Rs.{money}")
        else:
            print("Wrong answer. Game over!")
            print("You are going home with Rs.3000")
            print("Thank you for playing Kaun Banega Crorepati!")
            break    
    elif answer==3:
        if question[3]==question[5]:
            money=levels[i]    
            print(f"Correct answer! You have won Rs.{money}")
        else:
            print("Wrong answer. Game over!")
            print("You are going home with Rs.3000")
            print("Thank you for playing Kaun Banega Crorepati!")
            break
    elif answer==4:
        if question[4]==question[5]:
            money=levels[i]    
            print(f"Correct answer! You have won Rs.{money}")
        else:
            print("Wrong answer. Game over!")
            print("You are going home with Rs.3000")
            print("Thank you for playing Kaun Banega Crorepati!")
            break
    else:
        print("Wrong answer. Game over!")
        print("You are going home with Rs.3000")
        print("Thank you for playing Kaun Banega Crorepati!")
        break
