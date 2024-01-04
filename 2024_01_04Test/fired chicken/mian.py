# 定義class
class FriedChicken:
    # 屬性
    def __init__(self, name, price, ingredients, calories, rating):
        self.name = name            # 定義名稱
        self.price = price          # 定義價格
        self.ingredients = ingredients # 定義成分
        self.calories = calories # 定義卡路里
        self.rating = rating # 定義評分

    # 輸出名稱
    def get_name(self):
        return self.name   
    # 輸出價格
    def get_price(self): 
        return self.price
    # 輸出成分
    def get_ingredients(self):
        return self.ingredients

# 建立四個炸雞物件
chicken1 = FriedChicken('辣味炸雞', 50.0, ['雞肉', '辣椒', '鹽'], 500, 4.5)
chicken2 = FriedChicken('藥膳炸雞', 60.0, ['雞肉', '當歸', '枸杞'], 600, 4.0)
chicken3 = FriedChicken('脆皮炸雞', 45.0, ['雞肉', '麵粉', '鹽'], 450, 4.2)
chicken4 = FriedChicken('香蕉炸雞', 55.0, ['雞肉', '香蕉', '鹽'], 550, 4.8)

# 分別呼叫三個副函式
print(chicken1.get_name())
print(chicken1.get_price())
print(chicken1.get_ingredients())
print("\n") # 換行

print(chicken2.get_name())
print(chicken2.get_price())
print(chicken2.get_ingredients())
print("\n") # 換行

print(chicken3.get_name())
print(chicken3.get_price())
print(chicken3.get_ingredients())
print("\n") # 換行

print(chicken4.get_name())
print(chicken4.get_price())
print(chicken4.get_ingredients())