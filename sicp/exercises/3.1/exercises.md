# Exercises for Chapter 3.1: Assignment and Local State

## 3.1.1: Local State Variables

**Exercise 3.1**

An *accumulator* is a procedure that is called repeatedly with a single numeric
argument and accumulates its arguments into a sum. Each time it is called, it
returns the currently accumulated sum. Write a procedure `make-accumulator` that
generates accumulators, each maintaining an independent sum. The input to
`make-accumulator` should specify the initial value of the sum; for example

```scheme
(define A (make-accumulator 5))
(A 10)
15
(A 10)
25
```

**Answer 3.1**

```scheme
(define (make-accumulator init)
  (lambda (x)
    (set! init (+ init x))
    init))
```

**Exercise 3.2**

In software-testing applications, it is useful to be able to count the number of
times a given procedure is called during the course of a computation. Write
a procedure `make-monitored` that takes as input a procedure, `f`, that itself takes
one input. The result returned by `make-monitored` is a third procedure, say `mf`,
that keeps track of the number of times it has been called by maintaining an
internal counter. If the input to `mf` is the special symbol `how-many-calls?`, then
`mf` returns the value of the counter. If the input is the special symbol
`reset-count`, then `mf` resets the counter to zero. For any other input, `mf` returns
the result of calling `f` on that input and increments the counter. For instance,
we could make a monitored version of the `sqrt` procedure:

```scheme
(define s (make-monitored sqrt))

(s 100)
10

(s 'how-many-calls?)
1
```

**Answer 3.2**

```scheme
(define (make-monitored f)
  ;;;
  ;;; Monitor the procedure `f`, allowing the user to inspect
  ;;; the number of times that it is called in a given procedure.
  ;;;
  (define counter 0)
  (define (mf arg)
    (cond ((eq? arg 'how-many-calls?)
            counter)
          ((eq? arg 'reset-count)
            (set! counter 0)
            (counter))
          (else
            (set! counter (+ counter 1))
            (f arg))))
    mf)
```

**Exercise 3.5**

Implement Monte Carlo integration as a procedure `estimate-integral` that takes as
arguments a predicate `P`, upper and lower bounds `x1`, `x2`, `y1`, and `y2` for the
rectangle, and the number of trials to perform in order to produce the estimate.
Your procedure should use the same `monte-carlo` procedure that was used above to
estimate `pi`. Use your `estimate-integral` to produce an estimate of `pi` by measuring the
area of a unit circle.

**Answer 3.5**

```scheme
(define (estimate-integral P x1 x2 y1 y2)
  ;;;
  ;;; Estimate an integral using Monte Carlo simulations.
  ;;;
  ;;; Arguments:
  ;;;   - P: Predicate P(x,y) -- procedure to determine if the coordinates of a
  ;;;        trial result are within the bounds of the function to integrate
  ;;;   - x1, x2, y1, y2: Bounds of a rectangle that contains the region in question
  ;;;
  (define (experiment)
    (let ((x (random-in-range x1 x2))
          (y (random-in-range y1 y2)))
      (P x y)))
  (monte-carlo 10000 experiment))


(define (estimate-pi)
  ;;;
  ;;; Estimate pi by using the `estimate-integral` procedure to run a
  ;;; Monte Carlo simulation on the unit circle.
  ;;;
  (define (P x y)
   (let ((r (square (+ (square x)
                       (square y)))))
     (>= 1 r)))
  (define x1 -1.0)
  (define x2 1.0)
  (define y1 -1.0)
  (define y2 1.0)
  (let ((area-of-square (* (+ (abs x1) (abs x2)) (+ (abs y1) (abs y2)))))
    (* area-of-square (estimate-integral P x1 x2 y1 y2))))
```

**Exercise 3.6**

It is useful to be able to reset a random-number generator to produce a sequence
starting from a given value. Design a new `rand` procedure that is called with an
argument that is either the symbol `generate` or the symbol `reset` and behaves as
follows: `(rand 'generate)` produces a new random number; `((rand 'reset)
<new-value>)` resets the internal state variable to the designated `<new-value>`.
Thus, by resetting the state, one can generate repeatable sequences. These are
very handy to have when testing and debugging programs that use random numbers.
