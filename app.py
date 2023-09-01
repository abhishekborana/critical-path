class PricingRule:
    def __init__(self, productSku, discountQuantity, discountPrice):
        self.productSku = productSku
        self.discountQuantity = discountQuantity
        self.discountPrice = discountPrice
    
            

class Product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

class Checkout:
    def __init__(self, pricingRules):
        self.cart = list()
        self.pricingRules = pricingRules

    def scan(self, productSku):
        try:
            
            product = self.findProductThroughSku(productSku)
            if product:
                self.cart.append(product)
        except Exception as error:
            return error

    def total(self):
        try:
            totalPrice = 0

            totalProducts=dict()
            rulesOnSkus=dict()
            
            for rule in self.pricingRules:
                rulesOnSkus[rule.productSku]=[rule.discountQuantity,rule.discountPrice]
                
            for product in self.cart:
                if product.sku in totalProducts:
                    totalProducts[product.sku]+=1
                else:
                    totalProducts[product.sku]=1
            
            for product in self.cart:
                if(totalProducts[product.sku]!=0):
                    if product.sku in rulesOnSkus:
                        productCount = totalProducts[product.sku]
                        if productCount>=rulesOnSkus[product.sku][0]:
                            totalPrice+=rulesOnSkus[product.sku][1]*rulesOnSkus[product.sku][0]
                            totalProducts[product.sku]-=rulesOnSkus[product.sku][0]
                        else:
                            totalPrice+=product.price
                            totalProducts[product.sku]-=1
                    else:
                        totalPrice+=product.price
                        totalProducts[product.sku]-=1
                        
            return totalPrice
        except Exception as error:
            print(error)
            return 0

    def findProductThroughSku(self, productSku):
        try:
            for product in products:
                if product.sku == productSku:
                    return product
            return None
        except Exception as error:
            return None
            

products = [
    Product("op10", "Oneplus 10", 849.99),
    Product("op11", "Oneplus 11", 949.99),
    Product("buds", "Earbuds", 129.99),
    Product("wtch", "Smart Watch", 229.99)
]

pricingRules = [
    PricingRule("buds", 3, 86.66),  # 3 for 2 deal on Earbuds
    PricingRule("op11", 5, 899.99)  # Bulk discount on Oneplus 11
]

co = Checkout(pricingRules)
co.scan("op11")
co.scan("op11")
co.scan("op11")
co.scan("op11")
co.scan("op11")

print("Total: ${:.2f}".format(co.total()))
