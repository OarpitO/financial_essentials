"""
Script to calculate CAGR of an investment over years
Example usage:
python calculate_mf_cagr.py

Example Input:
Enter the initial invested amount for MF: 50000     <- Should be int
Enter the latest value for MF: 77850     <- Should be int
Enter no. of years: 5.75     <- Can take int and float both.


Example Output:
Compound Annual Growth Rate (CAGR): 9.26%
"""

def calculate_cagr(absolute_rate_of_return, num_of_years):
    cagr = ((1 + absolute_rate_of_return) ** (1 / num_of_years)) - 1
    return cagr


def calculate_absolute_return(initial, final):
    return (final - initial) / initial


initial = int(input("Enter the initial invested amount for MF: "))
final = int(input("Enter the latest value for MF: "))
years = float(input("Enter no. of years: "))

result = calculate_cagr(calculate_absolute_return(initial, final), years)
print("Compound Annual Growth Rate (CAGR): {:.2%}".format(result))
