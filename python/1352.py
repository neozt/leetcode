class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]

    def size(self):
        # Return how many non-zero numbers encountered since the last 0
        return len(self.prefix_products) - 1

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > self.size():
            # Includes a 0 in the product
            return 0

        return self.prefix_products[-1] // self.prefix_products[self.size() - k]

productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)        # [3]
productOfNumbers.add(0)        # [3,0]
productOfNumbers.add(2)        # [3,0,2]
productOfNumbers.add(5)        # [3,0,2,5]
productOfNumbers.add(4)        # [3,0,2,5,4]
print(productOfNumbers.getProduct(2)) # return 20. The product of the last 2 numbers is 5 * 4 = 20
print(productOfNumbers.getProduct(3)) # return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
print(productOfNumbers.getProduct(4)) # return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8)        # [3,0,2,5,4,8]
print(productOfNumbers.getProduct(2)) # return 32. The product of the last 2 numbers is 4 * 8 = 32