(define (filtered-accumulate combiner null-value filter term a next b)
  ;; Higher-order abstraction to generate accumulation procedures
  ;; (Like sum, product, sum-of-squares)
  (cond ((> a b) null-value)
        ((filter a)
         (combiner (term a)
                (filtered-accumulate combiner null-value filter term (next a) next b)))
        (else (filtered-accumulate combiner null-value filter term (next a) next b))))

(define (sum-of-prime-squares a b)
  ;; Sum the squares of the prime series using `filtered-accumulate`
  (define (filter n) (prime? n))
  (define (combiner a b) (+ a b))
  (define null-value 0)
  (define (term n) (* n n))
  (define (next n) (+ 1 n))
  (filtered-accumulate combiner null-value filter term a next b))

(define (product-of-primes n)
  ;; Find the product of all positive integers less than `n` that
  ;; are relatively prime to `n` (i.e., all positive integers `i < n`
  ;; such that `GCD(i,n) = 1`)
  (define (relative-prime? a)
    (= (gcd a n) 1))
  (define (filter a) (relative-prime? a))
  (define (combiner a b) (* a b))
  (define null-value 1)
  (define (term a) a)
  (define (next a) (+ 1 a))
  (filtered-accumulate combiner null-value filter term 1 next n))
