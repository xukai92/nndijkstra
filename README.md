# Learn Dijkstra's Algorithm using Artificial Nerual Networks

This project is aimed to learn the traditional graph algorithm *Dijkstra's shortest path algorithm* using a neural network and evaluate its performance on *unexpected input*, i.e. graphs with negative weights.

## Methods and plan

- [ ] Use the [Erdős–Rényi model](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model) to generate a batch of random graphs with non-negative weitghs
- [ ] Make labels using Dijkstra's algorithm

> Question: what output do we want? the length of shorest path? the terminating node? or something else?

- [ ] Train a NN to learn Dijkstra's algorithm using the synthesised data
- [ ] Use the Erdős–Rényi model to generate a batch of random graphs with negative weitghs
- [ ] Evaluate the performance of the NN on the new dataset with graphs with negative weitghs

## Design details

### Graph representation

Adjacency matrix or adjacency list?

### Graph and shorest paht encoding

How can we encode a graph and its corresponding output to feed into a NN?

## Contributers

- [Kai Xu](xukai92.github.io) - University of Cambridge, 
- [Yong Li](neilli1992.github.io) - University of Oxford
