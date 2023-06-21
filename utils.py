from datetime import timedelta
def add_years_to_date(original_date, years_to_add):
    try:
        return original_date.replace(year=original_date.year + years_to_add)
    except ValueError:
        # Handle leap year edge case
        return original_date + (timedelta(days=365) * years_to_add)
    
def subtract_years_from_date(original_date, years_to_subtract):
    try:
        return original_date.replace(year=original_date.year - years_to_subtract)
    except ValueError:
        # Handle leap year edge case
        return original_date - (timedelta(days=365) * years_to_subtract)
    