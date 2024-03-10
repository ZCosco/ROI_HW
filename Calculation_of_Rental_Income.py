class RentalProperty:
    def __init__(self, rental_income, expenses):
        # Initialize RentalProperty object with rental income and expenses
        self.rental_income = rental_income
        self.expenses = expenses
    
    def calculate_cash_flow(self):
        # Calculate monthly cash flow by subtracting expenses from rental income
        return self.rental_income - self.expenses
    
    def calculate_roi(self, down_payment, closing_costs, refurbish_budget):
        # Calculate Return on Investment (ROI)
        total_investment = down_payment + closing_costs + refurbish_budget
        annual_cash_flow = self.calculate_cash_flow() * 12
        roi = (annual_cash_flow / total_investment) * 100
        return roi

def Rental_Tycoon_Data():
    # Function to get input data for rental property
    rental_income = float(input("Enter the monthly rental income: "))
    expenses = float(input("Enter the monthly expenses (including mortgage): "))
    down_payment = float(input("Enter the down payment: "))
    closing_costs = float(input("Enter the closing costs: "))
    refurbish_budget = float(input("Enter the refurbish budget: "))
    
    return RentalProperty(rental_income, expenses), down_payment, closing_costs, refurbish_budget

# Main function
def main():
    while True:
        # Get rental property details from user input
        property_details, down_payment, closing_costs, refurbish_budget = Rental_Tycoon_Data()
        print("\nCalculating ROI for the rental property...")
        print("ROI:", property_details.calculate_roi(down_payment, closing_costs, refurbish_budget), "%")
        if property_details.calculate_roi(down_payment, closing_costs, refurbish_budget) > 0:
            print('Evil Landlord')
        else:
            print('Hard TImes')
            
            # Ask user if they want to calculate ROI for another property
        choice = input("Do you want to calculate ROI for another property? (y/n): ")
        if choice.lower() != 'y':
            print("Program terminated.")
            break

if __name__ == "__main__":
    main()
