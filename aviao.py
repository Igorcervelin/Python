from random import Random
from time import time
from math import cos
from math import pi
from inspyred import ec
from inspyred.ec import terminators
import numpy as np
import os

def generate_(random, args):
    size = args.get('num_inputs', 12) # Genes
    return [random.randint(0, 16000) for i in range(size)] 

# Avaliar soluções
def evaluate_(candidates, args):
    fitness = []
    for cs in candidates:
        fit = perform_fitness(cs[0], cs[1], cs[2], cs[3], cs[4], cs[5], cs[6], cs[7], cs[8], cs[9], cs[10], cs[11])
        fitness.append(fit)
    return fitness

def perform_fitness(cs1, cs2, cs3, cs4, cs5, cs6, cs7, cs8, cs9, cs10, cs11, cs12):

    cs1 = np.round(cs1)
    cs2 = np.round(cs2)
    cs3 = np.round(cs3)
    cs4 = np.round(cs4)
    cs5 = np.round(cs5)
    cs6 = np.round(cs6)
    cs7 = np.round(cs7)
    cs8 = np.round(cs8)
    cs9 = np.round(cs9)
    cs10 = np.round(cs10)
    cs11 = np.round(cs11)
    cs12 = np.round(cs12)
    fit = float((cs1 * 0.31 + cs2 * 0.31 + cs3 * 0.31 + cs4 * 0.38 + cs5 * 0.38 + cs6 * 0.38 + cs7 * 0.35 + cs8 * 0.35 + cs9 * 0.35 + cs10 * 0.285 + cs11 * 0.285 + cs12 * 0.285) / 12151.56)
  
   #Restrição quantidade
   #Lucromax*toneladas/kg
    h1 = np.maximum(0, float(((cs1+cs2+cs3) - (18000)) / (18000/10)))
    h2 = np.maximum(0, float(((cs4+cs5+cs6) - (15000)) / (15000/10)))
    h3 = np.maximum(0, float(((cs7+cs8+cs9) - (23000)) / (23000/10)))
    h4 = np.maximum(0, float(((cs10+cs11+cs12) - (12000)) / (12000/10)))

    #Restrição volume
    #Volumemax*toneladas/kg

    h5 = np.maximum(0, float(((cs1 * 0.48 + cs4 * 0.65 + cs7 * 0.58 + cs10 * 0.39) - 6800) / (6800/10)))
    h6 = np.maximum(0, float(((cs2 * 0.48 + cs5 * 0.65 + cs8 * 0.58 + cs11 * 0.39) - 8700) / (8700/10)))
    h7 = np.maximum(0, float(((cs3 * 0.48 + cs6 * 0.65 + cs9 * 0.58 + cs12 * 0.39) - 5300) / (5300/10)))

    #peso
    #Lucromax*toneladas/kg

    h8 = np.maximum(0, float(((cs1 + cs4 + cs7 + cs10) - 10000) / (10000/10)))
    h9 = np.maximum(0, float(((cs2 + cs5 + cs8 + cs11) - 16000) / (16000/10)))
    h10 = np.maximum(0, float(((cs3 + cs6 + cs9 + cs12) - 8000) / (8000/10)))

    fit = fit - (h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + h10)

    return fit


def solution_evaluation(D1, C1, T1, D2, C2, T2, D3, C3, T3, D4, C4, T4):

    D1 = np.round(D1)
    D2 = np.round(D2)
    D3 = np.round(D3)
    D4 = np.round(D4)
    T1 = np.round(T1)
    T2 = np.round(T2)
    T3 = np.round(T3)
    T4 = np.round(T4)
    C1 = np.round(C1)
    C2 = np.round(C2)
    C3 = np.round(C3)
    C4 = np.round(C4)

    print("")
    print(" RELATORIO DE EXECUCAO")
    print("")
    print("Lucro total", float((D1*0.31)+(C1*0.31)+(T1*0.31)+(D2*0.38)+(C2*0.38)+(T2*0.38)+(D3*0.35)+(C3*0.35)+(T3*0.35)+(D4*0.285)+(C4*0.285)+(T4*0.285)))
    print("Volume dianteiro", float((D1*0.48)+(D2*0.65)+(D3*0.58)+(D4*0.39)))
    print("Volume centro",float((C1*0.48)+(C2*0.65)+(C3*0.58)+(C4*0.39)))
    print("Volume traseiro",float((T1*0.48)+(T2*0.65)+(T3*0.58)+(T4*0.39)))
    print("Total",float((D1*0.48)+(D2*0.65)+(D3*0.58)+(D4*0.39)+(C1*0.48)+(C2*0.65)+(C3*0.58)+(C4*0.39)+(T1*0.48)+(T2*0.65)+(T3*0.58)+(T4*0.39)))
    print("")
    print("Carga 1 - Dianteiro", D1)
    print("Carga 1 - Central", C1)
    print("Carga 1 - Traseiro", T1)
    print("Carga 1 - Total", D1+C1+T1)
    print("")
    print("Carga 2 - Dianteiro", D2)
    print("Carga 2 - Central", C2)
    print("Carga 2 - Traseiro", T2)
    print("Carga 2 - Total", D2+C2+T2)
    print("")
    print("Carga 3 - Dianteiro", D3)
    print("Carga 3 - Central", C3)
    print("Carga 3 - Traseiro", T3)
    print("Carga 3 - Total", D3+C3+T3)
    print("")
    print("Carga 4 - Dianteiro", D4)
    print("Carga 4 - Central", C4)
    print("Carga 4 - Traseiro", T4)
    print("Carga 4 - Total", D4+C4+T4)

def main():
    rand = Random()
    rand.seed(int(time()))

    ea = ec.GA(rand)
    ea.selector = ec.selectors.tournament_selection
    ea.variator = [ec.variators.uniform_crossover,
                   ec.variators.gaussian_mutation]

    ea.replacer = ec.replacers.steady_state_replacement

    ea.terminator = terminators.generation_termination

    ea.observer = [ec.observers.stats_observer, ec.observers.file_observer]

    final_pop = ea.evolve(generator=generate_,
                          evaluator=evaluate_,
                          pop_size=100000,
                          maximize=True,
                          bounder=ec.Bounder(0, 16000),
                          max_generations=1000,
                          num_inputs= 12,
                          crossover_rae = 1.0,
                          num_crossover_points = 1,
                          mutation_rate = 0.5,
                          num_elites = 1,
                          num_selected = 12,
                          tournament_size = 12,
                          statistics_file=open("aviao_stats.csv", "w"),
                          individuals_file=open("aviao_individuais.csv", "w"))

    final_pop.sort(reverse=True) #Melhor candidato
    print(final_pop[0])

    perform_fitness(final_pop[0].candidate[0], final_pop[0].candidate[1], final_pop[0].candidate[2], final_pop[0].candidate[3], final_pop[0].candidate[4], final_pop[0].candidate[5], final_pop[0].candidate[6], final_pop[0].candidate[7], final_pop[0].candidate[8], final_pop[0].candidate[9], final_pop[0].candidate[10], final_pop[0].candidate[11])
    solution_evaluation(final_pop[0].candidate[0], final_pop[0].candidate[1], final_pop[0].candidate[2], final_pop[0].candidate[3], final_pop[0].candidate[4], final_pop[0].candidate[5], final_pop[0].candidate[6], final_pop[0].candidate[7], final_pop[0].candidate[8], final_pop[0].candidate[9], final_pop[0].candidate[10], final_pop[0].candidate[11])


main()