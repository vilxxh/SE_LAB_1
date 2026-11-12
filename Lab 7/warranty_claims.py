
def parse_claim(text):
  
    if not isinstance(text, str):
        raise ValueError("Claim must be text")

    
    if text.count(":") != 1:
        raise ValueError("Invalid claim format")

   
    plan, months = text.split(":")

    
    plan = plan.strip()
    months = months.strip()

    
    if not plan or not months:
        raise ValueError("Plan and months cannot be empty")

    
    try:
        months = float(months)
    except ValueError:
        raise ValueError("Months must be numeric")

    
    if months < 0 or not __import__("math").isfinite(months):
        raise ValueError("Months must be a valid non-negative number")

    
    return plan.title(), months


def age_average(ages_csv):
    
    if not isinstance(ages_csv, str):
        raise ValueError("Ages must be provided as text")

    
    parts = ages_csv.split(",")

    
    if not parts or any(not part.strip() for part in parts):
        raise ValueError("Ages cannot be empty")

    
    try:
        values = [int(part.strip()) for part in parts]
    except ValueError:
        raise ValueError("All ages must be integers")

    
    if any(age < 0 for age in values):
        raise ValueError("Ages cannot be negative")

    
    return sum(values) // len(values)


def payable_charge(text):
    
    if not isinstance(text, str):
        raise ValueError("Charge must be text")

    
    if text.count("|") != 1:
        raise ValueError("Invalid charge format")

 
    charge, discount = text.split("|")

   
    charge = charge.strip()
    discount = discount.strip()


    if not charge or not discount:
        raise ValueError("Charge and discount cannot be empty")

    
    try:
        charge = float(charge)
        discount = float(discount)
    except ValueError:
        raise ValueError("Charge and discount must be numeric")

  
    import math
    if not math.isfinite(charge) or not math.isfinite(discount):
        raise ValueError("Values must be finite numbers")

    if charge < 0 or discount < 0:
        raise ValueError("Values cannot be negative")

   
    total = charge * 1.18 - discount

 
    return max(total, 0)


def main():
    print("==== Running parse_claim ====")
    user_input = input("Enter plan:age in months (e.g. standard:30): ")
    result = parse_claim(user_input)
    print("Plan and Age:", result)

    print("\n==== Running age_average ====")
    user_input = input("Enter product ages as CSV (e.g. 12,24,36): ")
    result = age_average(user_input)
    print("Average Age:", result)

    print("\n==== Running payable_charge ====")
    user_input = input("Enter charge|discount (e.g. 1500|200): ")
    result = payable_charge(user_input)
    print("Payable Charge:", result)


if __name__ == "__main__":
    main()
