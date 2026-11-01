"""
Week 07 - Helper Functions Module
ISM 2411 - Introduction to Python for Business
"""

def calculate_total(price, quantity, tax_rate=0.07):
    """Calculate total cost including tax."""
    subtotal = price * quantity
    total = subtotal * (1 + tax_rate)
    return round(total, 2)

def calculate_discount(amount, discount_percent):
    """Calculate discounted amount."""
    discount = amount * (discount_percent / 100)
    return round(amount - discount, 2)

def format_currency(amount):
    """Format float as currency string."""
    return f"${amount:,.2f}"

def is_eligible_for_promo(purchase_amount, is_member=False):
    """Check if purchase is eligible for promotional discount."""
    if is_member or purchase_amount >= 100:
        return True
    return False

if __name__ == "__main__":
    print("Testing Helper Functions:")
    total = calculate_total(25.0, 4)
    print("Total:", format_currency(total))
    discounted = calculate_discount(total, 10)
    print("Discounted (10%):", format_currency(discounted))
