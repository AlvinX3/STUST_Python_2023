# 定義 employer class
class employer():
    def __init__(self, employer_name, employer_YearSalary, employer_hour):
        super().__init__()
        self.employer_name = employer_name  # 員工名稱
        self.employer_YearSalary = employer_YearSalary  # 年薪
        self.employer_hour = employer_hour  # 時薪
    
    def get_employer_info(self):
        return f"Name: {self.employer_name}\nYear salary: {self.employer_YearSalary}\nhour(monthly): {self.employer_hour}\n"


# 定義 drink class
class drink():
    def __init__(self, price, rating, hot_or_ice):
        super().__init__()
        self.price = price  # 價格
        self.rating = rating # 評分
        self.hot_or_ice = hot_or_ice

    

# 定義 cold_drink class，繼承自 drink class
class cold_drink(drink):
    def __init__(self, price, name, ice, suger, hot_or_ice, rating):
        super().__init__(price, hot_or_ice, rating) 
        self.name = name  # 飲料名稱
        self.ice = ice  # 冰塊量
        self.suger = suger  # 糖分量



    def drink_info(self):
        return f"Name: {self.name}\nIce: {self.ice}\nSugar: {self.suger}\nPrice: {self.price}\nhot or cold: {self.hot_or_ice}\n"

    # 定義副函式 change_name 用於變更名稱
    def change_name(self, new_name):
        print("----old info----")
        print(self.drink_info()) # 先輸出一次飲料資訊
        self.name = new_name
        print("----new info----")
        print(self.drink_info()) # 再輸出一次飲料資訊
    
    # 定義副函式 change_suger 用於變更甜度
    def change_suger(self, new_suger):
        print("----old info----")
        print(self.drink_info()) # 先輸出一次飲料資訊
        self.name = new_suger
        print("----new info----")
        print(self.drink_info()) # 再輸出一次飲料資訊
    
    # 定義副函式 change_price 用於變更價格
    def change_price(self, new_price):
        print("----old info----")
        print(self.drink_info()) # 先輸出一次飲料資訊
        self.name = new_price
        print("----new info----")
        print(self.drink_info()) # 再輸出一次飲料資訊


# 定義 hot_drink class，繼承自 drink class
class hot_drink(drink):
    def __init__(self, price, name, suger, hot_or_ice, rating):
        super().__init__(price, hot_or_ice, rating) 
        self.name = name  # 飲料名稱
        self.suger = suger  # 糖分量

    def drink_info(self):
        return f"Name: {self.name}\nSugar: {self.suger}\nPrice: {self.price}\nhot or cold: {self.hot_or_ice}\nRating: {self.rating}\n"
    
    # 定義副函式 change_name 用於變更名稱
    def change_name(self, new_name):
        print("----old info----")
        print(self.drink_info()) # 先輸出一次飲料資訊
        self.name = new_name
        print("----new info----")
        print(self.drink_info()) # 再輸出一次飲料資訊
    
    # 定義副函式 change_suger 用於變更甜度
    def change_suger(self, new_suger):
        print("----old info----")
        print(self.drink_info()) # 先輸出一次飲料資訊
        self.name = new_suger
        print("----new info----")
        print(self.drink_info()) # 再輸出一次飲料資訊
    
    # 定義副函式 change_price 用於變更價格
    def change_price(self, new_price):
        print("----old info----")
        print(self.drink_info()) # 先輸出一次飲料資訊
        self.name = new_price
        print("----new info----")
        print(self.drink_info()) # 再輸出一次飲料資訊

# 測試 employer class
employer1 = employer('John', 50000, 20)
print(employer1.get_employer_info())

# 測試 cold_drink class
cold_drink1 = cold_drink(50, 'lemon tea', 'less', 'half','cold',5)
print(cold_drink1.drink_info())
cold_drink1.change_name("black tea") # 變更名子


# 測試 hot_drink class
hot_drink1 = hot_drink(30, 'coffee', 'full', 'hot', 5)
print(hot_drink1.drink_info())
hot_drink1.change_name("lemon tea") # 變更名子
