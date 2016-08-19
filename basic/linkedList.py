#Used to create a linked list, only can add Note, delete Note, and print all Note.
class Note(object):
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data
	def setData(self, data):
		self.data = data
	def getNext(self):
		return self.next
	def setNext(self, next):
		self.next = next

class CircleLinkedList(object):
	def __init__(self):
		self.head = Note(None)
		self.head.setNext(self.head)
	def getHead(self):
		return self.head
	def addNote(self, data):
		tmp = Note(data)
		tmp.setNext(self.head.getNext())
		self.head.setNext(tmp)
	def deleteNote(self):
		temp = self.head
		if temp.next == self.head:
			print "This linked list is a none list."
			return
		while temp.next.next != self.head:
			temp = temp.next
		print "Delete the last note, %s"%(temp.data)
		temp.next = self.head
	def printLinkedList(self):
		temp = self.head
		while temp.next != self.head:
			print temp.getData()
			temp = temp.getNext()
		print temp.getData()
		
	def __eq__(self, other):
		if self.data == other.data:
			return True
		else:
			return False
	

def main():
	link = CircleLinkedList() 
	link.addNote("I love you")
	link.addNote("cc")
	print "print linked list:"
	link.printLinkedList()

"""
	cc = link.getHead()
	while cc.next != link.head:
		print cc.getData()
		cc = cc.getNext()
	print cc.getData()

	link.deleteNote()
	cc = link.getHead()
	while cc.next != link.head:
		print cc.getData()
		cc = cc.getNext()
"""
if __name__ == "__main__":
	main()
