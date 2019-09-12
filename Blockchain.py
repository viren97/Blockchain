import hashlib
import datetime

class Block:
	def __init__(self, index, data, prevHash = " "):
		self.index = index
		self.timestamp = datetime.datetime.now()
		self.prevHash = prevHash
		self.data = data
		self.hash = self.calculateHash()

	def calculateHash(self):
		h = hashlib.sha256()
		h.update(
			str(self.index).encode('utf-8')+
			str(self.timestamp).encode('utf-8')+
			str(self.prevHash).encode('utf-8')+
			str(self.data).encode('utf-8')
			)
		return h.hexdigest()

	def __str__(self):
		return "\nBlock No.: "+str(self.index)+"\nBlock Hash: "+str(self.hash)+"\nBlock prevHash: "+str(self.prevHash)+"\n Block Data: "+str(self.data)

 
class Blockchain:
	def __init__(self):
		self.chain = []
		self.chain.append(self.createGenesisBlock())

	def createGenesisBlock(self):
		return Block(0,'Genesis Block', '0')

	def getLatestBlock(self):
		return self.chain[len(self.chain)-1].hash

	def addBlock(self, newBlock):
		newBlock.prevHash = self.getLatestBlock()
		newBlock.hash = newBlock.calculateHash()
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
v.addBlock(Block(1, {'amount':56}))
v.addBlock(Block(2, '86'))

print("is Blockchain valid? ", v.isChainValid())

v.chain[1].data = '8799'
v.chain[1].hash = v.chain[1].calculateHash()
#reverse back all commit to its previous version if there is something wrong!

print("is Blockchain valid? ", v.isChainValid())





