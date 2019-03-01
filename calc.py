def calc(f,l,p,mShip,mOptimal):
    return (mOptimal/mShip)*((1000*f/l)**(1/p))

class FSD:
    def __init__(self,Class,Rating,mOptimal,f,l,p):
        self.Class = Class
        self.Rating = Rating
        self.f = f
        self.l = l
        self.p = p
        self.mOptimal = mOptimal

all_items = \
[
FSD(2,"E",48,0.6,11,2),
FSD(2,"D",54,0.6,10,2),
FSD(2,"C",60,0.6,8,2),
FSD(2,"B",75,0.8,10,2),
FSD(2,"A",90,0.9,12,2),
FSD(3,"E",80,1.2,11,2.15),
FSD(3,"D",90,1.2,10,2.15),
FSD(3,"C",100,1.2,8,2.15),
FSD(3,"B",125,1.5,10,2.15),
FSD(3,"A",150,1.8,12,2.15),
FSD(4,"E",280,2,11,2.3),
FSD(4,"D",315,2,10,2.3),
FSD(4,"C",350,2,8,2.3),
FSD(4,"B",438,2.5,10,2.3),
FSD(4,"A",525,3,12,2.3),
FSD(5,"E",560,3.3,11,2.45),
FSD(5,"D",630,3.3,10,2.45),
FSD(5,"C",700,3.3,8,2.45),
FSD(5,"B",875,4.1,10,2.45),
FSD(5,"A",1050,5,12,2.45),
FSD(6,"E",960,5.3,11,2.6),
FSD(6,"D",1080,5.3,10,2.6),
FSD(6,"C",1200,5.3,8,2.6),
FSD(6,"B",1500,6.6,10,2.6),
FSD(6,"A",1800,8,12,2.6),
FSD(7,"E",1440,8.5,11,2.75),
FSD(7,"D",1620,8.5,10,2.75),
FSD(7,"C",1800,8.5,8,2.75),
FSD(7,"A",2700,12.8,12,2.75)
]

classin=int(input("Enter The Class of Your FSD (From 2 to 7):"))
ratingin=str(input("Enter The Rating of Your FSD (From A to E):")).upper()
massin=int(input("Please enter your ship mass (in tons):"))
for item in all_items:
    if classin == item.Class and ratingin == item.Rating:
        eng_question = input("Is your drive engineered? (Y/N)").lower()
        if eng_question == "yes" or eng_question == "y":
            eng_rating = int(input("What is your optimal mass percentage?:"))
            item.mOptimal = item.mOptimal * (eng_rating/100)
        print("Your Jump Range is {} ly".format(round(calc(item.f, item.l, item.p, massin, item.mOptimal), 2)))




