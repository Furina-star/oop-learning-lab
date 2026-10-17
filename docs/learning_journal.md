# Day 1: Introduction to Object-Oriented Programming

**Project:** OOP Learning Lab — League of Legends-Inspired Champion Arena  
**Language:** Python  
**Focus:** Classes, objects, attributes, methods, and return values

## 1. What I Learned

- A **class** is a blueprint. `Champion` describes what a champion has and can do.
- An **object** is one instance of a class, such as Ahri or Garen.
- **Attributes** store data, such as a champion's name and health.
- **Methods** are functions in a class, such as `take_damage()`.
- Each champion can have its own attribute values. Damaging Ahri does not change Garen's health.

## 2. Setting Up a Champion

`__init__()` sets the starting attributes when I create an object. `self` refers to that particular object.

```python
class Champion:
    def __init__(self, name, max_health=1000, health=1000, ability_power=200):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.ability_power = ability_power
```

In `self.name = name`, `name` is the value passed in, and `self.name` stores it on the object.

Parameters with defaults are optional:

```python
ahri = Champion("Ahri")
garen = Champion("Garen", ability_power=100)
```

Ahri starts with `200` ability power. Garen starts with `100`.

I also learned the difference between attribute types:

- **Class attributes** are defined directly in the class body and are available through the class.
- **Instance attributes**, such as `self.health`, store values on each object.

## 3. Taking Damage

This method goes inside the `Champion` class:

```python
def take_damage(self, amount):
    old_health = self.health

    self.health -= amount
    if self.health < 0:
        self.health = 0

    return old_health - self.health
```

It saves the old health, subtracts damage, keeps health at zero or above, and returns the actual health lost.

For example, if a champion has `500` HP and takes `800` damage, they lose only `500` HP and finish with `0`.

### Updating Health vs. Returning a Value

- `self.health -= amount` **changes** the object's stored health.
- `return self.health - amount` **returns a calculation** without changing stored health.
- A method can change an attribute without a `return` statement. In that case, it returns `None`.

## 4. Trying It Out

```python
ahri = Champion("Ahri")
garen = Champion("Garen")

ahri_damage = ahri.take_damage(1500)
garen_damage = garen.take_damage(600)

print(f"{ahri.name}: lost {ahri_damage} HP, {ahri.health} HP left")
print(f"{garen.name}: lost {garen_damage} HP, {garen.health} HP left")
```

Output:

```text
Ahri: lost 1000 HP, 0 HP left
Garen: lost 600 HP, 400 HP left
```

## 5. Mistakes and Lessons

- I first renamed one object instead of creating two. I needed separate objects for Ahri and Garen.
- I learned to use instance attributes for each champion's own data.
- I first returned a subtraction without saving the new health. Updating an attribute and returning a value are separate actions.
- I fixed negative health and changed the return value to report actual HP lost.

## 6. What Comes Next

The code currently assumes damage is nonnegative. Negative damage can increase health, and starting health is not checked against `max_health`.

Future topics include input validation, controlled access to health, healing, attacks, combat turns, and automated tests.

**Main takeaway:** An object's attributes store its state. A method can change that state and return a result.
