import sys
import os
import hashlib
import json
from datetime import datetime
idCount=0
#command line arguments manuplations
'''fileName="python "
fileName+=sys.argv[1]
os.system(fileName)'''
class blockChain:
    records = []
    index=[]

    def addBlocks(self,preBlockHash,data):             #function to add data to a block and to hash them
        self.preBlockHash=preBlockHash
        self.blockData=preBlockHash
        self.blockData+="-"
        self.blockData+=data
        self.blockHash=hashlib.sha256(self.blockData.encode()).hexdigest()
        now=datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")        #to convert date and time to conventioal format
        self.index.append([self.blockHash,dt])
    def obtainRecords(self,details):                  #called when data is passed as individual parameters
                                                       #  #when individual parameters are obtaine as cli
        global idCount
        idCount+=1
        kycData={}
        kycData["customerId"]=idCount
        kycData["customerName"]={}
        kycData["customerName"]["firstName"]=details[0]
        kycData["customerName"]["lastName"]=details[1]
        kycData["customerAge"]=details[2]
        kycData["customerEmail"]=details[3]
        kycData["customerAddress"]={}
        kycData["customerAddress"]["permanentAddress"]=details[4]
        kycData["customerAddress"]["currentAdress"]=details[5]
        kycData["customerGender"]=details[6]
        kycData["customerPhNo"]=details[7]
        kycData["customerVerificationId"]={}

        kycData["customerVerificationId"]["aadhar"]=details[8]
        kycData["customerVerificationId"]["pan"]=details[9]
        kycData["customerVerificationId"]["passport"]=details[10]
        kycData["customerVerificationId"]["VoterId"]=details[11]
        self.records.append(kycData)          #to append all the  user data into a json object formal

    def userData(self):                         #function to display the user records
        for i in self.records:
            print(i)
    def displayBlocks(self):                     #function to display the hadvalues of the blocks
        print(" Number of Bocks present in the chain ",len(self.index))
        print("HashValue and timestamp of Blocks in the chain are as follows ")
        for i in self.index:
            print(i)
    def getPreBlockHash(self):              #function to return the hash value of the previous block
        return self.index[-1][0]


block = blockChain()
noOfRecords=len(sys.argv)     #to obtain the number of user ecords passed as arguments
userDetails = sys.argv[1] .replace("\'", "\"")
block.addBlocks("genesis Block", userDetails) #to add the genesis block to initiate the chains

for i in range(2,noOfRecords):     #to iterate through the rest  user data
    userDetails = sys.argv[i].replace("\'", "\"")
    block.addBlocks(block.getPreBlockHash(), userDetails)     #to add the block one after the other after the genesis block
block.displayBlocks()      #to display the hachvalues, number of blocks and time stamps of each blocks








