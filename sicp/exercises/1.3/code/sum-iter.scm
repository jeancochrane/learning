(define (sum term a next b)
  ;; An iterative version of the generic summation procedure.
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (+ (term a) result))))
  (iter a 0))
