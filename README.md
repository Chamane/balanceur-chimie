# 🧪🔬 Balanceur d'Équations Chimiques : La Magie de la Stoechiométrie en Python 🐍✨

**Par Madsen Servius**  
*Un projet qui donne vie à la chimie avec du code, des algorithmes et un peu de magie numérique !*

---

## 🌟 **Pourquoi ce Projet est Génial ?**

Imaginez un monde où équilibrer des équations chimiques complexes devient aussi simple qu'un clic. Ce projet rend cela possible !  
🔥 **Défis relevés** : Analyse lexicale, parsing AST, gestion des groupes polyatomiques, et équilibrage stoechiométrique.  
🚀 **Pour les chimistes, les étudiants et les curieux** : Comprendre la chimie n'a jamais été aussi interactif !

---

## 🛠 **Fonctionnalités**

- ✅ **Équilibrage automatique** d'équations simples à complexes.
- 🎯 **Gestion des groupes polyatomiques** : `(SO4)`, `(NO3)`, `(PO4)`, etc.
- 🧮 **Calculs précis** avec `numpy` pour des coefficients entiers.
- 🚨 **Validation robuste** : Détecte les entrées invalides.
- 🎨 **Sortie claire** : Affiche les équations équilibrées en beauté.

---

## 💻 **Technologies Utilisées**

- 🐍 **Python 3** : Le cœur du projet.
- 📦 **NumPy** : Pour résoudre les systèmes d'équations linéaires.
- 🧩 **Design Patterns** : Composite, Factory, Interpreter.
- 🧪 **Simulation Chimique** : Algorithmes de comptage d'atomes.

---

## 🚀 **Installation**

Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-username/balanceur-chimie.git
   cd balanceur-chimie
   ```

## 🧪 **Exemples d'Utilisation**

### 1. **Réaction Simple**  
**Entrée** :
```python
>>> Entrez une équation : H2 + O2 -> H2O
⚡ Équation équilibrée : 2H2 + O2 → 2H2O
```

### 2. **Combustion du Propane**
**Entrée** :
```python
>>> Entrez une équation : C3H8 + O2 -> CO2 + H2O
🔥 Équation équilibrée : C3H8 + 5O2 → 3CO2 + 4H2O
```
### 3. **Réaction avec Groupe Polyatomique**
**Entrée**
```python
>>> Entrez une équation : Al2(SO4)3 + Ca(OH)2 -> Al(OH)3 + CaSO4
🌈 Équation équilibrée : Al2(SO4)3 + 3Ca(OH)2 → 2Al(OH)3 + 3CaSO4
```

---

## 🧬 **Comment ça Marche ?**

1. **Lexer** : Découpe l'équation en tokens (`H2`, `+`, `O2`, `->`, etc.).  
2. **Parser** : Construit un AST (Arbre Syntaxique Abstrait) pour représenter la réaction.  
3. **Comptage d'Atomes** : Utilise le pattern *Composite* pour calculer les atomes dans chaque composé.  
4. **Équilibrage** : Résout un système linéaire avec `numpy` pour trouver les coefficients.  

---

## 🎯 **Défis Relevés**

- **Parsing des Formules Complexes** : `Fe3(PO4)2`, `(NH4)2SO4`, etc.  
- **Gestion des Coefficients Négatifs** : Normalisation pour éviter les `-1H2`.  
- **Validation des Charges** : *En cours pour les ions !*  

---

## 🚧 **Améliorations Futures**

- 🧪 **Gestion des Ions** : `Fe^3+`, `SO4^2-`.  
- 📊 **Interface Graphique** : Avec `tkinter` ou `streamlit`.  
- 🌐 **API Web** : Pour une utilisation en ligne.  

---

## 🙌 **Contribution**

Les contributions sont les bienvenues !  
1. **Forkez** le projet.  
2. Créez une branche : `git checkout -b feature/nouvelle-fonctionnalite`.  
3. Commitez : `git commit -m "Ajout d'une fonctionnalité géniale"`.  
4. Pushez : `git push origin feature/nouvelle-fonctionnalite`.  
5. Ouvrez une **Pull Request** !

---

## 📜 **Licence**

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 💬 **Remerciements**

- À **Mendeleïev** pour le tableau périodique.  
- À la communauté **Python** pour des outils incroyables.  
- À **Vous** pour avoir lu ce README ! 😊

---

**Prêt à explorer la chimie comme jamais auparavant ?** 🚀  
👉 **Clonez, testez, contribuez !** 👈