class ProductOfNumbers:

    def __init__(self):
        self.products = [1]
        self.previous_zero_index = [0]


    def add(self, num: int) -> None:
        if num == 0:
            self.products.append(1)
            self.previous_zero_index.append(len(self.previous_zero_index))
        else:
            self.products.append(self.products[-1] * num)
            self.previous_zero_index.append(self.previous_zero_index[-1])

    def getProduct(self, k: int) -> int:
        index_from_right = len(self.products) - k
        if index_from_right <= self.previous_zero_index[-1]:
            return 0

        return self.products[-1] // self.products[index_from_right - 1]

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


productOfNumbers2 = ProductOfNumbers()
productOfNumbers2.add(3)