# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name, greeting="Hello, <name>!"):
    greeting = greeting.replace("<name>", name)
    return greeting
    # Kan ook in een regel, maar dat vind ik minder overzichtelijk:
    # return greeting.replace("<name>", name)


print(greet("Nicolette"))
print(greet("Bob"))


def force(mass, body="earth"):
    dictionary_hemellichamen = {
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "earth": 9.798,
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58,
    }

    g = round(dictionary_hemellichamen[body], 1)
    # mass = argument
    F = mass * g
    return F


print(force(10))
print(force(5.972e24, "earth"))
print(force(5.972e24))
print(force(1.989e30, "sun"))
print(force(7.35e22, "moon"))
print(force(1.302e22, "pluto"))


def pull(m1, m2, d):
    G = 6.674e-11
    F = G * ((m1 * m2) / (d**2))
    return F


print(pull(800, 1500, 3))
print(pull(0.1, 5.972e24, 6.371e6))
