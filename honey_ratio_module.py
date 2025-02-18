def calculate_honey_water_ratio(batch_size, sweetness):
    """
    Calculate the required amount of honey and water based on batch size and sweetness level.
    
    Parameters:
    batch_size (float): The desired batch size in liters.
    sweetness (str): The desired sweetness level.
    
    Returns:
    tuple: A tuple containing (honey_amount, water_amount) in liters.
    """
    # Define honey-to-water ratios based on sweetness level
    ratios = {
        "dry": 0.15,       # 15% honey, 85% water
        "semi-sweet": 0.25, # 25% honey, 75% water
        "sweet": 0.35       # 35% honey, 65% water
    }
    
    honey_ratio = ratios.get(sweetness, 0.25)  # Default to semi-sweet if invalid sweetness
    honey_amount = batch_size * honey_ratio
    water_amount = batch_size - honey_amount
    
    return honey_amount, water_amount
