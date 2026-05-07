
price = 0
discount = 0

def apply_discount(price, discount):
    if isinstance(price, (int, float)) == False:
        return 'The price should be a number'
    elif isinstance(discount, (int, float)) == False:
        return 'The discount should be a number'
    elif price <= 0:
        return 'The price should be greater than 0'
    elif discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    else:
        pass
    apply_discount = price - (price * (discount/100)) 
    return apply_discount

print(apply_discount(100, 0))
