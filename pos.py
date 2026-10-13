class product:
  def __init__(self,name,price,quantity):
    self.name=name
    self.__quantity=quantity
    self.__price=price
  def displayinfo(self):
      print(self.name)
    
  def getprice(self):
    print("price= ",self.__price)
  def getquantity(self):
    print("quantity= ",self.__quantity,self.name)
  def sellproduct(self):
    amountsold=int(input("Enter amount sold: \n"))
    if (amountsold<=self.__quantity):
      stock=self.__quantity-amountsold
      self.__quantity=stock
      print("stock available: ",self.__quantity,self.name)
    else:
      print("insufficient stock")
class electronics(product):
  def __init__(self,name,price,quantity,warranty):
    self.warranty=warranty

    super() .__init__(name,price,quantity)
  def displaywarranty(self):
    print("warranty period= ",self.warranty)

p1=electronics("laptop",5000,6,"7 months")
p1.displayinfo()
p1.getquantity()
p1.getprice()
p1.displaywarranty()
p1.sellproduct()
p1.getquantity()


