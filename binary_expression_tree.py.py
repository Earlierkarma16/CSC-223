 
import operator
from stack import Stack

# Define a simple TreeNode class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryExpressionTree:
    def __init__(self):
        self.root = None
        self._operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    def build_from_postfix(self, postfix_expr):
        """
        Builds the binary expression tree from a postfix expression string.
        Implements the detailed algorithm provided in the prompt.
        """
        stack = Stack()
        tokens = postfix_expr.split()

        for token in tokens:
            if self._is_number(token):
                # If number: Create node, push onto stack
                new_node = TreeNode(token)
                stack.push(new_node)
            elif token in self._operators:
                # If operator: Create node
                new_node = TreeNode(token)
                
                # Get right and left operands from stack
                if stack.is_empty():
                    raise ValueError(f"Error: Not enough operands for operator {token}")
                new_node.right = stack.pop()
                
                if stack.is_empty():
                    raise ValueError(f"Error: Not enough operands for operator {token}")
                new_node.left = stack.pop()
                
                # Push the new subtree root back onto the stack
                stack.push(new_node)
            else:
                raise ValueError(f"Error: Unsupported token '{token}'")

        if stack.size() != 1:
            raise ValueError("Error: Invalid postfix expression (unused tokens or missing operator)")
        
        # Store the final tree root
        self.root = stack.pop()

    def evaluate(self):
        """Public method to start the recursive evaluation."""
        if not self.root:
            return None
        return self._evaluate_tree_helper(self.root)

    def _evaluate_tree_helper(self, p):
        """
        Recursive helper function to evaluate the tree (Algorithm provided).
        """
        if p.left is None and p.right is None:
            # If p is a leaf, return the value (converted to float)
            return float(p.value)
        else:
            # Op is the value field of p
            op_func = self._operators[p.value]
            x = self._evaluate_tree_helper(p.left)
            y = self._evaluate_tree_helper(p.right)
            # Evaluate the expression x op y
            return op_func(x, y)

    def inorder_traversal(self):
        """Public method to start the recursive inorder traversal (infix form)."""
        result = []
        self._inorder_helper(self.root, result)
        return "".join(result).strip()

    def _inorder_helper(self, p, result):
        """Recursive helper for inorder traversal with parentheses."""
        if p:
            # Add parenthesis for operators to maintain order of operations in infix form
            if p.value in self._operators:
                result.append("(")
            
            self._inorder_helper(p.left, result)
            result.append(f"{p.value} ")
            self._inorder_helper(p.right, result)
            
            if p.value in self._operators:
                result.append(")")

    def postorder_traversal(self):
        """Public method to start the recursive postorder traversal (postfix form)."""
        result = []
        self._postorder_helper(self.root, result)
        return " ".join(result).strip()

    def _postorder_helper(self, p, result):
        """Recursive helper for postorder traversal."""
        if p:
            self._postorder_helper(p.left, result)
            self._postorder_helper(p.right, result)
            result.append(p.value)

    def _is_number(self, s):
        """Checks if a string is a valid number (integer or float)."""
        try:
            float(s)
            return True
        except ValueError:
            return False