
# Import datasets from other files
from current_affairs import current_affairs, ai_growth, economy, students, topics
from market_analysis import companies, gold_price, oil_prices
from sports_analysis import players, analyze_cricket
from weather_analysis import city_temperature

# Import statistical functions
from statistics_analysis import (
    calculate_average,
    find_maximum,
    find_minimum,
    sort_data,
    calculate_statistics
)


# Function to analyze different datasets
def analyze_dataset(name, data):
    print("\n---", name, "---")

    if type(data) == dict:
        values = list(data.values())
    else:
        values = data

    print("Data:", data)

    if len(values) > 0:
        print("Average:", calculate_average(values))
        print("Maximum:", find_maximum(values))
        print("Minimum:", find_minimum(values))
        print("Sorted (highest first):", sort_data(values))

        print("\nStatistical Summary:")
        calculate_statistics(values)


# Main function
def main():
    print("=" * 45)
    print("DATA SCIENCE AND CURRENT AFFAIRS ANALYZER")
    print("=" * 45)

    # Current Affairs and related datasets
    analyze_dataset("Current Affairs", current_affairs)
    analyze_dataset("AI Growth", ai_growth)
    analyze_dataset("Economy", economy)
    analyze_dataset("Education", students)
    analyze_dataset("Technology Trends", topics)

    # Market datasets
    analyze_dataset("Stock Market", companies)
    analyze_dataset("Gold Prices", gold_price)
    analyze_dataset("Oil Prices", oil_prices)

    # Weather dataset
    analyze_dataset("Weather", city_temperature)

    # Cricket dataset
    analyze_dataset("Cricket", players)
    analyze_cricket()

    print("\nAnalysis completed successfully!")


# Program execution starts here
if __name__ == "__main__":
    main()

    
