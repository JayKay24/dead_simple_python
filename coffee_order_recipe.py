import functools


def auto_order(to_go):
    def decorator(cls):
        @functools.wraps(cls)
        def wrapper(*args, **kwargs):
            recipe = cls(*args, **kwargs)
            return (CoffeeOrder(recipe, to_go), recipe)
        return wrapper
    return decorator


class CoffeeOrder:
    def __init__(self, recipe, to_go=False):
        self.recipe = recipe
        self.to_go = to_go

    def brew(self):
        vessel = "in a paper cup" if self.to_go else "in a mug"
        print("Brewing", *self.recipe.parts, vessel)


class CoffeeRecipe:
    def __init__(self, parts):
        self.parts = parts


@auto_order(to_go=True)
class CoffeeShackRecipe(CoffeeRecipe):
    pass
