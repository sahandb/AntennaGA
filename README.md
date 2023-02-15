# AntennaGA
Helping an antenna company to provides better setup antennas to cover a rectangular m × n area.

Assume a cell phone company needs to setup antennas to cover a rectangular m × n area. Company has k different type of antenna. 𝑐𝑖 is the cost of a 𝑖 typed antenna. 𝑟𝑖 is the coverage radius of a i typed antenna. Antennas are installed at grid positions. When the Euclidian distance between the antenna and the point is less than or equal to 𝑟𝑖 , that point is covered by that antenna. A point is considered covered when at least one antenna covers it.
Company can install up to s antennas. However, they want to cover as much of the m × n grid as possible with minimum cost.
You are asked to design and implement a genetic algorithm for the problem. m, n, s, k, 𝑐𝑖 and 𝑟𝑖 i = 1, …, k are given as input. The fitness value 𝑓 to maximize and summary of parameters are given as:
m × n = grid dimensions k = number of different types of antenna 𝑐𝑖 = cost of type i, i = 1,2, ..., k
𝑟𝑖 = radius of type i, i = 1,2,..,k
u(x) = number of covered points in grid for individual x
p(x) = set of installed antennas for individual x
s = maximum number of antennas
t(j) = type of antenna j 𝑓(𝑥)=𝑢(𝑥)−Σ𝑐𝑡(𝑗)𝑝(𝑥)𝑗

As default encoding, use an array of size s as your genotype. Each allele is a triple (𝑖,𝑥,𝑦). 𝑖 is a number in [0,𝑘]. 0 means antenna is not installed, otherwise 𝑖 is the type of antenna. x is an integer in [0,𝑚] and y is an integer in [0,𝑛] denoting the position of the antenna. In this way, you expect to find the positions and types of antennas to install in the grid. Also use the following parameters in the default implementation:
• Random initialization of each integer value. Only valid triples.
• Population size 100
• Tournament selection
• 5% mutation probability. Randomly set one of the elements of the triple.
• One-point crossover
• 1% elitism. Replace worst offspring with best parent in the next generation.
Then make an experiment with different parameter setups. Here are some parameters for experiment:
• Different crossover operators (arithmetic crossovers etc.)
• Different selection mechanisms/pressures
• Another possible encoding or another idea you have (just ask me before)
