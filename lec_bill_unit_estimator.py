
def get_positive_number(prompt):
    """Ask for a number greater than zero."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_non_negative_number(prompt):
    """Ask for zero or a positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter zero or a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def currency_converter(amount, currency, exchange_rate):
    """Convert USD to LRD."""
    if currency == "USD":
        return amount * exchange_rate
    return amount


def unit_calculator(amount_lrd, service_fee, tariff_rate):
    """Calculate electricity units purchased."""
    net_amount = amount_lrd - service_fee

    if net_amount <= 0:
        raise ValueError(
            "The amount after the service fee must be greater than zero."
        )

    units = net_amount / tariff_rate
    return net_amount, units


def appliance_estimator(name, power_watts, hours_per_day, quantity):
    """Calculate daily electricity consumption."""
    daily_kwh = (power_watts / 1000) * hours_per_day
    return daily_kwh * quantity


def duration_calculator(units_purchased, daily_consumption):
    """Estimate how many days electricity units will last."""
    if daily_consumption <= 0:
        return None

    return units_purchased / daily_consumption


def receipt_generator(currency, original_amount, amount_lrd,
                      service_fee, net_amount, tariff_rate,
                      units, daily_consumption, days):

    print("\n" + "=" * 54)
    print("             LEC BILL & UNIT ESTIMATOR")
    print("=" * 54)

    print(f"Amount paid:                 {original_amount:,.2f} {currency}")
    print(f"Purchase value in LRD:       {amount_lrd:,.2f} LRD")
    print(f"Service fee:                 {service_fee:,.2f} LRD")
    print(f"Net purchase amount:         {net_amount:,.2f} LRD")
    print(f"Tariff rate:                 {tariff_rate:,.2f} LRD/kWh")
    print(f"Electricity units received:  {units:,.2f} kWh")

    print("-" * 54)

    print(f"Estimated daily usage:       {daily_consumption:,.2f} kWh/day")

    if days is None:
        print("Estimated duration:          Not available")
    else:
        print(f"Estimated duration:          {days:,.2f} days")

    print("=" * 54)
    print("Note: This is an estimate. Actual usage may differ.")
    print("=" * 54)


def main():

    print("=" * 54)
    print("             LEC BILL & UNIT ESTIMATOR")
    print("=" * 54)

    # Collect purchase information
    budget = get_positive_number("Enter your budget amount: ")

    while True:
        currency = input("Currency (USD or LRD): ").strip().upper()

        if currency in ("USD", "LRD"):
            break

        print("Please enter USD or LRD.")

    exchange_rate = get_positive_number(
        "Enter USD to LRD exchange rate: "
    )

    tariff_rate = get_positive_number(
        "Enter tariff rate (LRD per kWh): "
    )

    service_fee = get_non_negative_number(
        "Enter service fee (LRD): "
    )

    # Convert currency
    amount_lrd = currency_converter(
        budget, currency, exchange_rate
    )

    # Calculate electricity units
    try:
        net_amount, units = unit_calculator(
            amount_lrd, service_fee, tariff_rate
        )
    except ValueError as error:
        print(error)
        return

    # Collect appliance information
    number_of_appliances = int(
        get_positive_number(
            "How many appliance types do you want to enter? "
        )
    )

    daily_consumption = 0

    for i in range(number_of_appliances):

        print(f"\nAppliance {i + 1}")

        name = input("Enter appliance name: ")

        power = get_positive_number(
            "Power in watts: "
        )

        hours = get_non_negative_number(
            "Hours used per day: "
        )

        quantity = int(
            get_positive_number("Quantity: ")
        )

        daily_consumption += appliance_estimator(
            name, power, hours, quantity
        )

    # Estimate electricity duration
    days = duration_calculator(
        units, daily_consumption
    )

    # Display final receipt
    receipt_generator(
        currency,
        budget,
        amount_lrd,
        service_fee,
        net_amount,
        tariff_rate,
        units,
        daily_consumption,
        days
    )


# Run the program
if __name__ == "__main__":
    main()
