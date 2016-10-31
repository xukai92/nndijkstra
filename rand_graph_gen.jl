if length(ARGS) != 4
  print("Usage: julia reand_graph_gen.jl [N] [p] [M] [o_file]\n")
  print("Set N or p to 0 to randomly set it\n")
  exit()
end

using Distributions

# Number of vertices
N = ARGS[1] != 0 ? parse(Int64, ARGS[1]) : rand(DiscreteUniform(5, 10))
# Probablity of connection
p = ARGS[2] != 0 ? parse(Float64, ARGS[2]) : rand(Uniform(0, 1))
# Number of graphs
M = parse(Int64, ARGS[3])
# Output file
o_file = ARGS[4]


graphs = Array{Any}(M)

for idx in 1:M
  # Initialise adjacent matrix
  # Without loss of generality we use weigths with whole numbers
  ad_matrix = Array{Int64, 2}(N, N)

  for row in 1:N; for col in 1:N;
    if row != col
      if rand() < p
        # Connect with random weight
        ad_matrix[row, col] = rand(DiscreteUniform(1, 5))
      else
        # Disconnect
        ad_matrix[row, col] = 0
      end
    else
      # Connect with itself
      ad_matrix[row, col] = 1
    end
  end; end;
  graphs[idx] = ad_matrix
end

open(o_file, "w") do f
  for idx in 1:M
    ad_matrix = graphs[idx]
    write(f, "$N ")
    for row in 1:N; for col in 1:N;
      write(f, "$(ad_matrix[row, col]) ")
    end; end;
    write(f, '\n')
  end
end
