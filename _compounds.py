from abc import ABC, abstractmethod
from collections import defaultdict

# Design Pattern : Composite et Interpreter
class ChemicalComponent(ABC):
    """Classe abstraite pour les composants chimiques (éléments ou groupes)."""
    
    @abstractmethod
    def count_atoms(self):
        pass

class Element(ChemicalComponent):
    """Représente un élément chimique."""
    
    def __init__(self, symbol, count=1):
        self.symbol = symbol
        self.count = count
    
    def __str__(self):
        return f"{self.symbol}{self.count if self.count > 1 else ''}"

    def count_atoms(self):
        return {self.symbol: self.count}

class Compound(ChemicalComponent):
    """Représente un composé chimique (collection d'éléments ou de groupes)."""
    
    def __init__(self):
        self.components = []
    
    def __str__(self):
        return "".join(str(component) for component in self.components)

    def add_component(self, component):
        self.components.append(component)

    def count_atoms(self):
        atoms = defaultdict(int)
        for component in self.components:
            for element, count in component.count_atoms().items():
                atoms[element] += count
        return atoms

class Group(Compound):
    """Représente un groupe polyatomique (ex: (OH)3)."""
    
    def __init__(self, multiplier=1):
        super().__init__()
        self.multiplier = multiplier
        
    def __str__(self):
        base = super().__str__()
        return f"({base}){self.multiplier if self.multiplier > 1 else ''}"

    def count_atoms(self):
        atoms = super().count_atoms()
        for element in atoms:
            atoms[element] *= self.multiplier
        return atoms

# Design Pattern : Factory
class CompoundFactory:
    """Crée un composé chimique à partir d'une formule."""
    @staticmethod
    def create(formula):
        compound = Compound()
        stack = [compound]
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                # Créer un nouveau groupe et l'ajouter au composé parent
                group = Group()
                stack[-1].add_component(group)
                stack.append(group)
                i += 1
            elif formula[i] == ')':
                # Terminer le groupe et lire le multiplicateur
                group = stack.pop()
                i += 1
                multiplier = 1
                if i < len(formula) and formula[i].isdigit():
                    num_str = ''
                    while i < len(formula) and formula[i].isdigit():
                        num_str += formula[i]
                        i += 1
                    multiplier = int(num_str)
                group.multiplier = multiplier  # Correction clé ici
            elif formula[i].isupper():
                # Lire un élément chimique
                element_symbol = formula[i]
                i += 1
                if i < len(formula) and formula[i].islower():
                    element_symbol += formula[i]
                    i += 1
                # Lire le nombre d'atomes
                num_str = ''
                while i < len(formula) and formula[i].isdigit():
                    num_str += formula[i]
                    i += 1
                count = int(num_str) if num_str else 1
                stack[-1].add_component(Element(element_symbol, count))
            else:
                i += 1
        return compound