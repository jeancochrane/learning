(define (double n)
  (+ n n))

(define (halve n)
  (/ n 2))

(define (even? n)
  (= (remainder n 2) 0))

(define (mult-iter a b)
  ;; Multiply two numbers with an iterative process in O(log n) time
  (define (iter s a b)
    (cond ((= 0 b) s)
          ((= 1 b) a)
          ((even? b) (iter a (double a) (halve b)))
          (else (+ a (iter s a (- b 1))))))
  (iter 1 a b))
