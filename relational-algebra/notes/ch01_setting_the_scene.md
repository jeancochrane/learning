# Notes on Chapter 1, "Setting the Scene"

## Introducing the relational model

- Important conceptual distinction between "SQL" and "the relational model"
    - Relational model:
        - Theoretical system
        - Set of principles
        - Abstraction
    - SQL:
        - Inspired by the relational model
        - Relational-like
        - Implementation
    - SQL often sacrifices pure relationality for efficiency, in ways we'll
    look at soon

- The **relational model** (as originally defined)
    - Introduced by E. F. Codd in a paper for IBM in 1969
    - Inspired by the idea of bringing mathematical rigor to database design,
    particularly insights from set theory
    - Since 1969, has grown and developed like any branch of math

- Three primary components to the relational model:
    1. Structure
        - **Relations** are defined over **domains** (types)
        - Relations have **arity** (or degree), a certain number of attributes
            - We refer to them as n-ary relations
        - Relations are made up of **attributes** (what we often refer to as
          columns) and **tuples** (rows)
            - Not really a 1:1 correspondance
            - **Attributes**: name/type pairs that define the structure of
              a relation
            - **Tuple**: set of values of the same arity as the table, matching
              the types specified by the attributes
        - Relations have **keys**: sets of attributes that identify unique tuples
          within the relation
            - Any set of attributes that can uniquely identify a tuple in
              a relation is a **candidate key**
            - We often refer to special candidate keys as **primary keys**
                - Not really clear yet if there's a more rigorous definition
                - Speaking relationally, there's no real distinction between
                  primary/candidate keys
            - **Foreign kets** are sets of attributes corresponding to a key
              that must exist in another relation
    2. Integrity
        - **Integrity constraints** are boolean conditionals that must evaluate
          to `TRUE`
            - Expressed in terms of relations in the context of a particular
              database
        - Two **generic constraints** hold for all databases, according to the
          relational model:
            1. **Entity integrity**: no primary keys contain null values
                - This defines an "entity" within a relation
            2. **Referential integrity**: no unmatched foreign keys
                - This defines "reference" within a DB context, and makes
                  foreign keys usable
    3. Manipulation
        - Two fundamental means of manipulating relations:
            1. **Relational algebra**
                - Essential operators that can be applied to relations to alter them
            2. **Relational assignment operator**
                - A special operator that assigns the output of relational
                  expressions to a relation
                    - We refer to this process as an "update" in SQL
                    - Adheres to the "closure property": algebraic operations
                      on relations produce other relations
                        - This, in turn, allows for nested algebraic
                          expressions

## Relational algebra

- The fundamental operations of E. F. Codd's original relational algebra:
    1. Restrict
        - Return tuples from a relation that satisfy a given condition
    2. Project
        - Remove attributes from a relation and return the resulting subtuples
    3. Product
        - AKA "Cartesian product"
        - Return all combinations of two tuples
        - A special type of `JOIN`, as we'll see later
    4. Intersect
        - Return all tuples shared between two relations
        - Also a special `JOIN`
    5. Union
        - Return all tuples that appear in either or both of two relations
    6. Difference
        - Return all tuples in one but not the other of two relations
    7. Natural join
        - Return a relation with all possible tuples that are a combination of
          two tuples and share common values for specified attributes
        - When we refer to "joins," we typically mean natural joins

- Brief aside on physical data independence
    - Adjusting an implementation of a data model should be separate from
      adjusting the interface
    - In essence, we want to separate the logic by which a user accesses data
      from the physical means by which it is stored on disk
        - The relational model is designed to allow this: Codd didn't specify
          how relational algebra should be implemented, only how it should
          operate theoretically
    - Three important levels of independence:
        - View (GUI)
        - Logic (schema)
        - Physical (storage)

## Properties of relations

- Relations contain a **heading** and a **body**
    - Headings contain attributes (unique name/type pairs)
    - Bodies contain tuples (that must conform to the number and types of
      attributes in the heading)
    - The number of attributes in a relation is referred to as its **arity**
    - The number of tuples in a relation is referred to as its **cardinality**

- Relations cannot contain duplicate tuples
    - Bodies are defined strictly as mathematical sets, and sets cannot contain
      duplicates by definition
        - By a similar coin, relations cannot contain duplicate attributes
          (headings are also sets)
    - One way in which the relational model and SQL differ!

- Tuples and attributes are unordered 
    - Also an inherited property of sets
    - Hence, `ORDER BY` is a query-language convention and not a relational
      operator

- Relations are normalized (first normal form)
    - Each tuple contains one value of the right type for its corresponding
      attribute

- Two tuples are equal iff:
    1. They have values for the same attributes
    2. Corresponding values are equal

- Base relations + operators = derived relations
    - **Views** are a special type of derived relation in SQL and other query
      languages
        - AKA virtual relations
    - In the relational model, there's no distinction between a view and
      a relation

## Relations vs. relvars

- Relation variables (relvars) reference relations
    - In SQL, we might think of relvar as table names, while relations are
      actual sets of data that we pull out of the database
    - In SQL, much of the variable assignment in the relational model is
      obscured, but it's still there

Compare a delete statement:

```sql
DELETE S WHERE CITY = 'Athens';
```

To a purely-relational equivalent (Tutorial D):

```
S := S MINUS ( S WHERE CITY = 'Athens' );
```

- Relvars and relations are a general case of the variable/value distinction
    - **Values** are individual constants (e.g. 3 or "Athens")
        - No location in time and space
            - Kind of odd to think about... I would have thought that values
              would have a place in time/space, and variables wouldn't (because
              they don't refer to a specific "thing"). But values are in fact
              the dislocated element of a reference relationship!
        - Represented by an encoding in memory (e.g. ASCII value at a specific
          memory address)
            - This encoding does have a location
        - Cannot change
    - **Variables** are containers for representation of values
        - As Agre points out, it's not always so simple... variables mean different
          things in different times and different abstraction systems!
            - e.g. The "x" in 3x - 4 = 5 has a different semantic meaning from
              the "x" in f(x) = 3x - 4
                - One is a constant that exists but has not been fixed, while
                  the other represents a set of mappings
        - Has location in time/space (memory address in a stack)
        - Can be updated


