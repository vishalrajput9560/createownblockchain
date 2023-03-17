#Python code to build our own blockchain
import hashlib

def hashGenerator(data):
  result=hashlib.sha256(data.encode())
  return result.hexdigest()

class Block:
  def __init__(self,data,hash,prev_hash):
    self.data=data
    self.hash=hash
    self.prev_hash=prev_hash


class BlockChain:
  def __init__(self):
    hashLast=hashGenerator('0')
    hashStart=hashGenerator('First Block')

    genesis=Block('gendata',hashStart,hashLast)

    self.chain=[genesis]

  def add_Block(self,data):
    prev_hash=self.chain[-1].hash
    hash=hashGenerator(data)
    block=Block(data,hash,prev_hash)
    self.chain.append(block)


bc=BlockChain()
bc.add_Block('1')
bc.add_Block('2')
bc.add_Block('3')


for block in bc.chain:
  print(block.__dict__)
