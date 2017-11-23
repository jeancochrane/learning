(define (product term a next b)
  ;; A higher-order procedure to generate product procedures
  (if (> a b)
      1
      (* (term a) (product term (next a) next b))))

(define (product-iter term a next b)
  ;; An iterative version of `product`
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (* (term a) result))))
  (iter a 1))

(define (factorial n)
  ;; The factorial function defined in terms of `product`
  (define (term n) n)
  (define (next n) (+ n 1))
  (product term 1 next n))

(define (fact-iter n)
  ;; The factorial function defined in terms of `product-iter`
  (define (term n) n)
  (define (next n) (+ n 1))
  (product-iter term 1 next n))

(define (pi-approx n)
  ;; Approximate pi to the resolution `n`
  (define (term x)
    (if (even? x)
        (/ (+ 2 x) (+ 1 x))
        (/ (+ 1 x) (+ 2 x))))
  (define (next x) (+ 1 x))
  (* 4 (product term 1 next n)))
