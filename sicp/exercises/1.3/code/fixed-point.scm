(define (fixed-point f first-guess)
  ;; Compute the fixed point of a function `f` starting with the
  ;; initial value `first-guess`
  (define (close-enough? a b)
    (let ((tolerance 0.001))
        (< (abs (- a b)) tolerance)))
  (define (try guess)
    (let ((next (f guess)))
      (newline)
      (display guess)
      (if (close-enough? guess next)
          guess
          (try next))))
  (try first-guess))

(define (avg x y) (/ (+ x y) 2))

(define (average-damp f)
  (lambda (x) (avg x (f x))))
