class chi_squared:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M', \
                         'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.letter_probs = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966, \
                             0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987, \
                             0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

    def stat(self,cipher):
        
        cipher_len = len(cipher);

        # Calculate expected quantity of each letter

        exp_letter_freqs = [i * cipher_len for i in self.letter_probs] 

        chi = 0

        for i in range(0,26):
            chi = chi + ((cipher.count(self.alphabet[i]) - exp_letter_freqs[i])**2)/exp_letter_freqs[i]

        return chi

