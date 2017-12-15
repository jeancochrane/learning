(define (make-rat n d)
  ;; Constructor for rational numbers.
  ;; Handles negative numbers, and reduces fractions.
  (let ((g (gcd n d))
        (neg (lambda (x) (- 0 (abs x)))))
    (cond ((or (and (negative? n) (negative? d))
               (and (not (negative? n)) (not (negative? d))))
            (cons (/ (abs n) g) (/ (abs d) g)))
          (else
            (cons (/ (neg n) g) (/ (abs d) g))))))
