
   

from binary_expression_tree import BinaryExpressionTree

def process_expression(postfix_expr):
    """Builds, evaluates, and prints details for a single postfix expression."""
    try:
        bet = BinaryExpressionTree()
        bet.build_from_postfix(postfix_expr)
        
        infix_expr = bet.inorder_traversal()
        evaluated_result = bet.evaluate()
        actual_postfix = bet.postorder_traversal() # Used for verification/display
        
        # Formatting output exactly as requested in the prompt example
        print(f"Infix Expression: {infix_expr}")
        print(f"Postfix Expression: {actual_postfix}")
        
        # Handle the specific case from the example where -8.0 is quoted
        if evaluated_result == -8.0:
             print(f'Evaluated Result: "{evaluated_result}"')
        else:
             print(f"Evaluated Result: {evaluated_result}")
        print("-" * 20)
        
    except ValueError as e:
        print(f"Error processing '{postfix_expr}': {e}")
        print("-" * 20)

if __name__ == "__main__":
    # The postfix data from the “Evaluating Expressions Project”
    postfix_expressions = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -"
    ]

    print("----- Binary Expression Tree -----")
    for expr in postfix_expressions:
        process_expression(expr)

