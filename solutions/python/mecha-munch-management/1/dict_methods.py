"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    return add_item({}, notes)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    updated_ideas = ideas.copy()
    
    # Iterate through updates
    for recipe_name, ingredients in recipe_updates:
        # Overwrite or add new recipe
        updated_ideas[recipe_name] = ingredients
    
    return updated_ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    new_mapping = {}
    for key in cart:
        new_mapping[key] = [cart[key], aisle_mapping[key][0], aisle_mapping[key][1]]
        
    return dict(sorted(new_mapping.items(), key=lambda x: x[0], reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    updated_inventory = store_inventory.copy()

    for key, (ordered_qty, _, _) in fulfillment_cart.items():
        current_qty, aisle, refrigeration = updated_inventory[key]

        # Decrease stock
        new_qty = current_qty - ordered_qty
        if new_qty > 0:
            updated_inventory[key] = [new_qty, aisle, refrigeration]
        else:
            updated_inventory[key] = ['Out of Stock', aisle, refrigeration]

    return updated_inventory
