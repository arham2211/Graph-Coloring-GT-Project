#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <chrono>  // Include for time measurement

using namespace std;
using namespace chrono;  // For time-related functions

// Function to check if a graph coloring is valid
bool isValidColoring(const vector<vector<int>>& graph, const map<int, int>& coloring) {
    for (int u = 0; u < graph.size(); ++u) {
        for (int v : graph[u]) {
            if (coloring.at(u) == coloring.at(v)) {
                return false;
            }
        }
    }
    return true;
}

// Function to perform greedy coloring
map<int, int> greedyColoring(const vector<vector<int>>& graph) {
    map<int, int> coloring;
    for (int node = 0; node < graph.size(); ++node) {
        set<int> adjacentColors;
        for (int neighbor : graph[node]) {
            if (coloring.find(neighbor) != coloring.end()) {
                adjacentColors.insert(coloring[neighbor]);
            }
        }
        // Assign the first available color
        int color = 0;
        while (adjacentColors.find(color) != adjacentColors.end()) {
            ++color;
        }
        coloring[node] = color;
    }
    return coloring;
}

int main() {
    // Start measuring time
    auto start_time = high_resolution_clock::now();  // Time before reading the input file

    ifstream inputFile("graph_input.txt");

    if (!inputFile.is_open()) {
        cerr << "Error opening file!" << endl;
        return 1;
    }

    int n_nodes, n_edges;

    // Read number of vertices and edges from the file
    inputFile >> n_nodes >> n_edges;

    // Initialize graph as an adjacency list
    vector<vector<int>> graph(n_nodes);

    // Read edges from the file
    for (int i = 0; i < n_edges; ++i) {
        int v1, v2;
        inputFile >> v1 >> v2;
        graph[v1].push_back(v2);
        graph[v2].push_back(v1);
    }

    inputFile.close();

    // Time after reading inputs
    auto end_time = high_resolution_clock::now();

    // Perform greedy coloring
    map<int, int> coloring = greedyColoring(graph);

    // Print the coloring result
    cout << "\nColoring:" << endl;
    for (auto it = coloring.begin(); it != coloring.end(); ++it) {
        cout << "Vertex " << it->first << ": Color " << it->second << endl;
    }

    // Validate the coloring
    cout << "Valid: " << (isValidColoring(graph, coloring) ? "Yes" : "No") << endl;

    // Number of colors used
    set<int> uniqueColors;
    for (auto it = coloring.begin(); it != coloring.end(); ++it) {
        uniqueColors.insert(it->second);
    }
    cout << "Number of colors used: " << uniqueColors.size() << endl;

    // Calculate the total execution time (in milliseconds)
    auto duration = duration_cast<milliseconds>(end_time - start_time);
    cout << "\nTotal execution time: " << duration.count() << " milliseconds" << endl;

    return 0;
}
