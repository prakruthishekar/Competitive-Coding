def parse_str_rates(str_rates):
    rows = str_rates.split(';')
    
    matrix = {}
    lock_periods = set()
    
    for row in rows:
        if ':L' not in row:
            continue
        
        rates_prices, lock = row.split(':L')
        lock_periods.add(lock)
        
        rates_prices = rates_prices.split(',')
        for i in range(0, len(rates_prices), 2):
            rate = rates_prices[i].strip('"')
            price = rates_prices[i+1].strip('"')
            
            if rate not in matrix:
                matrix[rate] = {}
            matrix[rate][lock] = price
    
    return matrix, sorted(lock_periods)


def generate_html(matrix, lock_periods):
    html_content = "<table border='1'>"
    
    # Add header
    html_content += "<tr><th></th>"
    for lock_period in lock_periods:
        html_content += f"<th>{lock_period}</th>"
    html_content += "</tr>"
    
    for rate in sorted(matrix.keys(), key=float): # Sorting rates
        html_content += f"<tr><td>{rate}</td>"
        for lock_period in lock_periods:
            html_content += f"<td>{matrix[rate].get(lock_period, '')}</td>"
        html_content += "</tr>"
    
    html_content += "</table>"
    return html_content

# Get input from the user
str_rates = input("Enter the rate string: ")

matrix, lock_periods = parse_str_rates(str_rates)
html_content = generate_html(matrix, lock_periods)

with open("output.html", "w") as f:
    f.write(html_content)

print("HTML content has been written to 'output.html'.")
