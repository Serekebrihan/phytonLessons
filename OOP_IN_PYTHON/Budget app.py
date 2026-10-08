class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    def check_funds(self, amount):
        return amount <= self.get_balance()
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def transfer(self, amount, category_instance):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

    def __str__(self):
        output = f"{self.name:*^30}\n"
        for item in self.ledger:
            # Slice description to max 23 chars, left-aligned to 23 spaces
            desc = f"{item['description'][:23]:<23}"
            # Format amount to 2 decimal places, right-aligned to 7 spaces
            amt = f"{item['amount']:>7.2f}"

            output += f"{desc}{amt}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output


def create_spend_chart(categories):
    spent_by_category = []
    for category in categories:
        spent = sum(abs(item['amount']) for item in category.ledger if item['amount'] < 0)
        spent_by_category.append(spent)

    total_spent = sum(spent_by_category)

    percentages = []
    for spent in spent_by_category:
        if total_spent > 0:
            percentages.append(int((spent / total_spent) * 100 // 10) * 10)
        else:
            percentages.append(0)

    res = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "| "
        for p in percentages:
            if p >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    res += "    " + "-" * (3 * len(categories) + 1) + "\n"
    max_len = max(len(category.name) for category in categories)
    padded_names = [category.name.ljust(max_len) for category in categories]

    for i in range(max_len):
        res += "     "
        for name in padded_names:
            res += name[i] + "  "
        if i < max_len - 1:
            res += "\n"

    return res


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)