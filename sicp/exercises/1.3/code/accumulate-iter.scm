(define (accumulate-iter combiner null-value term a next b)
  ;; A higher-order procedure to generate iterative "accumulation" procedures
  ;; (Like `product` and `sum`)
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (combiner (term a) result))))
  (iter a null-value))

