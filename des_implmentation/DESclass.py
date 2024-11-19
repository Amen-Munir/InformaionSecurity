from datastructures import ipTable, pc1Table, shifts, pc2Table, expansionTable, sBoxes, pBoxTable, ipInverseTable


class DES:
    def strToBin(self, chunk):
        binary = ''
        for c in chunk:
            binaryChar = format(ord(c), '08b')
            binary += binaryChar
        binary = binary[:64].ljust(64, '0')
        return binary

    def binaryToAscii(self, binaryStr):
        ascii_str = ''.join([chr(int(binaryStr[i:i+8], 2)) for i in range(0, len(binaryStr), 8)])
        return ascii_str

    def initialPermutation(self, binary):
        permutedResult = [binary[ipTable[i] - 1] for i in range(64)]
        return ''.join(permutedResult)

    def KeyConversionToBin(self):
        hexKey = 'AMENMUNI'
        binKey = ''.join(format(ord(char), '08b') for char in hexKey)
        return binKey

    def generateRoundKeys(self):
        keyInBinary = self.KeyConversionToBin()
        pc1Key = ''.join(keyInBinary[bit - 1] for bit in pc1Table)
        c0 = pc1Key[:28]
        d0 = pc1Key[28:]
        roundKeys = []
        for round_num in range(16):
            c0 = c0[shifts[round_num]:] + c0[:shifts[round_num]]
            d0 = d0[shifts[round_num]:] + d0[:shifts[round_num]]
            CD = c0 + d0
            roundKey = ''.join(CD[bit - 1] for bit in pc2Table)
            roundKeys.append(roundKey)
        return roundKeys

    def encryptionDES(self, inputChunk):
        binary = self.strToBin(inputChunk)
        round_keys = self.generateRoundKeys()
        permuted = self.initialPermutation(binary)

        leftblock = permuted[:32]
        rightBlock = permuted[32:]

        for round_num in range(16):
            expandedResult = ''.join([rightBlock[i - 1] for i in expansionTable])
            xorRes = ''.join(str(int(expandedResult[i]) ^ int(round_keys[round_num][i])) for i in range(48))

            sixBit = [xorRes[i:i+6] for i in range(0, 48, 6)]
            sBoxSubstituted = ''

            for i in range(8):
                rowNum = int(sixBit[i][0] + sixBit[i][-1], 2)
                colNum = int(sixBit[i][1:-1], 2)
                sBoxSubstituted += format(sBoxes[i][rowNum][colNum], '04b')

            p_box_result = ''.join(sBoxSubstituted[i - 1] for i in pBoxTable)
            newRight = ''.join(str(int(leftblock[i]) ^ int(p_box_result[i])) for i in range(32))

            leftblock = rightBlock
            rightBlock = newRight

        finalEncrypted = rightBlock + leftblock
        finalPermutated = ''.join(finalEncrypted[ipInverseTable[i] - 1] for i in range(64))
        encryptedRes = self.binaryToAscii(finalPermutated)

        return encryptedRes



    def decryptionDES(self,encryptedText):
    
        binary = self.strToBin(encryptedText)
        roundKeys = self.generateRoundKeys()
        # for i in roundKeys:
        #     print(i)
        
        initialPermutedString = self.initialPermutation(binary)
        
        leftBlock = initialPermutedString[:32]
        rightBlock = initialPermutedString[32:]

        for n in range(16):
            expandedblock = [rightBlock[i - 1] for i in expansionTable]
            # print(expandedblock)
        
            res= ''.join(expandedblock)

            roundKey = roundKeys[15-n]
            # print(roundKey)

            xor = ''
            for i in range(48):
                xor += str(int(res[i]) ^ int(roundKey[i]))
            # print(xor)  
            sixBits= [xor[i:i+6] for i in range(0, 48, 6)]
            sBox4bit = ''
            for i in range(8):
                rowNum = int(sixBits[i][0] + sixBits[i][-1], 2)
                colNum = int(sixBits[i][1:-1], 2)
        
                sBoxres= sBoxes[i][rowNum][colNum]
            
                sBox4bit += format(sBoxres, '04b')

            pBoxRes = [sBox4bit[i - 1] for i in pBoxTable]
            leftList= list(leftBlock)

            newRighBlock= [str(int(leftList[i]) ^ int(pBoxRes[i])) for i in range(32)]
        
    
            newRighBlockString = ''.join(newRighBlock)
        
            leftBlock = rightBlock
            rightBlock = newRighBlockString
            # print(f"left: {leftBlock}")
            # print(f"right: {rightBlock}")
    
    
        concatRes = rightBlock + leftBlock
        # print(concatRes)

        DecryptedRes = [concatRes[ipInverseTable[i] - 1] for i in range(64)]

        resString = ''.join(DecryptedRes)
        conToTEXT =self.binaryToAscii(resString)
        

        return conToTEXT

