#Created by: Ricardo Garcia

class Encript:
    def __init__(self, message):
        self.message = message
    
    def encrypt(self):
        '''
        Input:
        ------
        this method don't receive a input 

        Output:
        --------
        Return the encrypted message 
        '''

        #Take each element of the message, and turned into its ASCII values    
        my_array = [ord(char) for char in self.message]

        #Now, for each element, form pairs, considering the border cases 

        pairs = []
        for i in range(0,len(my_array)-1, 2):
            pairs.append([my_array[i], my_array[i+1]])

        #Border case: Array length is not pair 
     
        if len(my_array) % 2 != 0:
            length = len(my_array) - 1
            pairs.append([my_array[length]])

        #for each pair in pairs, I'm gonna take the actual element and plus the position of the following pair 
        
        for i in range(len(pairs)-1):
            pairs[i][0] += i+1
            pairs[i][1] += i
        
        if len(self.message) % 2 != 0:
            pairs[len(pairs)-1][0] += len(my_array) - 2  

        #Now, we encrypt the elements in each pair

        for i in range(len(pairs)):
            pairs[i][0] = chr(pairs[i][0])
            pairs[i][1] = chr(pairs[i][1])
        
        if len(self.message) % 2 != 0: 
            pairs[-1][0] = chr(pairs[-1][0])
        #now, concatenate the array to form the final array
        final_array = []
        for i in range(len(pairs)):
            final_array.extend(pairs[i])
        
        encrypt = ''.join(final_array)
        return encrypt
    
    def decrypt(self):
        pass 
    def print(self):
        print('the encrypted array is: ', self.encrypt())
    
encrypt = Encript('Gato E')
cat = encrypt.encrypt()
encrypt.print()