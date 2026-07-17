class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = self.name.center(30, '*')
        items = ""
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + "\n" + items + total


def create_spend_chart(categories):
    spent = []
    total = 0

    for category in categories:
        category_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += -item["amount"]
        spent.append(category_spent)
        total += category_spent

    percentages = [int((x / total) * 100) // 10 * 10 for x in spent]

    chart = "Percentage spent by category\n"

    for y in range(100, -1, -10):
        line = f"{y:>3}| "
        for pct in percentages:
            line += "o  " if pct >= y else "   "
        chart += line + "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        line = "     "
        for category in categories:
            line += (category.name[i] if i < len(category.name) else " ") + "  "
        chart += line + "\n"

    return chart.rstrip("\n")

def main():
    categories = [Category("Food"), Category("Transportation"), Category("Entertainment"), Category("Shopping")]
    categories[0].deposit(100, "Groceries")
    categories[1].deposit(50, "Public transport")
    categories[2].deposit(20, "Movies")
    categories[3].deposit(15, "Groceries")
    categories[3].withdraw(10, "Rent")
    categories[3].withdraw(5, "Utilities")
    categories[3].withdraw(15, "Groceries")
    categories[3].transfer(5, categories[0])
    categories[3].transfer(10, categories[1])
    categories[3].transfer(15, categories[2])
    print("\n".join(str(category) for category in categories))
    print(create_spend_chart(categories))

if __name__ == '__main__':
    main()