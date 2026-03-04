def calculate_cagr(start_value, end_value, years):

    cagr = (end_value / start_value) ** (1 / years) - 1
    percentage = cagr * 100

    return {
        "start_value": start_value,
        "end_value": end_value,
        "years": years,
        "cagr": cagr,
        "percentage": round(percentage, 2),
        "formula": f"({end_value}/{start_value})^(1/{years}) - 1"
    }


if __name__ == "__main__":

    result = calculate_cagr(
        start_value=7351,
        end_value=17000,
        years=9
    )

    print(result)