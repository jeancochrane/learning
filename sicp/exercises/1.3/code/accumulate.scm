(define (accumulate combiner null-value term a next b)
  ;; A higher-order procedure to generate "accumulation" procedures
  ;; (Like `product` and `sum`)
  (if (> a b)
      null-value
      (combiner (term a)
                (accumulate combiner null-value term (next a) next b))))

(define (sum a b)
  (define (combiner a b) (+ a b))
  (define null-value 0)
  (define (term n) n)
  (define (next n) (+ 1 n))
  (accumulate combiner null-value term a next b))

(define (product a b)
  (define (combiner a b) (* a b))
  (define null-value 1)
  (define (term n) n)
  (define (next n) (+ 1 n))
  (accumulate combiner null-value term a next b))
