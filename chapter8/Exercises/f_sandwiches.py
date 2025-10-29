def sandwich(*ingredients):
    """Prints a summary of a sandwich"""
    
    print("\nThis sandwich contains:")
    for ingredient in ingredients:
       print(ingredient.title())

sandwich("cheese", "polony", "lettuce", "butter")
sandwich("cheese")
sandwich("polony", "lettuce")


