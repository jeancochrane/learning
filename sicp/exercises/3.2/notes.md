# Chapter 3.2: The Environment Model of Evaluation

- Substitution model recap:
    - "To apply a compound procedure to arguments, evaluate the body of the
       procedure with each formal parameter replaced by the corresponding
       argument."
        - i.e. Expand out functions as far as they'll go, then evaluate

- Substitution no longer holds under assigment, since variables are not names
  of values, but names of _places_
    - Places are maintained in **environments**

- Environment: sequence of **frames**
    - Frames consist of:
        - Table of **bindings**, associating names -> values
            - Only one binding per variable, per frame
        - Pointer to **enclosing environment**
            - Exception: **global** frames
    - Algorithm to determine the value of a variable in an environment:
        1. Check the binding for the variable in the first (latest child) frame
        2. If no binding is found, check subsequent parent frames
        3. Continue checking frames until reaching the outermost frame in the
           sequence; if no binding exists, the variable is considered
           **unbound**
    - Values of a variable that are reassigned in a later frame **shadow** the
      binding of earlier frames

- Expressions take their meaning from the environment
    - Even basic language constructs like `+` rely on an environment (the
      runtime?) to have meaning
        - "The symbol `+` is bound in the global environment to the primitive
          addition procedure"

## 3.2.1 The Rules for Evaluation

- The environment model has the same basic definition of evaluating a combination:
    1. Evaluate the subexpressions of the combination
        - Due to assignment, however, this needs to have a specified order
          (left-to-right)
    2. Apply the value of the operator subexpression to the values of the
       operand subexpressions

- Now, however, "apply a compound procedure to arguments" takes on a different
  meaning
    - Two parts to the definition:
        1. How to create procedures
        2. How to apply procedures

- Creating procedures:
    - Procedures = a pair of 1) some code and 2) a pointer to an environment
        - Procedures are always lambda expressions; `(define (f x) (...))` is
          just syntactic sugar around `(define f (lambda (x) (...)))`
        - `define` creates procedures by adding bindings to frames (!)

    - `(lambda (x) (* x x))`:
        - Definition for evaluation purposes: Procedure with one formal parameter (`x`) and a procedure body `(* x x)`, pointer t othe global environment
        - In `(define square (lambda (x) (* x x)))`, `define` binds this procedure
        definition to the symbol `square` in the global frame

- Applying procedures:
    1. Create a new environment, enclosed by the environment that is bound to
       the procedure, with a frame that binds the parameters to the
       values of the arguments
    2. In the new environment, evaluate the procedure body 

- Additional behaviors:
    - `define` creates a binding in the current environment frame
    - `set!` locate the binding of a variable in the environment and changes
      that binding to a new value
        - First frame takes precedence; if the variable is unbound, `set!`
          signals an error
