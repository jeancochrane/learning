# Chapter 3.1: Assignment and Local State

- "State" = has a history that influences behavior 
    - **state variables** record that history cumulatively
        - e.g.: Current balance in a bank account encodes transaction history

- Objects in a stateful system are rarely independent
    - Hence, the goal is to produce "closely-coupled subsystems loosely coupled
      to one another"

- Critical operation for state: **assignment**

## 3.1.1: Local State Variables

- Stateful procedures are the first kind of procedures we've seen that can
  return different outputs for the same inputs

- `set!` is Scheme's assignment operator

- Local state is accessible only to the method (object?) to which it pertains
    - "Encapsulation", or "the hiding principle": modular systems protect as
      much as much as possible from the other parts of the system

- Assignment means that the substitution model no longer holds (?)
    - i.e., if variables can change, we can't simply substitute the formal
      parameters into the method and evaluate (something like that?)
        - Anyway, more on this in a later section 

## 3.1.2: The Benefits of Introducing Assignment

- Example: random number generators with and without assignment
    - Without assignment: caller must keep track of the seed and its successive
      values
    - With assignment: seed can be encapsulated in the random-generating method

- Example application: Monte Carlo simulation of pi
    - Monte carlo refresher: Estimate the value of a constant by drawing
      experiments at random and using associated probabilities that include that
      constant
        - e.g. two integers chosen at random will have no factors in common with
          a probability of 6/pi^2 -- hence we can draw random integers and
          compute their greatest common divisor many times over, using the
          fraction of successes to estimate pi

    - Without state assignment, the procedure that runs the trials must
      continually compute and keep track of the random seeds
        - Not only is this more verbose and harder to read, but it tightly
          couples two components of the system that aren't interdependent on one
          another

- In spite of these points, stateful procedures are not universally more modular
  than stateless procedures! We'll see some examples in the next section
