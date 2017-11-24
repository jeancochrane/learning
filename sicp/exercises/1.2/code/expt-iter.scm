(define (expt-iter b n)
  (define (iter a b n)
    (cond ((= 0 n) a)
          ((= 1 n) b)
          ((even? n) (iter b (* b b) (/ n 2)))
          (else (* b (iter a b (- n 1))))))
  (define (even? n)
    (= (remainder n 2) 0))
  (iter 1 b n))