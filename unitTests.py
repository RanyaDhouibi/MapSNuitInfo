import unittest
import networkx as nx
from NetworkConfiguratorCLI import NetworkConfigurationGenerator

class TestNetworkConfigurationGenerator(unittest.TestCase):

    def test_is_graphical_valid_sequence(self):
        degree_sequence = [3, 3, 2, 2, 1, 1]
        result = NetworkConfigurationGenerator.is_graphical(degree_sequence)
        self.assertTrue(result)


    def test_generate_configurations_valid(self):
        degree_sequence = [3, 3, 2, 2, 1, 1]
        generator = NetworkConfigurationGenerator()
        configurations = generator.generate_configurations(degree_sequence)
        self.assertGreater(len(configurations), 0)

    def test_generate_configurations_invalid(self):
        degree_sequence = [3, 3, 3, 2, 1]
        generator = NetworkConfigurationGenerator()
        configurations = generator.generate_configurations(degree_sequence)
        self.assertEqual(len(configurations), 1)

    def test_check_degree_constraints_valid(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]
        degree_sequence = [2, 2, 2, 2, 2]
        result = NetworkConfigurationGenerator._check_degree_constraints(edges, degree_sequence)
        self.assertTrue(result)

    def test_check_degree_constraints_invalid(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
        degree_sequence = [2, 2, 2, 2, 2]
        result = NetworkConfigurationGenerator._check_degree_constraints(edges, degree_sequence)
        self.assertFalse(result)

    def test_are_isomorphic(self):
        edges_1 = frozenset([(0, 1), (1, 2), (2, 3), (0, 3)])
        edges_2 = frozenset([(0, 1), (1, 3), (3, 2), (0, 2)])
        graph_1 = NetworkConfigurationGenerator._create_graph(edges_1, 4)
        graph_2 = NetworkConfigurationGenerator._create_graph(edges_2, 4)
        result = NetworkConfigurationGenerator._are_isomorphic(graph_1, graph_2)
        self.assertTrue(result)

    def test_are_isomorphic_not(self):
        edges_1 = frozenset([(0, 1), (1, 2), (2, 3)])
        edges_2 = frozenset([(0, 1), (1, 2), (0, 2)])
        graph_1 = NetworkConfigurationGenerator._create_graph(edges_1, 4)
        graph_2 = NetworkConfigurationGenerator._create_graph(edges_2, 3)
        result = NetworkConfigurationGenerator._are_isomorphic(graph_1, graph_2)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
