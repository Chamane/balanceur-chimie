import re

class Validator:
    """Valide la syntaxe d'une équation chimique."""
    
    def validate(self, equation):
        if '->' not in equation and '⇌' not in equation:
            raise ValueError("L'équation doit contenir '->' ou '⇌'.")
        # Valider les composés avec regex
        pattern = r'\(?[A-Z][a-z]?\d*\)?\d*'
        for part in equation.replace('->', '+').split('+'):
            if not re.fullmatch(f'({pattern})+', part.strip()):
                raise ValueError(f"Composé invalide : {part}")