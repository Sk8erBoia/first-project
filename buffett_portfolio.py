import math

# Sample holdings from Warren Buffett's Berkshire Hathaway portfolio (approximate values)
holdings = {
    'AAPL': {
        'shares': 907_559_761,
        'price': 150.0  # example price
    },
    'BAC': {
        'shares': 1_010_100_606,
        'price': 29.0
    },
    'KO': {
        'shares': 400_000_000,
        'price': 55.0
    },
    'AXP': {
        'shares': 151_610_700,
        'price': 180.0
    },
    'KHC': {
        'shares': 325_634_818,
        'price': 35.0
    }
}

def total_value(holdings):
    return sum(info['shares'] * info['price'] for info in holdings.values())

def holding_values(holdings):
    return {symbol: info['shares'] * info['price'] for symbol, info in holdings.items()}

def holding_weights(holdings):
    total = total_value(holdings)
    return {symbol: (info['shares'] * info['price']) / total for symbol, info in holdings.items()}

# Example of intrinsic value using Graham formula (simplified)
# intrinsic value = EPS * (8.5 + 2*g) * 4.4 / AAA_bond_yield

def graham_intrinsic_value(eps, growth_rate, aaa_yield):
    return eps * (8.5 + 2 * growth_rate) * 4.4 / aaa_yield

if __name__ == "__main__":
    print("Holding values:")
    values = holding_values(holdings)
    for symbol, value in values.items():
        print(f"{symbol}: ${value:,.2f}")

    print("\nHolding weights:")
    weights = holding_weights(holdings)
    for symbol, weight in weights.items():
        print(f"{symbol}: {weight:.2%}")

    total = total_value(holdings)
    print(f"\nTotal portfolio value: ${total:,.2f}")

    # Example intrinsic value calculation
    eps = 5.0  # Example earnings per share
    growth = 4.0  # Example growth rate
    aaa_yield = 3.5  # Example AAA bond yield in percent
    intrinsic = graham_intrinsic_value(eps, growth, aaa_yield)
    print(f"\nGraham intrinsic value: ${intrinsic:,.2f}")
