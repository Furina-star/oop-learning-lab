# Day 1: Introduction to Object-Oriented Programming

**Project:** OOP Learning Lab — League of Legends-Inspired Champion Arena  
**Language:** Python  
**Focus:** Classes, objects, instance attributes, constructors, instance methods, object state, and return values

## 1. Learning Objectives

By the end of Day 1, I aimed to:

- Understand the difference between a class and an object.
- Create multiple independent objects from one class.
- Initialize objects using `__init__()` and `self`.
- Understand default parameter values.
- Add an instance method that modifies an object's state.
- Distinguish between updating an attribute and returning a value.
- Prevent a champion's health from becoming negative after taking nonnegative damage.
- Calculate the actual health lost rather than merely reporting incoming damage.

## 2. Classes and Objects

### Class

A class is a blueprint for creating objects. It defines the attributes (data) and methods (behavior) that objects created from the class can use.

### Object

An object is an instance created from a class. Each object can maintain its own attribute values while using the structure and behavior defined by its class.

### Example

In this project, `Champion` is the class. It defines attributes such as `name`, `max_health`, `health`, and `ability_power`, along with a `take_damage()` method.

The variables `ahri` and `garen` refer to two different instances of `Champion`:

```python
ahri = Champion("Ahri")
garen = Champion("Garen")
```

Although both objects come from the same class, changing Ahri's instance attributes does not automatically change Garen's.

## 3. Class Attributes vs. Instance Attributes

In my first attempt, I wrote attributes directly inside the class body:

```python
class Champion:
    name = "Unknown"
    health = 1000
```

These are **class attributes**. They belong to the class and can be accessed through `Champion.name` or `Champion.health`. If an instance does not have its own attribute with the same name, Python can look up the value on the class.

I later learned to create separate objects and assign values to each object:

```python
ahri = Champion()
garen = Champion()

ahri.name = "Ahri"
garen.name = "Garen"
```

These assignments create **instance attributes** on the respective objects, allowing the champion names to be stored independently. Modifying `Champion.name` is different from modifying `ahri.name`.

## 4. Initializing Objects with `__init__()`

The `__init__()` method initializes a newly created instance. It makes it possible to provide a champion's information at the time the object is created rather than setting each attribute afterward.

This is the initializer from my Day 1 implementation:

```python
class Champion:
    def __init__(self, name, max_health=1000, health=1000, ability_power=200):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.ability_power = ability_power
```

- `self` refers to the particular instance being initialized.
- `name` is a parameter that receives an argument, such as `"Ahri"`.
- `self.name = name` stores that argument as an attribute of the instance.
- `max_health=1000`, `health=1000`, and `ability_power=200` are **default parameter values**. They are used when no replacement argument is provided.

For example:

```python
ahri = Champion("Ahri")
garen = Champion("Garen", ability_power=100)
```

Ahri receives the default ability power of `200`, while Garen receives `100`. Their attributes are separate because each object is initialized independently.

## 5. Instance Methods and Object State

An **instance method** describes behavior that an object can perform. The method receives `self`, allowing it to access and modify the specific object on which it was called.

For example:

```python
ahri.take_damage(200)
```

This operates on Ahri's health, not Garen's.

The initial damage logic helped me understand the difference between computing a result and updating an attribute:

```python
return self.health - amount
```

This calculates and returns a number but does **not** change `self.health`.

In contrast:

```python
self.health -= amount
```

This updates the object's attribute. It is equivalent, for numeric health values, to `self.health = self.health - amount`.

## 6. Updating State vs. Returning a Value

Modifying an object's state and returning a value are separate operations.

For a method that updates health but has no explicit `return`, Python returns `None`:

```python
def take_damage(self, amount):
    self.health -= amount
```

A method can also return a specific value:

- `return amount` returns the incoming damage argument.
- `return self.health` returns the remaining health.
- `return old_health - self.health` returns the actual health lost.

A return statement is not required merely to save changes to an instance attribute. The appropriate return value depends on the intended behavior of the method.

## 7. Preventing Negative Health

The original damage method could produce negative health if incoming damage exceeded the champion's remaining HP. I added a conditional check after subtraction:

```python
self.health -= amount
if self.health < 0:
    self.health = 0
```

For example, a champion with `1000` HP who receives `1500` damage should finish with `0` HP, not `-500`.

This protection works for **nonnegative incoming damage** under the current exercise assumptions. Input validation has not been implemented yet.

## 8. Calculating Actual Health Lost

Incoming damage and actual HP lost can differ. If a champion has `500` HP and receives `800` damage, the actual health lost is only `500`.

To calculate this, I saved the original health before changing it, then compared the old and new values:

```python
def take_damage(self, amount):
    old_health = self.health

    self.health -= amount
    if self.health < 0:
        self.health = 0

    return old_health - self.health
```

The method now updates the champion's health **and** returns the amount of health actually lost.

### Examples

| Starting HP | Incoming damage | Remaining HP | Actual HP lost (return value) |
| ---: | ---: | ---: | ---: |
| 1000 | 200 | 800 | 200 |
| 1000 | 1000 | 0 | 1000 |
| 1000 | 1500 | 0 | 1000 |
| 1000 | 0 | 1000 | 0 |
| 500 | 800 | 0 | 500 |

## 9. Day 1 Implementation and Output

In my final Day 1 script, I created Ahri and Garen as independent champion objects and applied damage to each:

```python
ahri = Champion("Ahri")
garen = Champion("Garen")

ahri_took_damage = ahri.take_damage(1500)
garen_took_damage = garen.take_damage(600)

print("Champion 1:", ahri.name)
print(f"Took {ahri_took_damage} damage")
print(f"Current Health: {ahri.health}\n")

print("Champion 2:", garen.name)
print(f"Took {garen_took_damage} damage")
print(f"Current Health: {garen.health}")
```

**Expected output from the final implementation:**

```text
Champion 1: Ahri
Took 1000 damage
Current Health: 0

Champion 2: Garen
Took 600 damage
Current Health: 400
```

This demonstrates that each champion stores its own health and that `take_damage()` returns the actual HP lost.

## 10. Challenges and Lessons Learned

- **One object vs. two objects:** I initially renamed the same object from Ahri to Garen. I corrected this by creating two independent instances.
- **Class vs. instance attributes:** I learned that assigning `Champion.name` changes a class attribute, while assigning `ahri.name` changes that instance's attribute.
- **Understanding `self`:** I learned that `self.name` belongs to an object, while `name` is a parameter passed to the initializer.
- **Calculation vs. assignment:** Simply subtracting a value in a return expression does not save the result to `self.health`. Augmented assignment (`-=`) changes the attribute.
- **Return values:** I initially confused the damage argument, updated health, and returned result. I learned that a method can update object state regardless of whether it returns a value.
- **Damage exceeding health:** I fixed negative remaining HP and later adjusted the return value to report the actual health lost.

## 11. Current Limitations and Future Improvements

These features were **not implemented in Day 1**:

- Validation against negative damage, which currently can increase health.
- Validation of initial statistics, including keeping initial health within `0` and `max_health`.
- Protection against arbitrary external modification of health (encapsulation with controlled access).
- Healing, attacks, abilities, and combat turns.
- Automated tests with `pytest`.

These are possible topics for later stages, not requirements completed today.

## 12. Day 1 Summary

Day 1 established the foundation for the Champion Arena project. I practiced creating classes and independent objects, initializing instance attributes, implementing methods, modifying object state, and controlling damage calculations. The most important lesson was understanding **the difference between an object's stored state and a method's return value**.

