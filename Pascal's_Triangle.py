class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Time Complexity: O(h*m) | Space Complexity: O(n)
        # where, h is height of tree and m is number of nodes 2^h
        output_arr = [[1],[1,1]]

        j = 2
        while j < numRows:
            sub_arr = [0] * (len(output_arr[j-1])+1)
            #print(sub_arr)
            add_arr = output_arr[j-1]
            #print(add_arr)

            sub_arr[0] = 1
            sub_arr[len(sub_arr)-1] = 1

            for i in range(1, len(sub_arr)-1):
                sub_arr[i] = add_arr[i]+add_arr[i-1]
            
            output_arr.append(sub_arr)
            j += 1

        return output_arr[:numRows]
