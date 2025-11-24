"""Study case for Class Method in Python."""


class Shopping:
    """Class to manage shopping items and calculate total price."""
    
    def __init__(self, items):
        """
        Initialize Shopping instance.
        
        Args:
            items (list): List of dictionaries containing item name and price.
        """
        self.items = items
        self.total_price = self.calculate_total_price()
    
    def calculate_total_price(self):
        """Calculate total price of all items."""
        return sum(item["price"] for item in self.items)
    
    def get_item_names(self):
        """Get list of item names."""
        return [item["item"] for item in self.items]
    
    def display_items(self):
        """Display items and total price in formatted string."""
        return (
            f"Items: {', '.join(self.get_item_names())}\n"
            f"Total Price: Rp {self.total_price:,}"
        )
    
    @classmethod
    def display_data(cls, items):
        """
        Class method to create instance and display data.
        
        Args:
            items (list): List of dictionaries containing item name and price.
            
        Returns:
            str: Formatted string of items and total price.
        """
        instance = cls(items)
        return instance.display_items()


def main():
    """Main function to run tests."""
    datas = [
        {"item": "Rice", "price": 20000},
        {"item": "Eggs", "price": 15000},
        {"item": "Milk", "price": 10000},
        {"item": "Bread", "price": 12000},
    ]
    
    # Test 1: Object creation
    print("=== Test Object Creation ===")
    test_obj = Shopping(datas)
    print(f"Object created: {test_obj}")
    print(f"Items: {test_obj.get_item_names()}")
    print(f"Total: Rp {test_obj.total_price:,}\n")
    
    # Test 2: Class method
    print("=== Test Class Method ===")
    result = Shopping.display_data(datas)
    print(result)


if __name__ == "__main__":
    main()