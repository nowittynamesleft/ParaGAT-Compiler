class ExpressionTree:

    root = Node()
    currentNode = root
    st = Stack()
    
    def __init__(self, x[]): #string array input is given, with each token in each index
        for (i in x)
        {
            self.st.push(Node(i))
        }
        processStack(root)
            
    def add(parent, newNode):
        parent.addChild(newNode)

    def addOperator(parent, operator):
        add(parent, newNode)

    def addOperand(parent, operand):
        add(parent, operand)

    def processStack(current):
    {
        if(!st.isEmpty())
        {
            if(st.peek().isAnOperator())
            {
                temp = st.peek()
                addOperator(currentNode, st.pop())
                currentNode = temp
            }
            else #it's an operand
            {
                if(currentNode.operandCount < 2)
                {
                    addOperand(currentNode, st.pop())
                    currentNode.operandCount++
                }
                else #parent has two operands already
                {
                    currentNode = currentNode.parent
                    processStack(currentNode) #continue processing stack in the parent node
                }
            }
        }
    }