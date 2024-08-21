
//https://www.geeksforgeeks.org/how-to-create-vector-of-pairs-in-cpp/
// C++ program to create the Vector of Pairs   vector(pair<int><int>>
#include <iostream> 
#include <utility> 
#include <vector> 
using namespace std; 

// Driver Code 
int main() 
{ 
	// Declare a vector of pairs, where each pair 
	// contains an integer and a character 
	vector<pair<int, char> > vecOfPairs; 

	// creating pairs 
	pair<int, char> p1, p2; 
	p1 = make_pair(1, 'A'); 
	p2 = make_pair(2, 'B'); 

	// inserting pairs to the vector 
	vecOfPairs.push_back(p1); 
	vecOfPairs.push_back(p2); 

	// Iterate over the vector of pairs 
	// using a range-based for loop 
	for (const auto& pair : vecOfPairs) { 

		std::cout << "(" << pair.first << ", "
				<< pair.second << ")" << std::endl; 
	} 

	return 0; 
}


//By using auto&, you create a reference to each element instead of a copy. This is more efficient because no copying occurs; you're directly accessing the original elements in the collection.