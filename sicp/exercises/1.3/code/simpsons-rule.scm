(define (h a b n)
  ;; `h` as defined in Simpson's rule
  (/ (- b a) n))

(define (yk f a b n k)
  ;; The incremental function evaluation in the sum term
  ;; of Simpson's rule
  (f (+ a (* k (h a b n)))))

(define (coef k)
  ;; The coefficient of yk in the sum term of Simpson's rule
  (cond ((= 0 k) 1)
        ((even? k) 4)
        (else 2)))

(define (simpsons-sum f a b n k)
  ;; The sum term of Simpson's rule
  (if (= k n)
      (yk f a b n k)
      (+ (* (coef k) (yk f a b n k))
         (simpsons-sum f a b n (+ k 1)))))

(define (simpsons-rule f a b n)
  ;; Compute the definite integral of `f` between `a` and `b`
  ;; to a resolution of `n`
  (* (/ (h a b n) 3) (simpsons-sum f a b n 0)))
