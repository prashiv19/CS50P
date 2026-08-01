def hello(to="World"):
    print("Hello,", to.strip().title())


hello()
name = input("Whats your name? ")
hello(name)