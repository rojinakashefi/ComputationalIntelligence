import copy
import numpy as np
from player import Player
import random


class Evolution:
  fitnesses = ([], [], [])
  def __init__(self):
    self.game_mode = "Neuroevolution"

  def next_population_selection(self, players, num_players):
    """
    Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
    fitness value.

    :param players: list of players in the previous generation
    :param num_players: number of players that we return
    """
    # TODO (Implement top-k algorithm here)
    # selection = self.sorting_players(players)[:num_players]
    # TODO (Additional: Implement roulette wheel here)
    # selection = self.roulette_wheel(players, num_players)
    # TODO (Additional: Implement SUS here)
    selection = self.sus(players, num_players)
    # TODO (Additional: Implement q-tournament)
    # selection = self.q_tournament(2, players, num_players)
    # TODO (Additional: Learning curve)
    self.learning_curve(players)
    return selection

  def sorting_players(self, players):
    return sorted(players, reverse=True, key=lambda player: player.fitness)

  def learning_curve(self, players):
    sorted_players = sorted(players, key=lambda player: player.fitness, reverse=True)
    best_fitness = sorted_players[0].fitness
    worst_fitness = sorted_players[len(sorted_players) - 1].fitness
    fitnesses = [player.fitness for player in players]
    avg_fitness = sum(fitnesses) / len(fitnesses)
    with open('learning_curve.txt', 'a') as f:
      f.write(f'{best_fitness} {worst_fitness} {avg_fitness} \n')

  def roulette_wheel(self, players, num_players):
    fitness_sum = sum([player.fitness for player in players])
    each_player_prob = [player.fitness / fitness_sum for player in players]
    return list(np.random.choice(players, num_players, p=each_player_prob))

  def sus(self, players, num_players):
    player = sorted(players, reverse=True, key=lambda player: player.fitness)
    fitness_sum = sum([player.fitness for player in players])
    each_player_prob = [player.fitness / fitness_sum for player in players]
    selection_of_survivals = []
    pointer_param = np.random.uniform(0, 1 / float(num_players))
    for i in range(num_players):
      start_pointer = 0
      for j in range(len(players)):
        if start_pointer < pointer_param < start_pointer + each_player_prob[j]:
          selection_of_survivals.append(players[j])
          break
        start_pointer += each_player_prob[j]
      pointer_param += (1 / float(num_players))
    return selection_of_survivals

  def q_tournament(self, q, players, num_players):
    selection_of_survivors = []
    for i in range(num_players):
      competitors = random.sample(players, q)
      selection_of_survivors.append(max(competitors, key=lambda player: player.fitness))
    return selection_of_survivors

  def generate_new_population(self, num_players, prev_players=None):
    """
    Gets survivors and returns a list containing num_players number of children.
    :param num_players: Length of returning list
    :param prev_players: List of survivors
    :return: A list of children
    """
    first_generation = prev_players is None
    cs_prob = np.random.uniform(0, 1)
    m_prob = 0.8

    if first_generation:
      return [Player(self.game_mode) for _ in range(num_players)]
    else:
      # TODO ( Parent selection and child generation )
      new_players = []
      parents = self.q_tournament(2, prev_players, num_players)
      children = []
      # mutation
      for i in range(len(parents)):
        if m_prob >= np.random.uniform(0, 1):
          new_players.append(self.mutate(parents[i]))
        else:
          new_players.append(self.clone_player(parents[i]))
      # crossover
      i = 0
      while i < len(parents):
        if cs_prob >= np.random.uniform(0, 1):
          new_players[i], new_players[i + 1] = self.cross_over(parents[i], parents[i + 1])
        i += 2
      return new_players

  def mutate(self, parent):
    child = self.clone_player(parent)
    sigma = 0.8
    for i in range(len(parent.nn.layer_sizes) - 1):
      child.nn.weights[i] += sigma * np.random.standard_normal(size=(parent.nn.layer_sizes[i + 1], parent.nn.layer_sizes[i]))
      child.nn.bias[i] += sigma * np.random.standard_normal(size=(parent.nn.layer_sizes[i + 1], 1))
    return child

  def cross_over(self, parent1, parent2):
    alpha = 0.1
    child1 = self.clone_player(parent1)
    child2 = self.clone_player(parent2)
    for i in range(len(parent1.nn.layer_sizes) - 1):
      child1.nn.weights[i] = alpha * parent1.nn.weights[i] + (1 - alpha) * parent2.nn.weights[i]
      child2.nn.weights[i] = alpha * parent2.nn.weights[i] + (1 - alpha) * parent1.nn.weights[i]
      child1.nn.bias[i] = alpha * parent1.nn.bias[i] + (1 - alpha) * parent2.nn.bias[i]
      child2.nn.bias[i] = alpha * parent2.nn.bias[i] + (1 - alpha) * parent1.nn.bias[i]
    return child1, child2

  def clone_player(self, player):
    """
    Gets a player as an input and produces a clone of that player.
    """
    new_player = Player(self.game_mode)
    new_player.nn = copy.deepcopy(player.nn)
    new_player.fitness = player.fitness
    return new_player

