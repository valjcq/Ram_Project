# Ce code python a pour but de générer la structure de données de la RAM à  partir d'un fichier texte comportant le mot en entrée suivi de la liste d'instructions.
# Le fichier texte doit être sous la forme suivante:
#   - La première ligne doit contenir le mot en entrée
#   - Les lignes suivantes doivent contenir les instructions de la RAM
#   - Les instructions doivent être séparées par des virgules

import re


class ram:
    """Classe qui représente la machine RAM"""
    def __init__(self, lInstructions):
        self.pos = 0
        self.instructions = lInstructions
        self.registre = {}

    def __str__(self):
        return "\ninstructions = " + str(self.instructions)

    def __repr__(self):
        return "\ninstructions = " + str(self.instructions)

    def get_registre(self, name, i):
        """
        Renvoie la valeur du registre "name" à l'indice i
        Si le registre n'existe pas, ou que l'indice est supérieur à la taille
        du registre, on crée le registre et on met des
        0 à la place des valeurs manquantes
        """
        if isinstance(i, tuple):
            i = self.get_registre(i[0], i[1])
        if self.registre.get(name) is None:
            self.registre[name] = [0] * i
        if len(self.registre[name]) <= i:
            self.registre[name] += [0] * (i - len(self.registre[name]) + 1)
        return self.registre[name][i]

    def add(self, a, b):
        """
        Instruction ADD
        a: registre ou valeur
        b: registre ou valeur
        On ajoute a et b et on retourne le résultat
        """
        if isinstance(a, tuple):
            a = self.get_registre(a[0], a[1])
        if isinstance(b, tuple):
            b = self.get_registre(b[0], b[1])
        self.pos += 1
        return a + b

    def jeq(self, a, b, c):
        """
        Instruction JEQ
        a: registre ou valeur
        b: registre ou valeur
        c: valeur
        Si a == b alors on saute à l'instruction c
        Sinon on passe à l'instruction suivante
        """
        if isinstance(a, tuple):
            a = self.get_registre(a[0], a[1])
        if isinstance(b, tuple):
            b = self.get_registre(b[0], b[1])
        if isinstance(c, tuple):
            c = self.get_registre(c[0], c[1])
        if a == b:
            self.pos += c
        else:
            self.pos += 1

    def jle(self, a, b, c):
        """
        Instruction JLE
        a: registre ou valeur
        b: registre ou valeur
        c: valeur
        Si a <= b alors on saute à l'instruction c
        Sinon on passe à l'instruction suivante
        """
        print(f"a = {a}, b = {b}, c = {c}")
        if isinstance(a, tuple):
            a = self.get_registre(a[0], a[1])
        if isinstance(b, tuple):
            b = self.get_registre(b[0], b[1])
        if isinstance(c, tuple):
            c = self.get_registre(c[0], c[1])
        if a <= b:
            self.pos += c
        else:
            self.pos += 1

    def jge(self, a, b, c):
        """
        Instruction JGE
        a: registre ou valeur
        b: registre ou valeur
        c: valeur
        Si a => b alors on saute à l'instruction c
        Sinon on passe à l'instruction suivante
        """
        if isinstance(a, tuple):
            a = self.get_registre(a[0], a[1])
        if isinstance(b, tuple):
            b = self.get_registre(b[0], b[1])
        if isinstance(c, tuple):
            c = self.get_registre(c[0], c[1])
        if a >= b:
            self.pos += c
        else:
            self.pos += 1

    def stocker(self, a, rg: tuple):
        if self.registre.get(rg[0]) is None:
            self.registre[rg[0]] = [0] * rg[1]
        if isinstance(rg[1], tuple):
            rg = (rg[0], self.get_registre(rg[1][0], rg[1][1]))
        if len(self.registre[rg[0]]) <= rg[1]:
            self.registre[rg[0]] += [0] * (rg[1] -
                                           len(self.registre[rg[0]]) + 1)
        self.registre[rg[0]][rg[1]] = a

    def afficher_config(self):
        """
        Affiche la configuration actuelle de la RAM, c'est-à-dire
        la position et l'instruction actuelle, et les valeurs
        des registres.
        """
        print("Configuration actuelle de la RAM")
        print("Position = ", self.pos)
        if self.pos < len(self.instructions):
            print("Instruction actuelle = ", self.instructions[self.pos])
        for key, value in self.registre.items():
            print(f"registre \"{key}\" = {value}")
        print("\n")

    def set_registre(self, name: str, input: str):
        self.registre[name] = list(map(int, input.split()))

    def run(self, n=None, aff=True):
        """
        Exécute n instructions de la RAM.
        Si n est None, exécute toutes les instructions jusqu'à la fin.
        """
        i = 0
        while True:
            i += 1
            if self.pos >= len(self.instructions):
                print("--------------Fin de l'exécution--------------")
                self.afficher_config()
                # TODO: Afficher un affichage de fin
                break
            if aff:
                self.afficher_config()
            instruction = self.instructions[self.pos]
            if instruction[0] == "ADD":
                self.stocker(self.add(instruction[1],
                                      instruction[2]), instruction[3])
            elif instruction[0] == "JEQ":
                self.jeq(instruction[1], instruction[2], instruction[3])
            elif instruction[0] == "JLE":
                self.jle(instruction[1], instruction[2], instruction[3])
            elif instruction[0] == "JGE":
                self.jge(instruction[1], instruction[2], instruction[3])
            else:
                print("Instruction non reconnue")
                break
            if n is None:
                continue
            elif i == n-1:
                break


def init_ram(path="/home/val/Git_Depot/Etudes/L3/S6/IN620/Projet Ram/ram.txt"):
    """
    Permet d'initialiser la RAM à partir d'un fichier texte.
    """
    with open(path, "r") as file:
        lInstructions = []
        instruction = file.readline().replace("(", ",").replace(")", "").strip()
        while instruction != "":
            lInstructions.append(instruction.split(","))
            # On remplace les parenthèses par des virgules pour pouvoir séparer
            # les arguments
            instruction = file.readline().replace("(", ",").replace(")", "").strip()
            # lorsqu'on a 'ADD(1,2,3)' on veut avoir ['ADD, '1', '2', '3']
            # On remplace les chaine de caractère d'entier par des entiers
            # quand c'est possible.
            for i in range(len(lInstructions[-1])):
                match = re.match(r"([a-zA-Z]+)(\d+)", lInstructions[-1][i])
                match2 = re.match(r"([a-zA-Z])@([a-zA-Z]+)(\d+)", lInstructions[-1][i])
                if match:  # Si on a une variable de la forme 'var1'
                    # On la transforme en tuple
                    lInstructions[-1][i] = (match.group(1), int(match.group(2)))
                elif match2:
                    lInstructions[-1][i] = (match2.group(1), (match2.group(2), int(match2.group(3))))
                else:  # Si on a un entier
                    try:
                        # On le transforme en entier
                        lInstructions[-1][i] = int(lInstructions[-1][i])
                    except ValueError:
                        pass
    return ram(lInstructions)


class graph_instruc:
    """Classe qui représente le graphe des instructions de la RAM"""
    def __init__(self, linstructions):
        self.instructions = linstructions
        self.init_graph()

    def __repr__(self) -> str:
        return str(self.graph)

    def init_graph(self):
        self.graph = {}
        self.graph[0] = (0)
        # Créer un dictionnaire qui représente le graphe des instructions
        # Chaque clé représente l'index de l'instruction dans la liste
        # d'instructions et chaque valeur est un tuple qui représente
        # les instructions accessibles.
        for i, instruc in enumerate(self.instructions):
            if instruc[0] == "ADD":
                if i+1 < len(self.instructions):
                    self.graph[i] = i+1
            elif instruc[0] in ("JEQ", "JG", "JLE"):
                if isinstance(instruc[3], int):
                    if isinstance(instruc[1], int) and isinstance(instruc[2], int):
                        if instruc[0] == "JEQ" and instruc[1] == instruc[2]:
                            self.graph[i] = instruc[3] + i
                        elif instruc[0] == "JGE" and instruc[1] >= instruc[2]:
                            self.graph[i] = instruc[3] + i
                        elif instruc[0] == "JLE" and instruc[1] <= instruc[2]:
                            self.graph[i] = instruc[3] + i
                    else:
                        self.graph[i] = (i + 1, instruc[3] + i + 1)
            else:
                print("Instruction non reconnue")
                break

    def get_graph(self):
        return self.graph

    def remove_instruction(self, i):
        # on met à jour les clés du dictionnaire
        # si on supprime une instruction, on doit mettre à jour
        # les valeurs des instructions qui sont supérieures à i
        for key in self.graph.keys():
            if isinstance(self.graph[key], tuple):
                self.graph[key] = tuple([x-1 if x > i else x for x in self.graph[key]])
            else:
                self.graph[key] = self.graph[key]-1 if self.graph[key] > i else self.graph[key]
        for j in range(0, len(self.instructions)):
            if self.instructions[j][0] in ("JEQ", "JG", "JLE"):
                if self.instructions[j][3] + j > i > j:
                    self.instructions[j][3] -= 1    # On met à jour l'indice de l'instruction
        # on fait la même chose pour les clés
        # du dictionnaire
        self.graph = {key-1 if key > i else key: value for key, value in self.graph.items()}
        # Supprimer une instruction du graphe
        self.graph.pop(i)
        self.instructions.pop(i)

    def remove_unused_instruction(self):
        # Supprimer les instructions qui ne sont pas utilisées
        # dans le graphe
        keys = list(self.graph.keys())
        usedInstru = set()
        for value in self.graph.values():
            if isinstance(value, int):
                usedInstru.add(value)
            elif isinstance(value, tuple):
                usedInstru.update(value)
        print(f"usedInstru = {usedInstru}")
        for key in keys:
            if not key:  # On ne supprime pas la racine (0)
                continue
            if key not in usedInstru:
                self.remove_instruction(key)

    def optimize(self, linstructions):
        # Optimiser le graphe des instructions
        # On supprime les instructions qui ne sont pas utilisées
        # On fusionne les instructions qui peuvent l'être
        self.remove_unused_instruction()
        for key, value in self.graph.items():
            # Si on a une instruction de type ADD (avec un seul successeur)
            # et que le successeur est une instruction de type ADD
            print(f"key = {key}, value = {value}")
            if isinstance(value, int) and \
               isinstance(self.graph[value], int):
                # On fusionne les deux instructions si possible
                # On vérifie que les arguments sont de type (int, int, tuple)
                # et que le registre en output est en entrée de l'instruction
                # suivante
                print(f"linstructions[key] = {linstructions[key]}")
                if isinstance(linstructions[key][1], int) and \
                   isinstance(linstructions[key][2], int) and \
                   isinstance(linstructions[key][3], tuple):
                    print(f"linstructions[key][3] = {linstructions[key][3]}")
                    print(f"linstructions[value][1] = {linstructions[value][1]}")
                    if linstructions[key][3] == linstructions[value][1]:
                        # On remplace l'instruction ADD par une nouvelle
                        # instruction de type ADD
                        res_add1 = linstructions[key][1] + \
                            linstructions[key][2]
                        new_instruc = ("ADD", res_add1, linstructions[key][2],
                                       linstructions[key][3])
                        linstructions[key] = new_instruc
                        # On supprime l'instruction suivante
                        self.remove_instruction(value)
                        self.optimize(linstructions)
                        break
                    elif linstructions[key][3] == linstructions[value][2]:
                        res_add2 = linstructions[key][1] + \
                            linstructions[key][2]
                        new_instruc = ("ADD", linstructions[key][1], res_add2,
                                       linstructions[key][3])
                        linstructions[key] = new_instruc
                        self.remove_instruction(value)
                        self.optimize(linstructions)
                        break
                # on doit ensuite mettre à jour le graphe
                self.init_graph()
                print(f"linstructions = {linstructions}")
                print(f"graph = {self.graph}")
            elif linstructions[key][0] == "JEQ":
                # Si on a une instruction de type JEQ
                # si on a deux arguments de type (int, int, tuple)
                # et que les deux int ne sont pas égaux
                # on supprime l'instruction JEQ
                if isinstance(linstructions[key][1], int) and \
                   isinstance(linstructions[key][2], int) and \
                   isinstance(linstructions[key][3], int):
                    if linstructions[key][1] != linstructions[key][2]:
                        self.remove_instruction(key)
                # on doit ensuite mettre à jour le graphe
                self.init_graph()
                self.optimize(linstructions)
                break
            elif linstructions[key][0] == "JLE":
                # Si on a une instruction de type JLE
                # si on a deux arguments de type (int, int, tuple)
                # et que le premier int est supérieur au deuxième
                # on supprime l'instruction JLE
                if isinstance(linstructions[key][1], int) and \
                   isinstance(linstructions[key][2], int) and \
                   isinstance(linstructions[key][3], int):
                    if linstructions[key][1] >= linstructions[key][2]:
                        self.remove_instruction(key)
                # on doit ensuite mettre à jour le graphe
                self.init_graph()
                self.optimize(linstructions)
                break
            elif linstructions[key][0] == "JGE":
                # Si on a une instruction de type JGE
                # si on a deux arguments de type (int, int, tuple)
                # et que le premier int est inférieur au deuxième
                # on supprime l'instruction JGE
                if isinstance(linstructions[key][1], int) and \
                   isinstance(linstructions[key][2], int) and \
                   isinstance(linstructions[key][3], int):
                    if linstructions[key][1] <= linstructions[key][2]:
                        self.remove_instruction(key)
                # on doit ensuite mettre à jour le graphe
                self.init_graph()
                self.optimize(linstructions)
                break


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Veuillez entrer un argument")
        sys.exit(1)
    if sys.argv[1] == "AB":
        # Test de la classe ram
        machine1 = init_ram("/home/val/Git_Depot/Etudes/L3/S6/IN620/Projet Ram/ram_AB.txt")
        machine1.set_registre("A", sys.argv[2])
        machine1.set_registre("B", sys.argv[3])
        print(machine1)
        machine1.run(aff=False)
    if sys.argv[1] == "tableau":
        machine2 = init_ram("/home/val/Git_Depot/Etudes/L3/S6/IN620/Projet Ram/ram_Tableau.txt")
        machine2.set_registre("T", "2 1 3 2 2")
        machine2.set_registre("N", "4")
        print(machine2)
        machine2.run(aff=False)
    if sys.argv[1] == "Automate":
        machine3 = init_ram("/home/val/Dépots Github/Projet Ram/Partie2.txt")
        print(machine3)
        while True:
            machine3.run(10, aff=True)
            input("Appuyez sur Entrée pour continuer...")

