#TASK 1: CURRENT AFFAIRS REPORT


current_affairs={
    "politics":81,
    "health":76,
    "technology":67,
    "enternment":81,
    "cybersecurity":90,
    "sports":79,
    "science":89,
    "agriculture":70,
    "buisness": 56
}
# DISPLAY INFO
def display():
     for topic , score in current_affairs.items():
         print(f"The topic is {topic} and score is {score}")

        
#HIGHEST SCORE
def highest_topic ():
     topic = max(current_affairs, key=current_affairs.get) 
     print(f"The highest score is of{topic} = {current_affairs[topic]}")

# LOWEST SCORE   
def lowest_topic ():
     topic = min(current_affairs, key=current_affairs.get) 
     print(f"The lowest  score is of{topic} = {current_affairs[topic]}")


#AVERAGE 
def average_score():
    total=0
    for topic,score in current_affairs.items():
        total+=score
        average=total/len(current_affairs)
    print(f"The avaerage is {average}")

average_score()


#SCORE GREATER THE 70
def score_greater_than_70():
     for topics,score in current_affairs.items():
         if score>=70:
             print(f"The topics having score greater than 70 are {topics}={score}")
score_greater_than_70()
            

def main():
    print("CURRENT AFFAIRS COMPLETE REPORT")

    display()
    highest_topic()
    lowest_topic()   
    average_score()
    score_greater_than_70()  
       

main()    

#----------------------------------------------------------------------------------------------------

#TASK 2 = INDIAN STOCK MARKET ANALYZER

companies={
    "TCS":3000,
    "Infosys" : 5000, 
    "Reliance" :6500  ,
    "HDFC" : 5400
}

#display stock

def display():
    for name , stock in companies.items():
        print(f"The company is {name} stock is {stock}")
#display()


#highest stock price 
def highest_stock_price():
    
        name=max(companies,key=companies.get)
        print(f"The company having highest stock is {name} and is {companies[name]}")

#highest_stock_price()

#LOWEST STOCK PRICE 

def lowest_stock_price():
     name=min(companies,key=companies.get)
     print(f"The lowest is of {name} is {companies[name]}")
     
#lowest_stock_price()

# AVERAGE 

def average():
     total=0
     for name ,stock in companies.items():
          total+=stock
          average=total/len(companies)
     print(f"The average is:{average}")
#average()


#stocks as High, Medium or Low based on price.

def classify():
     for name , stock in companies.items():
          if stock>5000:
               print(f"{name} is having high stock")
          elif 4000<stock <=5000:
               print(f"{name} is having medium stock")
          else:
               print(f"{name} is having low stock")

def main ():
     print("STOCK MARKET SUMMARY")
     display()
     highest_stock_price()
     lowest_stock_price()
     average()
     classify()

main()     
#-----------------------------------------------------------------------------------------------

#TASK 3: CRICKET PERFORMANCE ANALYZER

players={
    "virat kholi" : 100,
    "rohit sharma" : 87,
    "shubnam gill" : 76 ,
    "hardik pandya" : 56 ,
    "abhishek sharma" : 67,
    "shreyas iyer" : 45,
    "kl rahul" : 67,
    "jaspreet" : 23,
    "vaishav suryavanshi" : 44,
    "akshar patel" : 12
}

def display():
    for name,runs in players.items():
        print(f"{name} has scored {runs} runs")
#display()

#highest score 
def highest_score():
    name=max(players,key=players.get)
    print(f"The highest score is of {name} , score is {players[name]}")
#highest_score()


# lowest score 

def lowest_score():
    name=min(players,key=players.get)
    print(f"The lowest score is of {name} ,score is {players[name]}")
#lowest_score()

def average():
    total=0
    for name , runs in players.items():
        total+=runs
        average=total/len(players)
    print(f"The average is {average}")
#average()

def above_average():
    a = sum(players.values()) / len(players)
    for name,runs in players.items():
        if runs> a :
            print(f"{name} has scored runs above averge = {runs}")
#above_average()       

def main():
    print("PLAYERS PERFORMANCE REPORT ")
    display()
    highest_score()
    lowest_score()
    average()
    above_average()
main()         
#---------------------------------------------------------------------------------------------------

#TASK 4: IPL PLAYER PERFORMANCE ANALYZER           

players={
    "virat kohli" :{
        "runs" : 650,
        "matches" : 13
    },
    "rohit sharma":{
        "runs" : 480,
        "matches":14
    },
    "shubmsn gill":{
        "runs":720,
        "matches":14
    },
    "hardik pandey":
    {
        "runs": 290,
        "matches": 12
    }
}

# #runs per match 

def runs_per_match():
    performance={}
    for name,data in players.items():
        rpm=data["runs"] / data["matches"]
        performance[name]=rpm
    print("runs per match:")    
    print(performance)
#runs_per_match()

# # best performing batsman
def best():
    runs={}
    for name , data in players.items():
        runs[name]=data["runs"]
    a=max(runs,key=runs.get)
    print(f"{a} is best batsman with runs {runs[a]}")
#best()

def low():
    runs_count={}
    for name , data in players.items():
        runs_count[name]=data["runs"]
    low=min(runs_count,key=runs_count.get)    
    print(f"the {low} is lowest performing with runs {runs_count[low]}")
#low()

# teams average runs
def team_average():
    total = 0
    for data in players.values():
        total += data["runs"]

    avg = total / len(players)
    print(f"\nTeam Average Runs: {avg:.2f}")
#team_average()    


def classify():
    test={}
    for name , data in players.items():
        test[name]=data["runs"]
        if data["runs"]>=700:
            print(f"{name} has ecxellent performance. ")
        elif data["runs"] >=500:
            print(f"{name} has good performance")
        elif  data["runs"]>=300:
            print(f"{name} has average performance")    
        else:
            print(f"{name} has poor performance")

#classify()
def main (): 
    print("COMPLETE REPORT : ")
    runs_per_match()
    best()
    low()
    team_average()
    classify()
main()

#-------------------------------------------------------------------------------------------------------
# # TASK 5 GOLD PRICE ANALYZER                                      [LIST]
gold_price=[9976,6789,9908,7896,8900,
            9753,9021,9765,8543,7690,
            9000,9210,8901,9654,8901]
#print(gold_price)

def average():
    avg = sum(gold_price) / len(gold_price)
    print(f"Average gold price: {avg:.2f}")
#average()    

#HIGHEST PRICE

def highest():
    highest=max(gold_price)
    print(f"the highest gold price is : {highest}")
#highest()

#lowest price

def lowest():
    lowest=min(gold_price)
    print(f"the lowest gold price is : {lowest}")
#lowest()

#price change in consecutive days

def price_change():
    for i in range (1,len(gold_price)):
        change=gold_price[i] - gold_price[i-1]
        print(f"From {i} to {i+1} = {change}")
#price_change()



def main():
    average()
    highest()
    lowest()
    price_change()
main()    
    
    

#-----------------------------------------------------------------------------------------------------
 #TASK 6 WEATHER DATA ANALYZE                                          
city_temperature={
    "nashik":23,
    "pune":30,
    "mumbai":44,
    "delhi":50,
    "kolkata" : -13,
    "bangluru" : 10
}

def average_temp():
    average=sum(city_temperature.values())/len(city_temperature)
    print(f"the average is :{average}")
average_temp()

#hottest city 
def hottest_city():
    for name , temp in city_temperature.items():
        name=max(city_temperature,key=city_temperature.get)
    print(f"The hootest city is : {name}")
#hottest_city()

#coolest city

def coldest_city():
    for name , temp in city_temperature.items():
        cold=min(city_temperature,key=city_temperature.get)
    print(f"The colest city is {cold}")
#coldest_city()

#max temp 

def temp():
    
    max_temperature=max(city_temperature,key=city_temperature.get)
    min_temperature=min(city_temperature,key=city_temperature.get)
    print(f"The max temp is {city_temperature[max_temperature]}")
    print(f"The minimum tem is : {city_temperature[min_temperature]}")
#temp()
#classfy
def classfy():
    for name , temp in city_temperature.items():
        if temp >40:
            print(f"{name} has hot temperature")
        elif temp >=20:
            print(f"{name} has moderate tempature")
        else :
            print(f"{name} has cold tempareture")
#classfy()

def main():
    print("WHETHER REPORT : ")
    average_temp()
    hottest_city()
    coldest_city()
    temp()
    classfy()
main()
# ------------------------------------------------------------------------------------------------------
# TASK 7: ELECTION SURVEY DATA ANALYZER

election={
    "BJP": 200,
    "shiv sena" : 300,
    "CJP" : 800 ,
    "abc" : 500,
    "xyz" : 450,
    "wer" : 345,
    "other" : 100
}

def total():
    total=0
    for name, votes in election.items():
        total+=votes
    print(f"The total votes are : {total}")
#total()

#vote per of each candidate 
def per():
    
    percentage={}
    total=0
    for candidate ,votes in election.items():
        total+=votes
        per=(votes/total)*100
        percentage[candidate]=round(per,2)
    print(percentage)
#per()

#candidate with highest score 
def highest():
    highest=max(election,key=election.get)
    print(f"{highest} has highest votes = {election[highest]}")
highest()
def lowest():
    lowest=min(election,key=election.get)
    print(f"{lowest} has lowest votes = {election[lowest]}")
#lowest()        

#rank according to votes
def get_rank(x):
    return x[1]

def rank():
    count=len(election)
    i=0
    sorted_list=sorted(election.items(),key=get_rank,reverse=True)

    for j in sorted_list:
        i=i+1
        print(f"Rank {i} = {j[0]} ,{j[1]}")
#rank()

def main():
    print("ELECTION SURVEY REPORT : ")
    total()
    per()
    highest()
    lowest()
    rank()
main()

#----------------------------------------------------------------------------------------------
#TAST 8 = POPULATION DATA ANALYZER


states = {
    "Maharashtra": 125,
    "Uttar Pradesh": 240,
    "Bihar": 130,
    "West Bengal": 100,
    "Madhya Pradesh": 85,
    "Tamil Nadu": 80,
    "Rajasthan": 82,
    "Karnataka": 70,
    "Gujarat": 72,
    "Odisha": 47
}
#total population
def total():
    total=0
    for name,population in states.items():
        total+=population
    print(f"the total population is {total}")
#total()    

#average population

def average():
    total=0
    for name,population in states.items():
        total+=population
        average=total/len(states)
    print(f"The average is {average}")
#average()

#most populated state
def most_populated():
    for name,population in states.items():
        name=max(states,key=states.get)
    print(f"The {name} has highest population = {states[name]} ")
#most_populated()

#least populated
def least_populated():
    for name ,population in states.items():
        name=min(states,key=states.get)
    print(f"The {name} has least population = {states[name]}")
#least_populated()
def above_limit():
    limit=100
    print(f"States with population above {limit}")
    for state, population in states.items():
        if population > limit:
            print(state, "-", population)
#above_limit()

#sort state according to population

#def sort():
    
    sorted_states = sorted(
        states.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for state, population in sorted_states:
        print(f"{state}: {population}")

#population report

def main():
    print(f"THE POPULATION REPORT : ")
    total()
    average()
    most_populated()
    least_populated()
    above_limit()

main()    

#-----------------------------------------------------------------------------------------------------
#TASK 9 UNEMPLOYMENT DATA ANALYZER

states = {
    "Maharashtra": 5.2,
    "Gujarat": 3.8,
    "Karnataka": 4.5,
    "Tamil Nadu": 6.1,
    "Rajasthan": 7.4,
    "Uttar Pradesh": 8.2,
    "Bihar": 9.5,
    "Punjab": 5.8,
    "Kerala": 6.7,
    "Odisha": 4.9
}

#display info
def display():
    for name,value in states.items():
        print(f"{name} has {value} % of unemployment")
#display()

#average unemployment

def average():
    total=0
    for name,values in states.items():
        total+=values
        average=total/len(states)
    print(f"The average is {average}")
#average()

#highest unemployment
def highest_unemp():
    for name,values in states.items():
        name=max(states,key=states.get)
    print(f"The {name} has highest unemploymet of {states[name]} %")
#highest_unemp()

#lower unemp rate
def lowest_unemp():
    for name,values in states.items():
        name=min(states,key=states.get)
    print(f"The {name} has lowest unemployment of {states[name]} %")
#lowest_unemp()

 #classify unemp as high,medium,low
def classify():
    for name ,value in states.items():
        if value<5:
            print(f"{name} is having low rate of unemployment")
        elif value<7:
            print(f"{name} has medium rate of unemployment")
        else:
            print(f"{name} has high rate of unemplyment")
#classify()

#main

def main():
    print("UNEMPLOYMENT RATE  REPORT :")

    display()
    average()
    highest_unemp()
    lowest_unemp()
    classify()
main()

# ------------------------------------------------------------------------------------------------------------

#TASK 10  AI INDUSTRY GROWTH ANALYZER

ai_growth = {
    "Generative AI": 35,
    "Computer Vision": 18,
    "Robotics": 22,
    "NLP": 28,
    "AI Healthcare": 25,
    "AI Finance": 20
}

#average growth

def average_growth():
    total=0
    for name,value in ai_growth.items():
        total+=value 
        average=total/len(ai_growth)
    print(f"The average is : {average}")
#average_growth()        

#fastest growing sector
def fastest_growing():
    for name,value in ai_growth.items():
        name=max(ai_growth,key=ai_growth.get)
    print(f"The fastest growth is of {name} sector = {ai_growth[name]}")
#fastest_growing()

#slowest growing sector

def slowest_growing():
    for name,value in ai_growth.items():
        name=min(ai_growth,key=ai_growth.get)
    print(f"The slowest growing is {name} sector = {ai_growth[name]}")
#slowest_growing()
        
#growth above 20%
def growth_above_20_per():
    limit=20
    print("The sector having rate above 20 percent are :")
    for name,value in ai_growth.items():
        if value>limit:
            print(f"{name} has grownth rate above 20% ={value}")
#growth_above_20_per()

#to rank sector according to growth 
def get_values(x):
    return x[1]

def rank():
    count=len(ai_growth)
    print("The sectors are ranked as:")
    sorted_sectors=sorted(ai_growth.items(),key=get_values,reverse=True)
    i=1

    for j in sorted_sectors:
        print(f"Rank {i} = {j[0]} - {j[1]}")
        i=i+1

#rank()

# #main

def main():
    print("IA - INDUSTRY REPORT : ")
    average_growth()
    fastest_growing()
    slowest_growing()
    growth_above_20_per()
    rank()
main()

# ---------------------------------------------------------------------------------------------------

# TASK 11 TECHNOLOGY COMPANY REVENUE ANALYZER

companies = {
    "TechNova": 850,
    "InfoSoft": 620,
    "CodeSphere": 940,
    "NextGen": 480,
    "CloudNet": 760,
    "Qspider": 550
}

# #total revenue 
# def total_revenue():
def total_revenue():
    total = sum(companies.values())
    print(f"Total revenue: {total}")
# #total_revenue()

#average revenue
def average():
    total=0
    for name,value in companies.items():
        total+=value
        average=total/len(companies)
    print(f"The average in : {average}")
#average()

# #highest revenue
def highest_revenue():
    name = max(companies, key=companies.get)
    print(f"{name} has the highest revenue of {companies[name]}")
highest_revenue()

def lowest_revenue():
    name = min(companies, key=companies.get)
    print(f"{name} has the lowest revenue of {companies[name]}")
lowest_revenue()


# #rank company based on revenue

def get_revenue(x):
    return x[1]

def rank():
    count=len(companies)
    print("The companies are ranked as :")
    sorted_rank=sorted(companies.items(),key=get_revenue,reverse=True)
    i=1

    for j in sorted_rank:
        print (f"The rank is {i} = {j[0]} - {j[1]}")
        i=i+1
#rank()

# classify according to revenue 

def classify():
    print("The company is classified as : ")
    for name ,value in companies.items():
        if value>=800 :
            print (f"{name} has high revenue")
        elif value >= 600:
            print(f"The {name} has averge revenue")
        else:
            print(f"The {name} has low revenue")

#classify()                     

#main

def main():
    print("THE COMPANY REVENUE REPORT : ")
    total_revenue()
    average()
    highest_revenue()
    lowest_revenue()
    rank()
    classify()
main()

#----------------------------------------------------------------------------------------------------

# TASK 12: CRYPTOCURRENCY MARKET ANALYZER

crypto = {
    "Bitcoin": 65000,
    "Ethereum": 3200,
    "Binance Coin": 600,
    "Solana": 180,
    "Cardano": 1,
    "Dogecoin": 0.25
}

def display():
    for name,value in crypto.items():
        print(f"The {name} = {value}")
#display()

#highest priced currency 
def highest():
    for name ,value in crypto.items():
        name=max(crypto,key=crypto.get)
    print(f"The {name} has highest currency {crypto[name]}")
#highest()

#lowest ranks
def lowest():
    for name ,value in crypto.items():
            name=min(crypto,key=crypto.get)
    print(f"The {name} has lowest  currency {crypto[name]}")

#lowest()


#average

def average():
    total=0
    for name ,value in crypto.items():
          total+=value
          average = total/len(crypto)
    print(f"The average is : {average}")
#average()    

#main 
def main():
     print("CRYPTOCURRENCY MARKET SUMMARY:" )
     display()
     highest()
     lowest()
     average()

main()     
#----------------------------------------------------------------------------------------------------
#TASK 13 GLOBAL OIL PRICE ANALYZER


oil_prices = [
    72, 74, 73, 75, 76,
    78, 77, 79, 80, 81,
    79, 78, 80, 82, 83,
    81, 84, 85, 86, 87
]

#  average price
def average_price():
    total = 0
    for price in oil_prices:
        total += price

    average = total / len(oil_prices)
    print("Average Oil Price:", round(average, 2))
average_price()

#highest price
def high():
    high=max(oil_prices)
    print(f"the highest price is : {high}")
high()

#lowest peice 
def lowest():
    low=min(oil_prices)
    print(f"the lowest price is : {low}")
lowest()

#daily price change 
def price_change():
    a=[]    
    for i in range (1,len(oil_prices)):
        change=oil_prices[i] - oil_prices[i-1]
        a.append(change)
    print(f"the daily change in price are : {a}")    
price_change()

# # identify days where price has increased 
def price_increased():
    for i in range(1, len(oil_prices)):
        if oil_prices[i] > oil_prices[i - 1]:
            change = oil_prices[i] - oil_prices[i - 1]
            print(f"Day {i + 1}: Increased by {change}")

price_increased()            
# --------------------------------------------------------------------------------------------
# TASK14: STUDENT PERFORMANCE ANALYZER

students= {
    "jaee":90,
    "ashmi":89,
    "tanuja":70,
    "rohit":12,
    "pranav" :30,
    "shruti" : 60,
    "laukik":47,
    "bhumika": 79,
    "piyush":-13,
    "anushka": 23


}
# total marks
def total():
    total=0
    for name,marks in students.items():
        total+=marks
    print(f"the total marks are :{total }")    
#total()

#average

def average():
    total=0
    for name,marks in students.items():
        total+=marks
        average=total/len(students)
    print(f"the average is :{average}")
#average()

#topper
def topper():
    for name,marks in students.items():
        name=max(students,key= students.get)
    print(f"The topper is {name} with marks {students[name]}")
#topper()

#lowest marks 

def lowest_marks():
    for name,marks in students.items():
        name=min(students,key=students.get)
    print(f"the student {name} has scored lowest marks = {students[name]}")
#lowest_marks()


#grades

def grade():
    print("Students recieved the grades as:")
    for name,marks in students.items():
        if marks >=80:
            print(f"grade A : {name} = {marks}")
        elif marks >=60:
            print(f"grade B ={name} = {marks}")
        elif marks>=50 :
            print(f"grade C = {name} = {marks}")
        else:
            print(f"grade D = {name} = {marks}")
#grade()


#main

def main():
    print("STUDENT PERFORMANCE REPORT :")
    total()
    average()
    topper()
    lowest_marks()
    grade()
main()

#----------------------------------------------------------------------------------------------------
          
#TASK 15: SOCIAL MEDIA TREND ANALYZER

topics = {
    "AI":  5000,
    "Cricket" : 2000, 
    "Movies": 3000, 
    "Technology":  5500,
    "Education":  6000,
    "Travel": 1000,
}
def total():
    total=0
    for topic,values in topics.items():
        total+=values
    print(f"the total is {total}")

def average():
    total=0
    for topic ,values in topics.items():
        total+=values
        average=total/len(topics)
    print(f"the average is :{average}")

#most trending
def trending():
    for topic,values in topics.items():
        topic=max(topics,key= topics.get)
    print(f"The {topic} is most trending = {topics[topic]}")




def least_trending():
    for topic,values in topics.items():
        topic=min(topics,key=topics.get)
    print(f"the  {topic} is least trending = {topics[topic]}")

#rank
def get_rank(x):
   return x[1]

def rank():
    count=len(topics)
    print("The topics are ranked as :")
    sorted_rank=sorted(topics.items(),key=get_rank,reverse=True)
    i=1

    for j in sorted_rank:
        print (f"The rank is {i} = {j[0]} - {j[1]}")
        i=i+1


def main ():
    print("SOCIAL MIDEA TREND REPORT:")
    total()
    average()
    trending()
    least_trending()
    rank()
main()


#----------------------------------------------------------------------------------------------------------

# PRACTICAL 16: CURRENT AFFAIRS QUIZ ANALYZER

questions = {
    "Capital of India?": "new delhi",
    "Red Planet?": "mars",
    "Currency of Japan?": "yen",
    "National animal of India?": "tiger",
    "Largest ocean?": "pacific ocean",
    "Capital of Maharashtra?": "mumbai",
    "Gas absorbed by plants?": "carbon dioxide",
    "Prime Minister of India?": "narendra modi",
    "Host of 2024 Olympics?": "france",
    "Father of Indian Constitution?": "b r ambedkar"
}

student_answers = {}


# Display questions
def quiz():
    for question in questions:
        print(question)
        answer = input("Enter answer: ").lower()
        student_answers[question] = answer


# Calculate score and count answers
def calculate_score():
    score = 0
    correct = 0
    incorrect = 0

    for question in questions:
        if student_answers[question] == questions[question]:
            score = score + 1
            correct = correct + 1
        else:
            incorrect = incorrect + 1

    print(f"\nScore:{ score}")
    print(f"Correct Answers:{correct}")
    print(f"Incorrect Answers:{ incorrect}")

    # Calculate percentage
def calculate_percentage(score):
    percentage = score * 10
    print(f"Percentage:{percentage}")
    grade(percentage)

# Assign grade
def grade(percentage):
    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 40:
        print("Grade: D")
    else:
        print("Grade: F")


# Main 
def main():
    print("CURRENT AFFAIRS QUIZ REPORT ")
    quiz()
    calculate_score()
    calculate_percentage()
    grade()
    print("\nQuiz Completed!")


main()

#----------------------------------------------------------------------------------------------
#  TASK 17 INDIAN ECONOMY INDICATOR ANALYZER

economy = {
    "GDP Growth": 7.2,
    "Inflation": 5.4,
    "Unemployment": 6.8,
    "Exports": 8.5,
    "Imports": 7.1,
    "Industrial Growth": 6.3
}

#display 

def display():
    for name,values in economy.items():
        print(f"The economy indicator is {name} the value is {values}")

#average indicator value 

def average():
    total =0 
    for name , values in economy.items():
        total+=values
        average=total/len(economy)
    print(f"The Average is : {average}")


#highest indicator value

def highest_indicator_value():
    for name,values in economy.items():
        name=max(economy,key=economy.get)
    print(f"The {name} has highest indicator value of {economy[name]}")


#lowest indicator value

def lowest_indicator_value():
    for name , values in economy.items():
        name=min(economy,key=economy.get)
    print(f"The {name} has lowest indicator value of {economy[name]}")

#classify indicator values

def classify():
    for name,values in economy.items():
        if values>=7.0:
            print(f"{name} has high indicator value")
        elif values>=6.0:
            print(f"{name} has average indicator value")
        else:
            print(f"{name} has low indicator value")


#main
def main():
    print("ECONOMY INDICATOR VALUE REPORT :")

    display()
    average()
    highest_indicator_value()
    lowest_indicator_value()
    classify()
main()

# -------------------------------------------------------------------------------------------------------
# TASK 18: MOVIE AND OTT DATA ANALYZER

movie_OTT ={

    "dhurandar" : {
        "ratings" : 8.5,
        "view count" : 21000
    } , 
    "stranger things" : {
        "ratings" : 9.2 ,
        "view count" : 32100
    },
    "wednesday" : {
        "ratings" : 7.8,
        "view count" : 1200
    },
    "Asur" : {
        "ratings" : 6.8,
        "view count" : 2199
    }
}
# Average rating
def average_rating():
    ratings = []

    for data in movie_OTT.values():
        ratings.append(data["ratings"])

    average = sum(ratings) / len(ratings)
    print(f"Average rating: {average:.2f}")

#  Find highest-rated movie
def highest_rated():
    highest_name = ""
    highest_rating = 0

    for name, data in movie_OTT.items():
        if data["ratings"] > highest_rating:
            highest_rating = data["ratings"]
            highest_name = name

    print("Highest Rated Movie:", highest_name)
    print("Rating:", highest_rating)


#  Find lowest-rated movie
def lowest_rated():
    lowest_name = ""
    lowest_rating = 10

    for name, data in movie_OTT.items():
        if data["ratings"] < lowest_rating:
            lowest_rating = data["ratings"]
            lowest_name = name

    print("Lowest Rated Movie:", lowest_name)
    print("Rating:", lowest_rating)


# Find most-watched movie
def most_watched():
    highest_views = 0
    movie_name = ""

    for name, data in movie_OTT.items():
        if data["view count"] > highest_views:
            highest_views = data["view count"]
            movie_name = name

    print("Most Watched Movie:", movie_name)
    print("Views:", highest_views)



#  Classify movies by rating
def classify():
    for name, data in movie_OTT.items():
        rating = data["ratings"]

        if rating >= 8:
            print(f"{name}: Excellent")
        elif rating >= 7:
            print(f"{name}: Good")
        else:
            print(f"{name}: Average")


#  Mean

def mean(ratings):
    total = 0

    for rating in ratings:
        total = total + rating

    avg = total / len(ratings)
    print("Mean:", round(avg, 2))

def main():
    average_rating()
    highest_rated()
    lowest_rated()
    most_watched()
    classify()
    mean()

main()



# --------------------------------------------------------------------------------------------------

# TASK 19 : DATA SCIENCE JOB MARKET ANALYZER

job_market = {
   " Data Analyst" : 75000 ,
 "Data Scientist" : 90000 ,
 "Machine Learning Engineer" : 95000 ,
 "Data Engineer" : 100000,
 "AI Engineer" : 125000,
 "Business Analyst":50000

}

#average 
def average():
    total=0
    for job , salary in job_market.items():
        total+=salary
        average=total/len(job_market)
    print(f"The average is {average}")
#average()

#highest paying salary 

def highest():
    for job , salary in job_market.items():
        name=max(job_market,key=job_market.get)
    print(f"the {name} is having highest salary of {job_market[name]}")
#highest()        

#lowest paying role

def lowest():
    for job , salary in job_market.items():
        name=min(job_market,key=job_market.get)
    print(f"the {name} having lowest salary {job_market[name]}")    
lowest()        


#salary diff between highest and lowest role

def difference():
    for job , salary in job_market.items():
        highest=max(job_market.values())
        lowest=min(job_market.values())
        diff=highest-lowest
    print(f"The difference in highest and lowest salary is {diff} ")
#difference()    

#rank jobs based on salary

def get_salary(x):
    return x[1]

def rank():
    count=len(job_market)
    print("the rank is given as: ")
    i=1
    sorted_rank=sorted(job_market.items(),key=get_salary,reverse=True)

    for j in sorted_rank:
        print(f"Rank {i} = {j[0]} , {j[1]}")
        i=i+1
#rank()

def main():
    print("DATA SCIENCE CARRER MARKET REPORT : ")
    average()
    highest()
    lowest()
    difference()
    rank()
main()
# ---------------------------------------------------------------------------------------------------------------

# TASK 20 COMPLETE DATA SCIENCE AND CURRENT AFFAIRS ANALYZER










