import itertools
import networkx as nx
import argparse
import json
import matplotlib.pyplot as plt
from typing import List, Set, Tuple

# ASCII Art for the header (MINDS)
def print_ascii_header():
    ascii_art = """
        .|'''', '||'''|, .|''''|, '||      ||` '||\   ||` 
        ||       ||   || ||    ||  ||      ||   ||\\  ||  
        ||       ||...|' ||    ||  ||  /\  ||   || \\ ||  
        ||       || \\   ||    ||   \\//\\//    ||  \\||  
        `|....' .||  \\. `|....|'    \/  \/    .||   \||.                                           
                                   
    """
    print(ascii_art)

class NetworkConfigurationGenerator:
    @staticmethod
    def is_graphical(degree_sequence: List[int]) -> bool:
        """
        Vérifie si une séquence de degrés peut former un graphe valide en utilisant le théorème d'Erdős–Gallai.

        Args:
        degree_sequence (List[int]): Liste triée des degrés des nœuds dans l'ordre décroissant

        Returns:
        bool: Si la séquence peut former un graphe valide
        """
        n = len(degree_sequence)
        sorted_degrees = sorted(degree_sequence, reverse=True)

        for k in range(1, n + 1):
            left_sum = sum(sorted_degrees[:k])
            right_sum = k * (k - 1) + sum(min(sorted_degrees[j], k) for j in range(k, n))

            if left_sum > right_sum:
                return False

        return True

    @staticmethod
    def generate_configurations(degree_sequence: List[int]) -> Set[frozenset]:
        """
        Génère toutes les configurations réseau uniques.

        Args:
        degree_sequence (List[int]): Séquence de degrés pour le réseau

        Returns:
        Set[frozenset]: Configurations réseau uniques
        """
        # Valider la séquence de degrés
        if not NetworkConfigurationGenerator.is_graphical(degree_sequence):
            return set()

        n = len(degree_sequence)
        unique_configs = set()

        # Générer toutes les combinaisons possibles d'arêtes
        for edges in itertools.combinations(
            itertools.combinations(range(n), 2),
            sum(degree_sequence) // 2
        ):
            # Vérifier les contraintes de degré
            if NetworkConfigurationGenerator._check_degree_constraints(edges, degree_sequence):
                # Utiliser frozenset pour représenter la configuration de manière canonique
                config = frozenset(edges)

                # Vérifier l'isomorphisme des graphes
                if not any(
                    NetworkConfigurationGenerator._are_isomorphic(
                        NetworkConfigurationGenerator._create_graph(config, n),
                        NetworkConfigurationGenerator._create_graph(existing_config, n)
                    )
                    for existing_config in unique_configs
                ):
                    unique_configs.add(config)

        return unique_configs

    @staticmethod
    def _check_degree_constraints(edges: Tuple[Tuple[int, int]], degree_sequence: List[int]) -> bool:
        """
        Vérifie si les arêtes respectent les contraintes de degré de la séquence donnée.

        Args:
        edges (Tuple[Tuple[int, int]]): Arêtes proposées
        degree_sequence (List[int]): Séquence de degrés à respecter

        Returns:
        bool: Si les arêtes respectent les contraintes
        """
        # Compter les degrés pour chaque nœud
        degrees = [0] * len(degree_sequence)
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1

        # Comparer avec les degrés requis
        return all(
            degrees[i] == degree_sequence[i]
            for i in range(len(degree_sequence))
        )

    @staticmethod
    def _create_graph(edges: frozenset, n: int) -> nx.Graph:
        """
        Crée un graphe NetworkX à partir d'un ensemble d'arêtes.

        Args:
        edges (frozenset): Ensemble d'arêtes
        n (int): Nombre de nœuds

        Returns:
        nx.Graph: Graphe créé
        """
        G = nx.Graph()
        G.add_nodes_from(range(n))
        G.add_edges_from(edges)
        return G

    @staticmethod
    def _are_isomorphic(G1: nx.Graph, G2: nx.Graph) -> bool:
        """
        Vérifie si deux graphes sont isomorphes.

        Args:
        G1 (nx.Graph): Premier graphe
        G2 (nx.Graph): Deuxième graphe

        Returns:
        bool: Si les graphes sont isomorphes
        """
        return nx.is_isomorphic(G1, G2)

    def generate_network_configurations(self, degree_sequence: List[int], save_to_json: bool, json_filename: str = "network_configurations.json", visualize: bool = False) -> List[List[Tuple[int, int]]]:
        """
        Génère des configurations réseau avec une sortie lisible par l'homme et une option de visualisation.

        Args:
        degree_sequence (List[int]): Séquence de degrés pour le réseau
        save_to_json (bool): Indique si les configurations doivent être sauvegardées dans un fichier JSON
        json_filename (str): Nom du fichier JSON pour sauvegarder les configurations
        visualize (bool): Indique si les graphes doivent être visualisés

        Returns:
        List[List[Tuple[int, int]]]: Liste des configurations réseau uniques
        """
        unique_configs = self.generate_configurations(degree_sequence)

        if save_to_json:
            with open(json_filename, 'w') as json_file:
                json.dump([list(config) for config in unique_configs], json_file, indent=4)

        # Visualisation des configurations
        if visualize:
            for i, config in enumerate(unique_configs, 1):
                G = self._create_graph(config, len(degree_sequence))
                plt.figure(i)
                nx.draw(G, with_labels=True, node_color="lightblue", font_weight="bold", node_size=500)
                plt.title(f"Configuration {i}")
                plt.show()

        return [list(config) for config in unique_configs]

# Fonction principale avec argparse pour la CLI
def main():
    # Afficher l'ASCII Art
    print_ascii_header()

    # Configurer les arguments CLI
    parser = argparse.ArgumentParser(description="Générer des configurations réseau uniques basées sur une séquence de degrés.")
    parser.add_argument('degree_sequence', metavar='D', type=int, nargs='+', help="Séquence de degrés sous forme d'entiers séparés par des espaces.")
    parser.add_argument('--save', action='store_true', help="Sauvegarder les configurations générées dans un fichier JSON.")
    parser.add_argument('--json_filename', type=str, default="network_configurations.json", help="Nom du fichier JSON pour sauvegarder les configurations.")
    parser.add_argument('--visualize', action='store_true', help="Visualiser les configurations générées.")
    args = parser.parse_args()

    # Vérifier que la séquence de degrés est valide
    degree_sequence = args.degree_sequence
    if not all(isinstance(d, int) and d >= 0 for d in degree_sequence):
        print("Erreur: La séquence de degrés doit être constituée de nombres entiers positifs.")
        return

    generator = NetworkConfigurationGenerator()

    try:
        configurations = generator.generate_network_configurations(degree_sequence, args.save, args.json_filename, args.visualize)

        print(f"\nConfigurations réseau uniques pour la séquence de degrés {degree_sequence}:")
        for i, config in enumerate(configurations, 1):
            print(f"\nConfiguration {i}:")
            for edge in config:
                print(f" Connexion entre les nœuds {edge[0]} et {edge[1]}")

        print(f"\nNombre total de configurations uniques : {len(configurations)}")

        if args.save:
            print(f"\nLes configurations ont été sauvegardées dans '{args.json_filename}'.")

    except Exception as e:
        print(f"Erreur lors de la génération des configurations : {e}")

if __name__ == "__main__":
    main()
