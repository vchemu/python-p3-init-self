#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

    def showing_self(self):
        return self
    
fido = Dog("Fido")
fido.showing_self()
fido is fido.showing_self()