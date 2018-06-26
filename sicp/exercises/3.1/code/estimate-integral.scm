(define (monte-carlo trials experiment)
  ;;;
  ;;; Run a Monte Carlo simulation.
  ;;;
  ;;; Arguments:
  ;;;   - `experiment`: Procedure to run one trial of the simulation
  ;;;   - `trial`: Number of times to run the simulation
  ;;;
  (define (iter trials-remaining trials-passed)
    (cond ((= trials-remaining 0)
           (/ trials-passed trials))
          ((experiment)
           (iter (- trials-remaining 1) (+ trials-passed 1)))
          (else
           (iter (- trials-remaining 1) trials-passed))))
  (iter trials 0))


(define (random-in-range low high)
  ;;;
  ;;; Return a random number in the range between `low` and `high`.
  ;;;
  (let ((range (- high low)))
    (+ low (random range))))


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
