class ArvoreGenealogica:
    def __init__(self):
        # Armazena os pares (progenitor, filho)
        self._progenitores = set()
        # Armazena o sexo de cada pessoa
        self._sexos = {}

    def adicionar_progenitor(self, progenitor: str, filho: str):
        """Adiciona a relação progenitor(progenitor, filho)."""
        self._progenitores.add((progenitor.lower().strip(), filho.lower().strip()))

    def definir_sexo(self, pessoa: str, sexo: str):
        """Define o sexo de uma pessoa ('masculino' ou 'feminino')."""
        self._sexos[pessoa.lower().strip()] = sexo.lower().strip()

    # --- Regras / Relações Familiares ---

    def progenitor(self, p: str, f: str) -> bool:
        """progenitor(P, F)"""
        return (p.lower().strip(), f.lower().strip()) in self._progenitores

    def sexo(self, pessoa: str, s: str) -> bool:
        """sexo(Pessoa, Sexo)"""
        return self._sexos.get(pessoa.lower().strip()) == s.lower().strip()

    def pai(self, p: str, f: str) -> bool:
        """pai(X, Y) :- progenitor(X, Y), sexo(X, masculino)."""
        return self.progenitor(p, f) and self.sexo(p, "masculino")

    def mae(self, m: str, f: str) -> bool:
        """mae(X, Y) :- progenitor(X, Y), sexo(X, feminino)."""
        return self.progenitor(m, f) and self.sexo(m, "feminino")

    def filho(self, f: str, p: str) -> bool:
        """filho(X, Y) :- progenitor(Y, X)."""
        return self.progenitor(p, f)

    def irmao(self, x: str, y: str) -> bool:
        """irmao(X, Y) :- progenitor(A, X), progenitor(A, Y), X \== Y, sexo(X, masculino)."""
        x_lbl, y_lbl = x.lower().strip(), y.lower().strip()
        if x_lbl == y_lbl or not self.sexo(x_lbl, "masculino"):
            return False
        for a, f in self._progenitores:
            if f == x_lbl and (a, y_lbl) in self._progenitores:
                return True
        return False

    def irma(self, x: str, y: str) -> bool:
        """irma(X, Y) :- progenitor(A, X), progenitor(A, Y), X \== Y, sexo(X, feminino)."""
        x_lbl, y_lbl = x.lower().strip(), y.lower().strip()
        if x_lbl == y_lbl or not self.sexo(x_lbl, "feminino"):
            return False
        for a, f in self._progenitores:
            if f == x_lbl and (a, y_lbl) in self._progenitores:
                return True
        return False

    def vo_m(self, x: str, y: str) -> bool:
        """vô(X, Y) :- progenitor(X, A), progenitor(A, Y), sexo(X, masculino)."""
        x_lbl, y_lbl = x.lower().strip(), y.lower().strip()
        if not self.sexo(x_lbl, "masculino"):
            return False
        for p1, a in self._progenitores:
            if p1 == x_lbl and (a, y_lbl) in self._progenitores:
                return True
        return False

    def vo_f(self, x: str, y: str) -> bool:
        """vó(X, Y) :- progenitor(X, A), progenitor(A, Y), sexo(X, feminino)."""
        x_lbl, y_lbl = x.lower().strip(), y.lower().strip()
        if not self.sexo(x_lbl, "feminino"):
            return False
        for p1, a in self._progenitores:
            if p1 == x_lbl and (a, y_lbl) in self._progenitores:
                return True
        return False

    def tio(self, x: str, y: str) -> bool:
        """tio(X, Y) :- irmao(X, A), progenitor(A, Y)."""
        x_lbl, y_lbl = x.lower().strip(), y.lower().strip()
        for a, f in self._progenitores:
            if f == y_lbl and self.irmao(x_lbl, a):
                return True
        return False

    def tia(self, x: str, y: str) -> bool:
        """tia(X, Y) :- irma(X, A), progenitor(A, Y)."""
        x_lbl, y_lbl = x.lower().strip(), y.lower().strip()
        for a, f in self._progenitores:
            if f == y_lbl and self.irma(x_lbl, a):
                return True
        return False

    def primo(self, x: str, y: str) -> bool:
        """primo(X, Y) :- progenitor(P1, X), progenitor(P2, Y), (irmao(P1, P2); irma(P1, P2)), X \== Y."""
        x_lbl, y_lbl = x.lower().strip(), y.lower().strip()
        if x_lbl == y_lbl:
            return False
        p1_list = [p for p, f in self._progenitores if f == x_lbl]
        p2_list = [p for p, f in self._progenitores if f == y_lbl]
        for p1 in p1_list:
            for p2 in p2_list:
                if self.irmao(p1, p2) or self.irma(p1, p2):
                    return True
        return False

    def esposo(self, x: str, y: str) -> bool:
        """esposo(X, Y) :- progenitor(X, F), progenitor(Y, F), X \== Y, sexo(X, masculino)."""
        x_lbl, y_lbl = x.lower().strip(), y.lower().strip()
        if x_lbl == y_lbl or not self.sexo(x_lbl, "masculino"):
            return False
        for p1, f1 in self._progenitores:
            if p1 == x_lbl:
                if (y_lbl, f1) in self._progenitores:
                    return True
        return False

    def esposa(self, x: str, y: str) -> bool:
        """esposa(X, Y) :- progenitor(X, F), progenitor(Y, F), X \== Y, sexo(X, feminino)."""
        x_lbl, y_lbl = x.lower().strip(), y.lower().strip()
        if x_lbl == y_lbl or not self.sexo(x_lbl, "feminino"):
            return False
        for p1, f1 in self._progenitores:
            if p1 == x_lbl:
                if (y_lbl, f1) in self._progenitores:
                    return True
        return False

    # --- Métodos de Busca de Parentes ---

    def obter_todas_pessoas(self) -> list:
        """Retorna uma lista ordenada com o nome de todas as pessoas registradas."""
        todas = (
            set(p for p, _ in self._progenitores)
            | set(f for _, f in self._progenitores)
            | set(self._sexos.keys())
        )
        return sorted([p.capitalize() for p in todas])

    def buscar_parentes(self, pessoa: str, relacao: str) -> list:
        """Retorna a lista de pessoas que possuem a 'relacao' informada com a 'pessoa'."""
        pessoa_lbl = pessoa.lower().strip()
        relacoes = {
            "pai": lambda x, y: self.pai(x, y),
            "mae": lambda x, y: self.mae(x, y),
            "filho": lambda x, y: self.filho(x, y),
            "irmao": lambda x, y: self.irmao(x, y),
            "irma": lambda x, y: self.irma(x, y),
            "vo_m": lambda x, y: self.vo_m(x, y),
            "vo_f": lambda x, y: self.vo_f(x, y),
            "tio": lambda x, y: self.tio(x, y),
            "tia": lambda x, y: self.tia(x, y),
            "primo": lambda x, y: self.primo(x, y),
            "esposo": lambda x, y: self.esposo(x, y),
            "esposa": lambda x, y: self.esposa(x, y),
        }
        if relacao not in relacoes:
            return []

        todas_pessoas = set(p.lower() for p in self.obter_todas_pessoas())

        resultados = [
            p.capitalize()
            for p in todas_pessoas
            if relacoes[relacao](p, pessoa_lbl)
        ]
        return sorted(resultados)

    def obter_todos_parentes_por_pessoa(self, pessoa: str) -> dict:
        """Retorna um dicionário com todos os tipos de parentesco e a lista de parentes correspondente."""
        ordem_relacoes = [
            ("esposo", "Esposo"),
            ("esposa", "Esposa"),
            ("pai", "Pai"),
            ("mae", "Mãe"),
            ("filho", "Filho(a)"),
            ("irmao", "Irmão"),
            ("irma", "Irmã"),
            ("vo_m", "Vô"),
            ("vo_f", "Vó"),
            ("tio", "Tio"),
            ("tia", "Tia"),
            ("primo", "Primo(a)"),
        ]
        
        resultado = {}
        for chave, rotulo in ordem_relacoes:
            parentes = self.buscar_parentes(pessoa, chave)
            if parentes:
                resultado[rotulo] = parentes
                
        return resultado


def carregar_base_dados() -> ArvoreGenealogica:
    arvore = ArvoreGenealogica()

    progenitores_dados = [
        ("deus", "todos"), ("deus", "helena"), ("deus", "alice"),
        ("helena", "lucas"), ("arthur", "lucas"),
        ("alice", "cecilia"), ("alice", "davi"), ("samuel", "cecilia"), ("samuel", "davi"),
        ("sophia", "valentina"), ("sophia", "anthony"), ("sophia", "daniel"),
        ("lucas", "valentina"), ("lucas", "anthony"), ("lucas", "daniel"),
        ("cecilia", "ada"), ("pedro", "ada"),
        ("davi", "diego"), ("antonella", "diego"),
        ("valentina", "clara"), ("rafael", "clara"),
        ("daniel", "bruce"), ("daniel", "lorena"), ("lara", "bruce"), ("lara", "lorena"),
        ("sarah", "nicole"), ("sarah", "leonardo"), ("diego", "nicole"), ("diego", "leonardo"),
        ("clara", "melissa"), ("oliver", "melissa"),
        ("lorena", "bianca"), ("gabriela", "bianca"),
        ("nicole", "samira"), ("yuri", "samira"),
        ("melissa", "catharina"), ("melissa", "vitoria"), ("melissa", "bryan"),
        ("leon", "catharina"), ("leon", "vitoria"), ("leon", "bryan"),
        ("bianca", "yasmin"), ("peter", "yasmin"),
        ("samira", "nicolas"), ("isacc", "nicolas"),
        ("yasmin", "hinata"), ("natanael", "hinata"),
        ("nicolas", "luna"), ("charlotte", "luna")
    ]

    for p, f in progenitores_dados:
        arvore.adicionar_progenitor(p, f)

    sexos_dados = [
        ("arthur", "masculino"), ("samuel", "masculino"), ("lucas", "masculino"),
        ("pedro", "masculino"), ("davi", "masculino"), ("rafael", "masculino"),
        ("anthony", "masculino"), ("daniel", "masculino"), ("diego", "masculino"),
        ("oliver", "masculino"), ("bruce", "masculino"), ("leonardo", "masculino"),
        ("yuri", "masculino"), ("leon", "masculino"), ("peter", "masculino"),
        ("isacc", "masculino"), ("bryan", "masculino"), ("natanael", "masculino"),
        ("nicolas", "masculino"),
        ("helena", "feminino"), ("alice", "feminino"), ("sophia", "feminino"),
        ("cecilia", "feminino"), ("antonella", "feminino"), ("valentina", "feminino"),
        ("lara", "feminino"), ("ada", "feminino"), ("sarah", "feminino"),
        ("clara", "feminino"), ("lorena", "feminino"), ("gabriela", "feminino"),
        ("nicole", "feminino"), ("melissa", "feminino"), ("bianca", "feminino"),
        ("samira", "feminino"), ("catharina", "feminino"), ("vitoria", "feminino"),
        ("yasmin", "feminino"), ("charlotte", "feminino"), ("hinata", "feminino"),
        ("luna", "feminino")
    ]

    for p, s in sexos_dados:
        arvore.definir_sexo(p, s)

    return arvore


def menu_interativo():
    arvore = carregar_base_dados()

    while True:
        print("\n" + "=" * 50)
        print("      ÁRVORE GENEALÓGICA - MENU INTERATIVO")
        print("=" * 50)
        print("1. Buscar todos os parentes de uma pessoa")
        print("2. Listar todas as pessoas cadastradas")
        print("3. Adicionar nova relação de progenitor/filho")
        print("0. Sair")
        print("=" * 50)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- BUSCAR TODOS OS PARENTES DE UMA PESSOA ---")
            pessoa = input("Digite o nome da pessoa: ").strip()

            parentes_dict = arvore.obter_todos_parentes_por_pessoa(pessoa)

            print(f"\nPessoa: {pessoa.capitalize()}")
            print("Parentes:")
            
            if parentes_dict:
                for rotulo, lista in parentes_dict.items():
                    print(f"  {rotulo}: {', '.join(lista)}")
            else:
                print("  Nenhum parentesco encontrado.")

        elif opcao == "2":
            pessoas = arvore.obter_todas_pessoas()
            print(f"\n--- PESSOAS CADASTRADAS ({len(pessoas)}) ---")
            print(", ".join(pessoas))

        elif opcao == "3":
            print("\n--- ADICIONAR NOVA RELAÇÃO ---")
            p = input("Nome do progenitor(a): ").strip()
            f = input("Nome do filho(a): ").strip()
            s = input("Sexo do progenitor (masculino/feminino): ").strip().lower()

            arvore.adicionar_progenitor(p, f)
            if s in ["masculino", "feminino"]:
                arvore.definir_sexo(p, s)
            print(f"\nRelação adicionada com sucesso: {p.capitalize()} é progenitor(a) de {f.capitalize()}.")

        elif opcao == "0":
            print("\nEncerrando o programa. Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_interativo()
