# Chapter 2: Types and Domains

#### Intro

- Relations are defined over types; hence, we need a type theory!

- Types can be arbitrarily complex

- The relational model specifically requires only one type, `BOOLEAN` (used for
  comparison)... that's pretty wild!

#### Domains are types

- This section is mostly a long-winded argument on Date's part about why we
  should feel comfortable treating types and domains as equivalent sets of
  things. I didn't really disagree at the start, so I think I may be the wrong
  audience... It's pretty pedantic, but here are some useful parts anyway.

- Codd initially proposed _Domain Check Override_ (DCO) as a way of allowing
  comparisons between attributes in different domains
    - Basic idea: check that the "basic data types" are the same (e.g. that
      both attributes inherit from the `Integer` type), and then proceed
    - Date thinks that DCO confuses _types_ with their _representations_ 

- Date suggests an improvement to DCO: define _reversing functions_ that
    convert types (like `SNO`) to their representations (like `String`) to more
    rigorously allow for comparison between different types

#### Data value atomicity

- (Different from the A in ACID that also stands for atomicity! Why does every
  database term mean at least three very different things...?)

- Formal definition of first normal form: every tuple in every relation
  contains just one _atomic_ value of the right type in every attribute
  position

- Codd left "atomic" as an ambiguous property, saying that it meant the DBMS
  cannot decompose it into smaller pieces
    - Date's analogy: it's precisely like the atom in physics, which is
      sometimes the smallest possible unit of measurement (like in atomic
      theory) and other types not (like when considering quarks and neutrinos)
    - Because of the fuzziness of this property, it's best thought of as
      a principle to follow ("each attribute value should only encode one
      thing, however you define 'thing'") than a strict constraint of the
      relational model

#### What's a type?

- "Named, finite set of values"
    - Named: like PNO/SNO, can refer to it uniquely
    - Finite: we're dealing with digital computers, after all! (In theory,
      there's no reason a type has to be finite. This maybe even applies to
      computers too? Apparently [the Integer type
      in Haskell is infinite...](https://bartoszmilewski.com/2014/11/24/types-and-functions/))

- Important properties of types
    - Setting aside type inheritance for a minute (which makes things murkier),
      in principal every value has exactly one type
        - Hence, types are theoretically disjoint sets
    - Certain properties that must be defined in order to constitute a type:
        - Variables
        - Attributes
        - Operators
            - Every type must have at least assignment (`:=`) and equality (`=`)
            - Operators that aren't defined for a type are "unsupported"
                - There's an intriguing recursiveness here where types are
                  defined for operators, and operators are defined for types...
        - Operator parameters

- Steps to define a type:
    - Name
    - Set of values
    - Physical representation
        - On disk? Or for the user? Could go either way (representation means
          so many things)
            - Given Date's annoyance over mistaking types and representations,
              I think this is more like "The symbols that you will use to
              denote the type"
    - A selector operator
        - Basically a syntax for literals
            - All literals are selector invocations, but not all selector
            invocations are literals! Selector invocations can refer to
            abstractions or variables
                - e.g. POINT(X, Y) is a selector invocation, but not a literal
                - POINT(1, 2) is both
    - Operators that apply to variables and values of the type
    - Types of results that operators return

#### Scalar vs. nonscalar types

- Scalar types: no "user-visible components"
    - e.g. integers, floating-point numbers
        - I don't really understand, both of these examples do have user-visible
        components...?

- Nonscalar types: exposed to the user
    - See above, I'm still confused about how this is a coherent distinction
    - Date's example: POINT()

- In the context of this book:
    - Tuple/relation types will be considered "nonscalar types"
    - All other types will be considered "scalar"
    - According to Date, relvars are the only kind of variable allowed in
      a relational databae (!)

#### Type checking

- SQL supports a "weak form of strong typing"
    - Within certain wider type sets (e.g. "numeric" or "character") types can
      be coerced for comparison
        - Like Python!
    - There's also some more complex coercion from nonscalar to scalar types
      during subquery evaluation, but we'll get to that later

#### Row and table types in SQL

- "Row" type in SQL is not exactly a tuple type
    - e.g. rows have order; tuples do not

- No real "table" type in SQL (!)
    - Date argues that `CREATE TABLE` is not a type generator
        - Syntactically, constraints can go in many places
            - True, but seems to adhere to an unecessarily strict definition of
              "type" (particularly, one that is concerned with implementation
              details)
        - Tables are collections of rows
            - But they're more than that, too, aren't they? As in, a table in
              SQL can have no rows in it -- what is that?

#### Final thoughts
 
- Since a relation can have attributes of any type, no matter how complex, they
  are in first normal form by definition

- Two important exceptions to the claim that "arbitrarily complex" types are
  allowed in a relation:
    - If a relation is of type T, none of its attributes can be of type T
        - Endless recursion alert!
    - No pointer types allowed
        - Pre-relational databases were often dependent on pointers in a way
          that proved to be a huge headache for consistency and memory
          management (? Date doesn't say this, I'm just extrapolating) and
          finding a way out of the constraints of that situation was really
          important to Codd
            - I still don't fully get how the relational model elides the
              difficulties with pointers and consistencies in a database, so
              I hope Date covers that

