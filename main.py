from _balancer import ReactionBalancer 

if __name__ == "__main__":
    balancer = ReactionBalancer()
    equation = input("Entrez une équation chimique (ex: H2 + O2 -> H2O) : ")
    try:
        balanced_equation = balancer.balance(equation)
        print("Équation équilibrée :", balanced_equation)
    except ValueError as e:
        print("Erreur :", e)