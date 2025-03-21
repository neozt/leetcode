from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe_ingredients = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        recipe_feasibility = {}
        supplies_set = set(supplies)

        def is_feasible(recipe: str) -> bool:
            if recipe in supplies_set:
                return True

            if recipe in recipe_feasibility:
                return recipe_feasibility[recipe]

            if recipe not in recipe_ingredients:
                return False

            recipe_feasibility[recipe] = False # Temp set False to prevent circular dependency
            feasible = True
            for ingredient in recipe_ingredients[recipe]:
                if not is_feasible(ingredient):
                    feasible = False
                    break

            recipe_feasibility[recipe] = feasible
            return feasible

        result = []
        for recipe in recipes:
            if is_feasible(recipe):
                result.append(recipe)

        return result

print(Solution().findAllRecipes(["bread"], [["yeast","flour"]], ["yeast","flour","corn"]))
print(Solution().findAllRecipes(["bread","sandwich"], [["yeast","flour"],["bread","meat"]], ["yeast","flour","meat"]))
print(Solution().findAllRecipes(["bread","sandwich","burger"], [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], ["yeast","flour","meat"]))
