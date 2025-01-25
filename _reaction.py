from collections import defaultdict
import numpy as np

class ChemicalReaction:
    """Représente une réaction chimique avec des réactifs et produits."""
    def __init__(self):
        self.reactants = []  # Liste de tuples (coefficient, composé)
        self.products = []   # Liste de tuples (coefficient, composé)

    def add_reactant(self, coefficient, compound):
        self.reactants.append((coefficient, compound))

    def add_product(self, coefficient, compound):
        self.products.append((coefficient, compound))

    def balance(self):
        """Équilibre la réaction en utilisant l'algèbre linéaire."""
        all_compounds = self.reactants + self.products
        element_counts = defaultdict(lambda: [0] * len(all_compounds))

        # Compter les atomes pour chaque élément
        for idx, (_, compound) in enumerate(all_compounds):
            atoms = compound.count_atoms()
            for element, count in atoms.items():
                element_counts[element][idx] = count

        # Construire la matrice et le vecteur
        matrix = []
        b = []
        num_reactants = len(self.reactants)
        num_products = len(self.products)
        
        for element in element_counts:
            # Partie réactifs (positif) et produits (négatif sauf dernier)
            row = [
                *element_counts[element][:num_reactants], 
                *[-x for x in element_counts[element][num_reactants:-1]]
            ]
            matrix.append(row)
            b.append(element_counts[element][-1])  # Dernier produit

        # Résoudre le système linéaire
        A = np.array(matrix, dtype=np.float64)
        b = np.array(b, dtype=np.float64)
        coefficients = np.linalg.lstsq(A, b, rcond=None)[0]
        
        # Ajouter le coefficient 1 pour le dernier produit et normaliser
        coefficients = np.append(coefficients, 1.0)
        coefficients = self._normalize_coefficients(coefficients)

        # Mettre à jour les coefficients
        self._update_coefficients(coefficients, num_reactants, num_products)

    def _normalize_coefficients(self, coefficients):
        """Normalise les coefficients en entiers positifs."""
        # Trouver le plus petit coefficient non nul
        non_zero = coefficients[coefficients != 0]
        min_coeff = np.min(np.abs(non_zero)) if non_zero.size > 0 else 1
        
        # Convertir en entiers
        coefficients = np.round(coefficients / min_coeff).astype(int)
        
        # S'assurer que tous les coefficients sont positifs
        if np.any(coefficients < 0):
            coefficients *= -1
            
        return coefficients

    def _update_coefficients(self, coefficients, num_reactants, num_products):
        """Met à jour les coefficients dans la réaction."""
        # Séparer réactifs et produits
        reactant_coeffs = coefficients[:num_reactants]
        product_coeffs = coefficients[num_reactants:]
        
        # Mettre à jour les réactifs
        for i in range(num_reactants):
            self.reactants[i] = (reactant_coeffs[i], self.reactants[i][1])
            
        # Mettre à jour les produits
        for i in range(num_products):
            self.products[i] = (product_coeffs[i], self.products[i][1])

    def __str__(self):
        def format_side(side):
            return " + ".join(
                f"{int(coeff)}{comp}" if coeff != 1 else f"{comp}"
                for coeff, comp in side
                if coeff != 0
            )
        return f"{format_side(self.reactants)} -> {format_side(self.products)}"