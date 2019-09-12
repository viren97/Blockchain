import hashlib
import datetime

class Block:
	def __init__(self, index, data, prevHash = " "):
		self.index = index
		self.timestamp = datetime.datetime.now()
		self.prevHash = prevHash
		self.data = data
		self.nonce = 0
		self.hash = self.calculateHash()
		

	def calculateHash(self):
		h = hashlib.sha256()
		h.update(
			str(self.index).encode('utf-8')+
			str(self.timestamp).encode('utf-8')+
			str(self.prevHash).encode('utf-8')+
			str(self.data).encode('utf-8')+
			str(self.nonce).encode('utf-8')
			)
		return h.hexdigest()

	def mineBlock(self, difficulty):
		s = '0'
		while(self.hash[0:difficulty] != s*difficulty):
			self.nonce+=1 
			self.hash = self.calculateHash()

		print("Block mines: ", self.hash)



	def __str__(self):
		return "\nBlock No.: "+str(self.index)+"\nBlock Hash: "+str(self.hash)+"\nBlock prevHash: "+str(self.prevHash)+"\n Block Data: "+str(self.data)

 
class Blockchain:
	def __init__(self):
		self.chain = []
		self.chain.append(self.createGenesisBlock())
		self.difficulty = 5

	def createGenesisBlock(self):
		return Block(0,'Genesis Block', '0')

	def getLatestBlock(self):
		return self.chain[len(self.chain)-1].hash

	def addBlock(self, newBlock):
		newBlock.prevHash = self.getLatestBlock()
		newBlock.mineBlock(self.difficulty)
		self.chain.append(newBlock)

	def isChainValid(self):
		for i in range(1,len(self.chain)):
			curBlock = self.chain[i]
			prevBlock = self.chain[i-1]

			if(curBlock.hash != curBlock.calculateHash()):
				return False

			if(curBlock.prevHash != prevBlock.hash):
				return False
		return True



v = Blockchain()
print('mining block 1...........')
v.addBlock(Block(1, {'amount':56}))
print('mining block 2...........')
v.addBlock(Block(2, '86'))




