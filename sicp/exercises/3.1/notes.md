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
