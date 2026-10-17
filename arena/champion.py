class Champion:

    # The initializer function
    def __init__(self, name, max_health=1000, health=1000, ability_power=200):
        if health < 0 or max_health < 0:
            raise ValueError("Negative health is not allowed here.")

        if health > max_health:
            raise ValueError("Cannot exceed the maximum health")

        if max_health == 0:
            raise ValueError("Health or Max health cannot be zero")

        self.name = name
        self.max_health = max_health
        self._health = health
        self.ability_power = ability_power

    # Set function health as readable property attribute
    @property
    def health(self):
        return self._health

    # Take damage function where it calculates and check the damage dealt
    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Negative damage is not allowed here.")

        old_health = self._health
        self._health -= amount

        if self._health < 0:
            self._health = 0

        return old_health - self._health

ahri = Champion("Ahri")
garen = Champion("Garen")

ahri_took_damage = ahri.take_damage(1500)
assert ahri.health == 0

garen_took_damage = garen.take_damage(300)
assert garen.health == 700

print("Champion 1:", ahri.name)
print(f"Took {ahri_took_damage} damage")
print(f"Current Health: {ahri.health}\n")

print("Champion 2:", garen.name)
print(f"Took {garen_took_damage} damage")
print(f"Current Health: {garen.health}")

