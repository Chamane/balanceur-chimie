import re
from _validator import Validator
from _compounds import CompoundFactory
from _reaction import ChemicalReaction

# Design Pattern : Facade (pour simplifier l'interface)
class ReactionBalancer:
    def __init__(self):
        self.validator = Validator()
        self.factory = CompoundFactory()

    def parse_side(self, side_str):
        """Parse une partie de l'équation (réactifs ou produits)."""
        compounds = []
        for part in re.split(r'\s*\+\s*', side_str.strip()):
            if not part:
                continue
            # Extraire le coefficient et le composé
            coeff_match = re.match(r'^(\d*\.?\d*)(.*)', part)
            coeff_str, compound_str = coeff_match.groups()
            coeff = float(coeff_str) if coeff_str else 1.0
            # Valider et créer le composé
            if not compound_str:
                raise ValueError(f"Composé manquant dans '{part}'.")
            compound = self.factory.create(compound_str)
            compounds.append((coeff, compound))
        return compounds

    def balance(self, equation):
        try:
            self.validator.validate(equation)
            reaction = ChemicalReaction()
            
            # Découpage de l'équation
            parts = re.split(r'\s*(->|⇌)\s*', equation)
            if len(parts) != 3:
                raise ValueError("Format d'équation invalide. Utilisez '->' ou '⇌'.")
            
            reactants_str, _, products_str = parts
            
            # Parsing des réactifs
            for coeff, compound in self.parse_side(reactants_str):
                reaction.add_reactant(coeff, compound)
            
            # Parsing des produits
            for coeff, compound in self.parse_side(products_str):
                reaction.add_product(coeff, compound)
            
            # Équilibrer et retourner
            reaction.balance()
            return str(reaction)
            
        except Exception as e:
            raise ValueError(f"Erreur lors du traitement : {str(e)}")