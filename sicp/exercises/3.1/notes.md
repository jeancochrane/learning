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

## 3.1.3: The Costs of Introducing Assignment

- With assignment, the substitution model of procedure application no longer
  holds
    - i.e. without assignment, two evaluations of a procedure will always
      produce the same result; with assignment, this is no longer strictly true
        - No assignment = _functional programming_

- Core of the problem: substitution assumes that symbols are _names of values_
    - Assignment, however, assumes that symbols are _places where a value is
      stored_
        - The first kind of symbol is immutable; the second can change! We have
          to go and retrieve it whenever we want to know what its value is, we
          can't simply substitute

### Sameness and change

- Introducing the capacity for change makes "sameness" hard to define
    - e.g. two instances of the same (purely functional) procedure are "the same", but two instances of a class are not
        - i.e. sameness can no longer mean "can be substituted for each other"
    - This isn't the only definition of "sameness", it's just the simplest to
      define; sameness that includes assignment is tricky

- **Referentially transparent**: quality of a language where "equals can be
  substituted for equals"
    - `set!` violates this principle; makes it difficult to know when
      expressions can be simplified

- Deep insight: in the real world, "sameness" and "change" depend on each other for semantic
  coherence
    - i.e.: only way to tell if two objects are "the same" is to _change_ one
      and watch if the other changes too; however, only way to tell if an object
      has "changed" is to look at the _same_ object before and after
      intervention

- In programming, the intertwining of sameness and change comes up in
  **aliasing**: the phenomenon of a single computation object having mutliple
  names
    - Aliasing makes analyzing code and finding bugs substantially more
      difficult
    - Basically: sharing state is hard

- In sum: introducing assignment means introducing _change_, which alters our
  definition of "sameness" such that it no longer means "two things that can be
  functionally interchanged with one another" -- instead, it's more slippery,
  and has to handle the fact that an object with state is "the same" over time,
  even though its outputs change

### Pitfalls of imperative programming

- Programming with assignment is known as _imperative programming_

- Imperative programming introduces a unique set of bugs
    - Example: order of assignment can change the output
        - With assignment, the programmer has to be careful that the correct
          version of a variable is referenced at all times
