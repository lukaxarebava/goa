# 1) input

# პირველი დავალება --- 
# მომხმარებელმა უნდა შემოიტანოს რიცხვი 1 - დან 1000 - მდე, თქვენი მიზანია, რომ გამოიცნოთ შემოტანილი რიცხვი, თუ სწორი იქნება დაპრინტეთ 'სწორია!', ხოლო თუ არასწორია, დაპრინტეთ ;არასწორია!'


# number = int(input("enter number:"))

# correct_num = 100

# result = correct_num == number

# print("your answer is", result)


# მეორე დავალება ---

# დაწერეთ პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს ნივთების რაოდენობა, რომლის შეძენაც სურს.
# დარწმუნდით, რომ მომხმარებელი შეიყვანს დადებითი რიცხვს.
# თითოეული ნივთისთვის, შესთავაზეთ მომხმარებელს შეიყვანოს ფასი.
# დარწმუნდით, რომ მომხმარებელი შეიყვანოს დადებითი რიცხვს პროდუქტის ფასისთვის.
# გამოთვალეთ და აჩვენეთ ყველა ელემენტის მთლიანი ღირებულება.


# item = int(input("sheiyvanet nivtebis raodenoba:"))
# price = int(input("sheiyvanet fasi:"))
# print(item * price)



# 2) შედარებითი ოპერატორები

# გააკეთეთ 10 მაგალითი შედარებით ოპერატორებზე.


# print(200 > 1)
# print(1 > 200)
# print(485 > 205)
# print(836 < 1194)
# print(30 > 25)
# print(74 >= 74)
# print(430 <= 945)
# print(7495 <= 7495)
# print(8471 == 8471)
# print(7402 == 863)



# პირველი დავალება ---
# დაწერეთ პროგრამა,  რათა შეამოწმოთ, აქვს თუ არა მომხმარებელს ფასდაკლების უფლება მისი ასაკისა და შესყიდვის მთლიანი თანხის მიხედვით. შესთავაზეთ მომხმარებელს შეიყვანოს მათი ასაკი და შესყიდვის მთლიანი თანხა. დარწმუნდით, რომ მომხმარებელი შეიყვანს დადებითი რიცხვს ასაკისა და შესყიდვის თანხისთვის. გამოიყენეთ შემდეგი ფასდაკლების წესები: 60 წელზე უფროსი ასაკის მომხმარებლებს შეუძლიათ ისარგებლონ ფასდაკლებით.
# კლიენტებს, რომლებიც ხარჯავენ $100 ან მეტს, შეუძლიათ მიიღონ ფასდაკლება. 60 წელზე უფროსი ასაკის მომხმარებლები და 100 დოლარი ან მეტი დახარჯული აქვთ უფრო მაღალი ფასდაკლების უფლება. მომხმარებლისთვის აჩვენეთ შეტყობინება, რომელშიც მითითებულია, შეუძლიათ თუ არა მას ფასდაკლება და ფასდაკლების ოდენობა, თუ ეს შესაძლებელია.


# age = int(input("enter your age"))
# money = int(input("enter money"))

# result = age > 60 or money > 100 or age > 60 and money >= 100
# print(result)

# 4) მონაცემთა ტიპები


# შემოიტანეთ სხვადასხვა ცვლადები, რომლებსაც ექნებათ სხვადასხვა მონაცემთა ტიპი, შემდგომ შეამოწმეთ ეს ტიპები.


# num = 24

# name = "luka"

# height = 167.8

# is_student = True

# print(type(num))

# print(type(name))

# print(type(height))

# print(type(is_student))







# დაწერეთ პროგრამა, რომელიც მოუწოდებს მომხმარებელს შეიყვანოს წონა (კილოგრამებში) და სიმაღლე (მეტრებში). გამოთვალეთ სხეულის მასის ინდექსი (BMI) ფორმულის გამოყენებით: BMI = წონა
#  / (სიმაღლე * სიმაღლე). გამოთვლილი BMI-დან გამომდინარე, მიაწოდეთ მომხმარებლის ჯანმრთელობის შეტყობინება: თუ BMI 18.5-ზე ნაკლებია, აჩვენეთ "Underweight". თუ BMI არის 18.5-დან 24.9-მდე,
# ჩვენება "ნორმალური წონა". თუ BMI არის 25-დან 29.9-მდე, აჩვენეთ "Overweight". თუ BMI არის 30 ან მეტი, აჩვენეთ "სიმსუქნე". აჩვენეთ გამოთვლილი BMI და ჯანმრთელობის შეტყობინება გამოყენებისთვის



# height = int(input("enter your height:"))
# weight = int(input("enter your weight:"))

# height_m = height / 100

# BMI = weight / (height_m * height_m)


# if BMI < 18.5:
#     print("underweight")

# elif BMI > 18.5 and BMI < 24.9:
#     print("normal weight")

# elif BMI > 25 and BMI < 29.9:
#     print("overweight")

# else :
#     print("simsuqne")


# print(BMI)


# დაწერეთ პროგრამა, რათა შეამოწმოთ, არის თუ არა სტუდენტი უფლებამოსილი სტიპენდიის მისაღებად მათი აკადემიური მოსწრებისა და ოჯახის შემოსავლის მიხედვით. სთხოვეთ მომხმარებელს შეიყვანოს
# თავისი GPA (საშუალო ქულა) და ოჯახის შემოსავალი. დარწმუნდით, რომ მომხმარებელი შეიყვანს დადებითრიცხვებს. გამოიყენეთ შემდეგი დასაშვებობის კრიტერიუმები: სტუდენტები GPA 3.
# 5 ან მეტი ადამიანი უფლებამოსილია სტიპენდიის მისაღებად. სტუდენტები, რომლებსაც აქვთ GPA 3.0 ან მეტი და ოჯახის შემოსავალი $50,000-ზე ნაკლები, შეუძლიათ მიიღონ უმაღლესი სტიპენდია.
#  სტუდენტები, რომლებსაც აქვთ GPA 3.0-ზე დაბალი, არ შეუძლიათ სტიპენდიის მიღება. მომხმარებლისთვის აჩვენეთ შეტყობინება, რომელშიც მითითებულია, რამდენად შეუძლიათ სტიპენდიის მიღება
#  და სტიპენდიის ოდენობა, თუ ეს შესაძლებელია.


# gpa = int(input("enter your gpa:"))
# ojaxis_shemoshavali = int(input("enter your ojaxis shemoshavali:"))

# if ojaxis_shemoshavali < 50000 and gpa >= 3:
#     print("umaglesi stimendia")


# elif gpa < 3:
#     print("ar gaqvt stipendia") 
          




